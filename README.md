# 🔍 Chat Detective: LLM 기반 용의자 추리 게임

![screenshot](https://img.shields.io/badge/Built%20with-LangChain-blue?style=flat-square)
![streamlit](https://img.shields.io/badge/Frontend-Streamlit-orange?style=flat-square)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI-green?style=flat-square)

---

## 🎮 프로젝트 소개

**Chat Detective**는 GPT 기반 AI 용의자들과 대화를 통해, 범인을 추리하는 인터랙티브 텍스트 추리 게임입니다.  
무고한 용의자들은 모두 사실만 말하지만, **범인은 일부 허점을 보입니다.** 당신의 추리력이 범인을 찾아낼 수 있을까요?

---

## 🧠 사용 기술

| 항목 | 기술 |
|------|------|
| UI | Streamlit |
| LLM | OpenAI GPT / Ollama (eeve) |
| 프레임워크 | LangChain |
| 메모리 | ConversationBufferMemory |
| 설정 방식 | 용의자별 역할 프롬프트 기반 롤플레이 |

---

## 🧭 실행 순서

1. **Streamlit 앱 실행**
   ```bash
   streamlit run app.py
   ```

2. **"게임 시작" 클릭**
   - 사건 시나리오 자동 생성
   - 용의자 3명 등장 (직업/성격/알리바이 포함)

3. **용의자 선택 후 질문하기**
   - 유저는 사전 설정된 턴 안에 원하는 질문 가능

4. **범인 지목**
   - 유저는 누가 범인인지 선택
   - 결과 및 진짜 범인의 해명 확인

---

## 🧪 사용 예시

### 🕵️ 사건 시나리오 예시
> 도심 호텔의 스위트룸에서 유명 연예인이 칼에 찔려 사망했습니다. 범행은 새벽 2시경 발생했으며, 비서와 지인 두 명이 함께 있었습니다. CCTV에는 피해자가 마지막으로 엘리베이터를 탄 장면만 남아있습니다.

### 💬 유저 질문
> 사건 당시 어디에 있었습니까?

### 🤖 AI 응답 (결백한 용의자)
> 저는 방에서 자고 있었습니다. 사건은 전혀 몰랐고, 아침에 경찰이 도착하고 나서야 알게 되었습니다.

### 🤖 AI 응답 (범인)
> 사건 당시에는 근처에 있었지만, 정확한 시간은 기억이 잘 나지 않습니다. 피해자와 말다툼이 있었던 건 사실이지만 해칠 의도는 없었습니다.

---

## 🧠 AI 응답 방식

| 구분 | 방식 | 설명 |
|------|------|------|
| ✅ 결백한 용의자 | 사실만 말함 | 알리바이, 피해자와 관계, 감정 일관됨 |
| ⚠️ 범인 | 허점 포함한 진술 | 의심을 피하기 위해 거짓말을 할 수 있지만, 알리바이에 허점을 보임 |
| 🧠 기억 유지 | LangChain Memory 사용 | 이전 질문을 기억하고, 대화를 이어나감 |

---

## 📁 프로젝트 구조

```
chat-detective-game/
├── app.py               # Streamlit 메인 앱
├── scenario.py          # 사건 시나리오 생성
├── suspect.py           # 용의자 설정
├── chains.py            # LLMChain + 메모리
├── prompt.py            # 역할 기반 프롬프트
└── README.md
```

---


## 🛠 향후 개선 가능성

- [ ] 게임 재시작 버튼
- [ ] 신뢰도 시각화
- [ ] 용의자 성격 다양화
- [ ] 추리 힌트 시스템
