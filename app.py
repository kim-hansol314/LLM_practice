import streamlit as st
from scenario import generate_crime_scenario
from suspect import generate_suspects
from chains import get_suspect_chain
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="LLM 기반 용의자 추리 게임", layout="centered")

# 세션 상태 초기화
if "scenario" not in st.session_state:
    st.session_state.scenario = None
if "suspects" not in st.session_state:
    st.session_state.suspects = []
if "chat_logs" not in st.session_state:
    st.session_state.chat_logs = {}
if "turn" not in st.session_state:
    st.session_state.turn = 0
if "max_turns" not in st.session_state:
    st.session_state.max_turns = 9
if "selected_suspect" not in st.session_state:
    st.session_state.selected_suspect = None
if "final_choice" not in st.session_state:
    st.session_state.final_choice = None

st.title("🔍 LLM 기반 용의자 추리 게임")

# 게임 시작 버튼
if st.button("🕵️ 게임 시작") or st.session_state.scenario is None:
    st.session_state.scenario = generate_crime_scenario()
    st.session_state.suspects = generate_suspects(st.session_state.scenario)
    st.session_state.chat_logs = {s['name']: [] for s in st.session_state.suspects}
    st.session_state.turn = 0
    st.session_state.final_choice = None
    st.rerun()

# 사건 개요 출력
st.subheader("사건 개요")
st.info(st.session_state.scenario['summary'])

# 용의자 목록 출력
st.subheader("용의자 목록")
for s in st.session_state.suspects:
    st.markdown(f"**{s['name']}** - {s['description']}")

# 질문을 진행하는 부분
if st.session_state.turn < st.session_state.max_turns:
    st.markdown(f"### 🗣️ {st.session_state.turn+1} / {st.session_state.max_turns}번째 질문")

    # 용의자 선택
    st.session_state.selected_suspect = st.selectbox("대화할 용의자를 선택하세요", [s['name'] for s in st.session_state.suspects])

    # 질문 입력 form
    with st.form("chat_form"):
        user_question = st.text_input("질문을 입력하세요", key="user_input")
        submitted = st.form_submit_button("질문하기")

    if submitted and user_question:
        suspect_name = st.session_state.selected_suspect

        chain = get_suspect_chain(suspect_name, st.session_state.scenario, st.session_state.suspects)
        response = chain.run(question=user_question)

        st.session_state.chat_logs[suspect_name].append((user_question, response))

        st.session_state.turn += 1
        st.rerun()

else:
    # 게임 종료 후 범인 지목
    st.markdown("## 🤔 범인을 지목하세요")
    final_choice = st.radio("범인은 누구입니까?", [s['name'] for s in st.session_state.suspects])
    if st.button("🔎 정답 확인"):
        st.session_state.final_choice = final_choice
        true_culprit = next(s for s in st.session_state.suspects if s['is_culprit'])
        if final_choice == true_culprit['name']:
            st.success("🎉 정답입니다! 범인을 정확히 지목하셨습니다.")
        else:
            st.error(f"😢 틀렸습니다. 진짜 범인은 **{true_culprit['name']}** 입니다.")
        st.markdown(f"#### 📝 범인의 설명: {true_culprit['truth']}")

# 대화 로그 출력
st.markdown("---")
st.subheader("💬 대화 로그")
for suspect, chats in st.session_state.chat_logs.items():
    st.markdown(f"**{suspect}**")
    for q, a in chats:
        st.markdown(f"- **Q:** {q}")
        st.markdown(f"  - **A:** {a}")
