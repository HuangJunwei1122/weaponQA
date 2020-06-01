from Levenshtein import jaro
import pickle

def fetch_answer(Q_input):
    score_list = list(map(lambda x: jaro(x, Q_input), Q_list))
    highest_score = max(score_list)
    highest_score_index = score_list.index(highest_score)
    selected_answer = A_list[highest_score_index]
    score_list.pop(highest_score_index)
    second_highest_score = max(score_list)
    return selected_answer, highest_score, second_highest_score

with open('QA_dict.pkl', 'rb') as f:
    QA_dict = pickle.load(f)
Q_list, A_list = list(QA_dict.keys()), list(QA_dict.values())

# print(fetch_answer('CNS航母的建造时间是？'))
# ('2007年', 0.8425925925925926, 0.7976190476190476)