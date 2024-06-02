from datetime import datetime
from ProctoringApp.models import Exam


def update_status():
    now = datetime.now()
    current_date = now.date()
    current_time = now.time()

    for exam in Exam.objects.all():
        if exam.start_date > current_date:
            exam.status = "In Active"
        elif exam.start_date == current_date == exam.end_date:
            if exam.start_time <= current_time <= exam.end_time:
                exam.status = "Active"
            elif current_time < exam.start_time:
                exam.status = "In Active"
            else:
                exam.status = "Completed"
        
