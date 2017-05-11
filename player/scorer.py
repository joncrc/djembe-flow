"""
Module for scores handling.
"""


def get_scores(file):
    # return a dictionary

    # Load scores from file to list
    text_file = open(file, "r")
    lines = text_file.readlines()
    text_file.close()

    score = {}

    for line in lines:
        if ":" in line:
            line = line.replace(" ", "").replace("\n", "")
            line = line.split(':')
            score[line[0]+"_score"] = list(line[1])

    # print(score)
    return score


# get_scores("../scores/moribayassa.sc")
