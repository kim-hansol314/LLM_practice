# scenario.py
import random

def generate_crime_scenario():
    scenarios = [
        "한 저택에서 부유한 사업가가 독살당한 채 발견되었습니다.",
        "도심 호텔에서 유명 연예인이 칼에 찔려 사망했습니다.",
        "대학 연구실에서 과학자가 의문의 약물에 의해 사망했습니다."
    ]
    return {"summary": random.choice(scenarios)}