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

# Sau đó trong main_memory_demo.py
# from agent_with_memory import create_agent_with_buffer_memory, create_agent_with_window_memory
# agent_executor_buffer = create_agent_with_buffer_memory()
# agent_executor_window = create_agent_with_window_memory(k_val=2)
# # Rồi gọi invoke trên từng executor

# # --- Hàm tạo AgentExecutor với ConversationBufferMemory ---
# def create_agent_with_buffer_memory():
#     """
#     Khởi tạo và trả về một AgentExecutor được cấu hình với ConversationBufferMemory.
#     """
#     print("Đang khởi tạo Agent với ConversationBufferMemory...")

#     # 1. Khởi tạo LLM (ví dụ: GPT-4)
#     # temperature=0 để giảm tính ngẫu nhiên, giúp Agent đưa ra quyết định nhất quán hơn
#     llm = ChatOpenAI(model="gpt-4", temperature=0)

#     # 2. Lấy danh sách các tools
#     # available_tools đã được import từ tools_v2.py
#     tools = available_tools
#     if not tools:
#         print("LƯU Ý: Không có tools nào được cung cấp cho Agent.")


#     # 3. Tải Agent Prompt Template
#     # Sử dụng prompt ReAct được thiết kế sẵn từ LangChain Hub,
#     # loại "react-chat" thường được tối ưu hơn cho việc sử dụng memory.
#     # Nếu không có sẵn, bạn có thể dùng "hwchase17/react"
#     try:
#         prompt = hub.pull("hwchase17/react-chat")
#     except Exception as e:
#         print(f"Không thể tải prompt 'hwchase17/react-chat', thử 'hwchase17/react'. Lỗi: {e}")
#         prompt = hub.pull("hwchase17/react")


#     # 4. Khởi tạo ConversationBufferMemory
#     # memory_key="chat_history" phải khớp với tên biến mà prompt template sử dụng
#     # để chèn lịch sử hội thoại.
#     # return_messages=True là quan trọng khi làm việc với ChatModels.
#     memory = ConversationBufferMemory(
#         memory_key="chat_history",
#         return_messages=True
#     )

#     # 5. Tạo Agent
#     # Kết hợp LLM, tools, và prompt để tạo agent
#     agent = create_react_agent(llm, tools, prompt)

#     # 6. Tạo AgentExecutor
#     # Môi trường thực thi cho agent, bao gồm cả memory.
#     # verbose=True để in ra quá trình suy nghĩ và hành động của agent khi chạy.
#     # handle_parsing_errors=True giúp agent xử lý tốt hơn các lỗi parsing từ LLM.
#     agent_executor = AgentExecutor(
#         agent=agent,
#         tools=tools,
#         memory=memory,  # Truyền đối tượng memory vào đây
#         verbose=True,
#         handle_parsing_errors=True # Nên có để xử lý lỗi LLM output không đúng format
#     )

#     print("Agent với ConversationBufferMemory đã sẵn sàng!")
#     return agent_executor

# # --- Khởi tạo LLM ---
# # temperature=0 để giảm tính ngẫu nhiên, giúp Agent đưa ra quyết định nhất quán hơn
# # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
# llm = ChatOpenAI(model="gpt-4", temperature=0)

# # --- Tải Agent Prompt ---
# # Sử dụng prompt ReAct được thiết kế sẵn từ LangChain Hub
# # prompt = hub.pull("hwchase17/react")
# prompt = hub.pull("hwchase17/react-chat")
# print (f"Prompt: {prompt}")

# # --- Tạo Agent ---
# # Kết hợp LLM, tools, và prompt để tạo agent
# agent = create_react_agent(llm, available_tools, prompt)

# # --- Tạo bộ nhớ cho Agent ---
# # Sử dụng ConversationBufferMemory để lưu trữ lịch sử hội thoại
# # memory_key là tên khóa để lưu trữ lịch sử hội thoại
# # return_messages=True để trả về danh sách các tin nhắn trong lịch sử hội thoại
# # Bộ nhớ này sẽ giúp agent ghi nhớ các thông tin đã trao đổi trong quá khứ
# # (có thể sử dụng cho các lần gọi tiếp theo)
# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# # --- Tạo AgentExecutor ---
# # Tạo môi trường thực thi cho agent
# # verbose=True để in ra quá trình suy nghĩ và hành động của agent khi chạy
# agent_executor_with_buffer_memory = AgentExecutor(agent=agent, tools=available_tools, memory=memory, verbose=True, handle_parsing_errors=True)




# # In mô tả tools (tùy chọn, để kiểm tra)
# print("--- Tools được Agent sử dụng ---")
# for tool in available_tools:
#     print(f"- {tool.name}: {tool.description}")
# print("-" * 20)

