# chains.py
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.memory import ConversationBufferMemory
from prompt import build_prompt

models = {}
memories = {}

def get_suspect_chain(name, scenario, all_suspects):
    if name not in models:
        suspect = next(s for s in all_suspects if s['name'] == name)
        system_prompt = build_prompt(suspect, scenario, all_suspects)

        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(system_prompt),
            HumanMessagePromptTemplate.from_template("{question}")
        ])

        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        llm = ChatOpenAI(temperature=0.7)

        chain = LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=False)

        models[name] = chain
        memories[name] = memory

    return models[name]
