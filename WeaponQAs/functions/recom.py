import jieba
import pickle

def recom(question: str):
    weapon_name_list = pickle.load(open('selected_weapon_name_list.pkl', 'rb'))
    for weapon_name in weapon_name_list:
        jieba.add_word(weapon_name, tag='weapon_name', freq=300000)
    word_seg = list(jieba.cut(question, cut_all=False))
    weapon_list = pickle.load(open('weapon_list.pkl', 'rb'))
    recommendation_content = '当前问题无推荐答案'
    for seg in word_seg: 
        for weapon_name in weapon_name_list:
            if seg == weapon_name:
                for weapon in weapon_list:
                    if weapon['名称'] == weapon_name:
                        recommendation_content = weapon
        return recommendation_content

print(recom('M1114装甲车的产国是？'))