# main_memory_demo.py
from agent_with_memory import create_agent_with_window_memory # Import agent executor đã có memory

if __name__ == "__main__":
    print("\n--- DEMO AGENT VỚI ConversationBufferWindowMemory (k=2) ---")
    # Tạo MỘT instance agent_executor cho phiên này
    agent_executor = create_agent_with_window_memory()
    print("\n1.User] Trạng thái của TASK-001 là gì?")
    res_w1 = agent_executor.invoke({"input": "Trạng thái của TASK-001 là gì?"})
    print(f"[Agent] {res_w1['output']}") # Lượt 1 (user + AI)

    print("\n2.[User] Nó được giao cho ai?")
    res_w2 = agent_executor.invoke({"input": "Nó được giao cho ai?"})
    print(f"[Agent] {res_w2['output']}") # Lượt 2 (user + AI) - Vẫn nhớ TASK-001

    print("\n3.[User] Alice là ai??")
    res_w3 = agent_executor.invoke({"input": "Alice là ai?"})
    print(f"[Agent] {res_w3['output']}") # Lượt 2 (user + AI) - Vẫn nhớ TASK-001


    print("\n4.[User] Deadline của TASK-003 là khi nào?")
    res_w4 = agent_executor.invoke({"input": "Deadline của TASK-003 là khi nào?"})
    print(f"[Agent] {res_w4['output']}") # Lượt 3 (user + AI) - Nhớ TASK-001 và TASK-003

    print("\n5.[User] Hỏi TASK-003 ai phụ trách?")
    res_w5 = agent_executor.invoke({"input": "Ai phụ trách này?"})
    print(f"[Agent] {res_w5['output']}") # Lượt 4 (user + AI) - Nhớ TASK-003

    print("\n6.[User] Nhắc lại xem người thực hiện TASK-001 là ai?") # Lượt 5
    # Vì k=2, nó chỉ nhớ 2 lượt gần nhất (TASK-003 và câu hỏi này).
    # Thông tin về TASK-001 có thể đã bị "quên".
    res_w6 = agent_executor.invoke({"input": "Alice là người thực hiện task nào?"})
    print(f"[Agent] {res_w6['output']}") # Quan sát xem Agent có trả lời đúng không hay yêu cầu cung cấp lại task_id
    
    # print("\n[User] Trạng thái của TASK-001 là gì?")
    # res_w1 = create_agent_with_window_memory().invoke({"input": "Trạng thái của TASK-001 là gì?"})
    # print(f"[Agent] {res_w1['output']}") # Lượt 1 (user + AI)

    # print("\n[User] Nó được giao cho ai?")
    # res_w2 = create_agent_with_window_memory().invoke({"input": "Nó được giao cho ai?"})
    # print(f"[Agent] {res_w2['output']}") # Lượt 2 (user + AI) - Vẫn nhớ TASK-001

    # print("\n[User] Deadline của TASK-003 là khi nào?")
    # res_w3 = create_agent_with_window_memory().invoke({"input": "Deadline của TASK-003 là khi nào?"})
    # print(f"[Agent] {res_w3['output']}") # Lượt 3 (user + AI) - Nhớ TASK-001 và TASK-003

    # print("\n[User] Hỏi TASK-003 ai phụ trách?")
    # res_w3 = create_agent_with_window_memory().invoke({"input": "Ai phụ trách này?"})
    # print(f"[Agent] {res_w3['output']}") # Lượt 4 (user + AI) - Nhớ TASK-003

    # print("== Chat history hiện tại ==")
    # for msg in create_agent_with_window_memory().memory.chat_memory.messages:
    #     print(msg)
    # print("===========================")

    # print("\n[User] Nhắc lại xem người thực hiện TASK-001 là ai?") # Lượt 5
    # # Vì k=2, nó chỉ nhớ 2 lượt gần nhất (TASK-003 và câu hỏi này).
    # # Thông tin về TASK-001 có thể đã bị "quên".
    # res_w4 = create_agent_with_window_memory().invoke({"input": "Nhắc lại xem người thực hiện đầu tiên là ai?"})
    # print(f"[Agent] {res_w4['output']}") # Quan sát xem Agent có trả lời đúng không hay yêu cầu cung cấp lại task_id