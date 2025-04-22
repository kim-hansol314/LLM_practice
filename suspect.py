# suspects.py
import random

def generate_suspects(scenario):
    names = ["김지훈", "이서연", "박민수"]
    roles = ["비서", "동료", "형제"]
    descriptions = [
        "침착하고 말수가 적습니다.",
        "활발하고 질문에 적극적입니다.",
        "감정 기복이 크고 격앙되어 있습니다."
    ]

    culprit_index = random.randint(0, 2)
    suspects = []
    for i in range(3):
        is_culprit = (i == culprit_index)
        suspects.append({
            "name": names[i],
            "role": roles[i],
            "description": descriptions[i],
            "is_culprit": is_culprit,
            "truth": "실제로 범인이며, 범행 당시 피해자와 말다툼 끝에 사건이 발생함." if is_culprit else "사건 당시 다른 장소에 있었으며, 피해자와 크게 관련은 없음."
        })
    return suspects