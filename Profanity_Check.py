from profanity_check import predict, predict_prob
import random

def profanity_check(user_input):
    return predict([user_input])


# def test_accuracy():
#   texts = [
#     'Hello there, how are you',
#     'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
#     '!!!! Click this now!!! -> https://example.com',
#     'fuck you',
#     'fUcK u',
#     'GO TO hElL, you dirty scum',
#   ]
#   assert list(predict(texts)) == [0, 0, 0, 1, 1, 1]
#
#   probs = predict_prob(texts)
#   for i in range(len(probs)):
#     if i < 3:
#       assert probs[i] <= 0.5
#     else:
#       assert probs[i] >= 0.5
#
# def test_edge_cases():
#   texts = [
#     '',
#     '                    ',
#     'this is but a test string, there is no offensive language to be found here! :) ' * 25,
#     'aaaaaaa' * 100,
#   ]
#   assert list(predict(texts)) == [0, 0, 0, 0]

def give_candidate():
    return "response"

def exchange(session_id: str,
                  user_input: str = None):

    candidate_reponses=[
        "I am well behaved lady. I can't answer that",
        "Please stop using these kind of words",
        "If you keep speaking like that I will kick you out",
        "Did you hear about the receptionist that murdered the customer that insulted her"
    ]
    response=candidate_reponses[random.randint(0, len(candidate_reponses)-1)]
    return response