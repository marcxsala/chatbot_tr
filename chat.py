import re

import long_responses


def message_probability(user_message, recognized_words, single_response=False, required_words=None):
    if required_words is None:
        required_words = []
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1
    percentage = float(message_certainty) / float(len(recognized_words))

    # Comprova que les paraules requerides son al fil
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=None):
        if required_words is None:
            required_words = []
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Resposta--------------------------------------------------------------------------------------------------------------x
    response("Hello!", ["hello", "hi", "sup", "hey", "heyo"], single_response=True)
    response("I\'m doing Fine, How about you?", ["how", "are", "you", "doing"])
    response("Yes", ["i", "love", "barcelona"], required_words=["barcelona", "love"])
    response(long_responses.R_EATING, ["what", "you", "eat"], required_words=["you", "eat"])
    response(long_responses.R_Futbol, ["t'agrada", "el", "futbol"], required_words=["t'agrada", "futbol"])
    response(long_responses.R_Hora, ["hora"], required_words=["hora"])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)

    return long_responses.unknwon() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r"\s+|[,:?!.-]\s*", user_input.lower())
    response = check_all_messages(split_message)
    return response


# PROVANT EL SISTEMA DE REPSOSTES
while True:
    print("Bot: " + str(get_response(input("You:"))))


#Borra el restant. Incrementa certesa a les respostes.

