# main_memory_demo.py
from agent_with_memory import create_agent_with_buffer_memory # Import agent executor đã có memory

if __name__ == "__main__":
    print("--- DEMO AGENT VỚI ConversationBufferMemory ---")
    # Tạo MỘT instance agent_executor cho phiên này
    agent_executor = create_agent_with_buffer_memory()

    print("\n[User] Trạng thái của TASK-001 là gì?")
    response1 = agent_executor.invoke({"input": "Trạng thái của TASK-001 là gì?"})
    print(f"[Agent] {response1['output']}")

    print("\n[User] Nó được giao cho ai?") # Câu hỏi follow-up
    response2 = agent_executor.invoke({"input": "Nó được giao cho ai?"})
    print(f"[Agent] {response2['output']}")

    print("\n[User] Mô tả chi tiết của task đó là gì?") # Câu hỏi follow-up khác
    response3 = agent_executor.invoke({"input": "Mô tả chi tiết của task đó là gì?"})
    print(f"[Agent] {response3['output']}")

    print("\n[User] Thế còn TASK-002 thì sao, deadline của nó là khi nào?") # Chuyển sang task khác
    response4 = agent_executor.invoke({"input": "Thế còn TASK-002 thì sao, deadline của nó là khi nào?"})
    print(f"[Agent] {response4['output']}")

    print("\n[User] Nó được giao cho ai vậy?") # Follow-up cho TASK-002
    response5 = agent_executor.invoke({"input": "Nó được giao cho ai vậy?"})
    print(f"[Agent] {response5['output']}")