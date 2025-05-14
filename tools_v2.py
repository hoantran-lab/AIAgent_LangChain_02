# tools_v2.py
from datetime import datetime, date
from langchain_core.tools import tool
from config import project_data

# (Giữ nguyên 3 tools: get_task_status, get_task_deadline, calculate_remaining_time từ video 1)
# ... (copy code 3 tools đó vào đây) ...

@tool
def get_task_status(task_id: str) -> str:
    """Trả về trạng thái hiện tại của một công việc dựa trên mã công việc (task_id)."""
    # ... (code như video 1)
    task_id = task_id.upper()
    task = project_data.get(task_id)
    if task:
        return f"Trạng thái của công việc '{task['name']}' ({task_id}) là: {task['status']}"
    else:
        return f"Lỗi: Không tìm thấy công việc với mã {task_id}."

@tool
def get_task_deadline(task_id: str) -> str:
    """Trả về hạn chót (deadline) của một công việc dựa trên mã công việc (task_id)."""
    # ... (code như video 1)
    task_id = task_id.upper()
    task = project_data.get(task_id)
    if task:
        return f"Hạn chót của công việc '{task['name']}' ({task_id}) là: {task['deadline']}"
    else:
        return f"Lỗi: Không tìm thấy công việc với mã {task_id}."

@tool
def calculate_remaining_time(task_id: str) -> str:
    """Tính toán và trả về số ngày còn lại cho đến hạn chót của một công việc dựa trên mã công việc (task_id)."""
    # ... (code như video 1)
    task_id = task_id.upper()
    task = project_data.get(task_id)
    if not task:
        return f"Lỗi: Không tìm thấy công việc với mã {task_id}."
    try:
        deadline_str = task.get('deadline')
        if not deadline_str:
             return f"Lỗi: Công việc {task_id} không có thông tin deadline."
        deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d").date()
        today = date.today()
        remaining_days = (deadline_date - today).days
        if remaining_days < 0:
            return f"Công việc '{task['name']}' ({task_id}) đã quá hạn {abs(remaining_days)} ngày (Deadline: {deadline_str})."
        elif remaining_days == 0:
            return f"Công việc '{task['name']}' ({task_id}) đến hạn vào hôm nay (Deadline: {deadline_str})."
        else:
            return f"Công việc '{task['name']}' ({task_id}) còn {remaining_days} ngày nữa là đến hạn (Deadline: {deadline_str})."
    except ValueError:
        return f"Lỗi: Định dạng deadline '{deadline_str}' của công việc {task_id} không hợp lệ (cần YYYY-MM-DD)."
    except Exception as e:
        return f"Lỗi không xác định khi tính toán thời gian cho {task_id}: {str(e)}"

@tool
def get_task_assignee(task_id: str) -> str:
    """Trả về người được giao (assignee) của một công việc dựa trên mã công việc (task_id)."""
    task_id = task_id.upper()
    task = project_data.get(task_id)
    if task and task.get('assignee'):
        return f"Công việc '{task['name']}' ({task_id}) được giao cho: {task['assignee']}."
    elif task:
        return f"Công việc '{task['name']}' ({task_id}) chưa có thông tin người được giao."
    else:
        return f"Lỗi: Không tìm thấy công việc với mã {task_id}."

@tool
def get_task_description(task_id: str) -> str:
    """Trả về mô tả chi tiết của một công việc dựa trên mã công việc (task_id)."""
    task_id = task_id.upper()
    task = project_data.get(task_id)
    if task and task.get('description'):
        return f"Mô tả của công việc '{task['name']}' ({task_id}): {task['description']}."
    elif task:
        return f"Công việc '{task['name']}' ({task_id}) chưa có mô tả chi tiết."
    else:
        return f"Lỗi: Không tìm thấy công việc với mã {task_id}."

# Cập nhật danh sách tools
available_tools = [
    get_task_status,
    get_task_deadline,
    calculate_remaining_time,
    get_task_assignee,
    get_task_description
]