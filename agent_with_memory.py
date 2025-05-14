# agent_with_memory.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory

from tools_v2 import available_tools # Import tools từ file tools_v2.py

load_dotenv()


# Gợi ý trong agent_with_memory.py
def create_agent_with_buffer_memory():
    # ... khởi tạo LLM, tools, prompt, ConversationBufferMemory ...
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    prompt = hub.pull("hwchase17/react-chat")
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    agent = create_react_agent(llm, available_tools, prompt)
    return AgentExecutor(agent=agent, tools=available_tools, memory=memory, verbose=True, handle_parsing_errors=True)

def create_agent_with_window_memory(k_val=2):
    # ... khởi tạo LLM, tools, prompt, ConversationBufferWindowMemory ...
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    prompt = hub.pull("hwchase17/react-chat")
    memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True, k=k_val)
    agent = create_react_agent(llm, available_tools, prompt)
    return AgentExecutor(agent=agent, tools=available_tools, memory=memory, verbose=True, handle_parsing_errors=True)
