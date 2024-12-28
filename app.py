from flask import Flask, render_template, request, redirect, url_for
from logic import find_top_gifts
from dataset import data

app = Flask(__name__)
questions = [
    {
        "id": 0,
        "question": "What is your recipient gender ?",
        "options": {
            0: "Male",
            1: "Female"
        },
    },
    {
        "id": 1,
        "question": "How old is your recipient ?",
        "options": {
            0: "1-13",
            1: "14-20",
            2: "21-35",
            3: "36-65",
            4: "66-100"
        },
    },
    {
        "id": 2,
        "question": "What is your relationship with the recipient ?",
        "options": {
            0: "Friend",
            1: "Family",
            2: "Partner",
        }
    },
    {
        "id": 3,
        "question": "What is the occasion ?",
        "options": {
            0: "Birthday",
            1: "Anniversary",
            2: "Graduation",
            3: "Holiday",
        },
    },
    {
        "id": 4,
        "question": "What are your recipient most interest ?",
        "options": {
            0: "Sports",
            1: "Technology",
            2: "Music",
            3: "Art",
            4: "Fashion",
            5: "Book",
            6: "Cooking",
            7: "Travel",
            8: "Gaming",
            9: "Movies",
            10: "Pets"

        },
    },
    {
        "id": 5,
        "question": "What is your budget ?",
        "options": {
            0: "0-300,000 T",
            1: "300,000-1,000,000 T",
            2: "1,000,000-5,000,000 T",
            3: "5,000,000-20,000,000 T",
            6: "20,000,000-100,000,000 T",
            7: "More than 100,000,000 T"
        },
    }
]

user_answers = {}


@app.route("/")
def index():
    return render_template("welcome.html")


@app.route("/question/<int:question_id>", methods=["GET", "POST"])
def question(question_id):
    global user_answers

    if request.method == "POST":
        answer = request.form.get("answer")
        user_answers[question_id - 1] = int(answer)

    if question_id >= len(questions):
        return redirect(url_for("results"))

    question_data = questions[question_id]
    return render_template(
        "question.html",
        question=question_data["question"],
        options=question_data["options"],
        question_id=question_id,
    )


@app.route("/results")
def results():
    print(user_answers)
    gift_suggestions = find_top_gifts(user_answers, data)
    return render_template("result.html", suggestions=gift_suggestions)


if __name__ == "__main__":
    app.run(debug=True)
