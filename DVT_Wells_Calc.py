# ==================================== #
#      DVT Wells Score Calculator      #
#     by M.Flitton and M.Stammers      #
# ==================================== #

print("Welcome to the DVT_Wells PyScorer Program")
print("You will be asked a series of questions in order to calculate the full modern Wells score")

DVT_score = 0

def question_function(score, question_string, score_increase):
    yes = 'yes'
    no = 'no'
    answer_array = yes + no

    question = input(question_string).lower()

    while question not in answer_array:
        question = input(question_string)

    if question in yes:
        score = score + score_increase
        print("The score was {}".format(score-score_increase))
        if score_increase < 0:
            score_show = score_increase * (-1)
            print("This has decreased the score by {}".format(score_show))
        else:
            print("This increased the score by {}".format(score_increase))

    elif question in no:
        print('The score is unchanged.')

    else:
        print("There is an error!")

    return score

def DVT_scorer(score):
    if score < 2:
        print("This is a low risk score. Please consider other causes first.")
    elif score > 1:
        print("This is a high risk score. Please proceed to investigate for DVT with venous dopplers.")
    else:
        print("There has been an error.")

DVT_score = question_function(DVT_score, 'Does the patient have active cancer? ', 1)
DVT_score = question_function(DVT_score, 'Is the patient recently bedbound > 3 days or surgery less than a month ago? ', 1)
DVT_score = question_function(DVT_score, 'Calf swelling more than 3 cm compared to the other leg? ', 1)
DVT_score = question_function(DVT_score, 'Are collateral non-varicose veins present? ', 1)
DVT_score = question_function(DVT_score, "Entire leg swollen? ", 1)
DVT_score = question_function(DVT_score, "Localised tenderness along the deep venous system? ", 1)
DVT_score = question_function(DVT_score, "Pitting oedema confined to the symptommatic leg? ", 1)
DVT_score = question_function(DVT_score, "Recent plaster or paralysis of the lower extremity? ", 1)
DVT_score = question_function(DVT_score, "Previous documented DVT? ", 1)
DVT_score = question_function(DVT_score, "Alternative diagnosis just as likely or more likely? ", -2)

print("The Full DVT Wells score is: {}".format(DVT_score))
print(DVT_scorer(DVT_score))


print("The Full DVT Wells score is: {}".format(DVT_score))
print(DVT_scorer(DVT_score))
