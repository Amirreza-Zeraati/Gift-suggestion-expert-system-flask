def find_top_gifts(input_pattern, dataset, top_n=3):
    input_list = [input_pattern[i] for i in sorted(input_pattern)]
    match_scores = []

    for row in dataset[1:]:
        gift = row[0]
        row_features = row[1:]
        matches = 0

        for input_val, row_val in zip(input_list, row_features):
            if input_val == row_val:
                matches += 1

        match_scores.append((gift, matches))

    top_gifts = sorted(match_scores, key=lambda x: x[1], reverse=True)[:top_n]
    return [gift for gift, score in top_gifts]
