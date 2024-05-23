from datetime import datetime
from ProctoringApp.models import Exam


def update_status():
    now = datetime.now()
    current_date = now.date()
    current_time = now.time()

    for exam in Exam.objects.all():
        if exam.start_date == current_date:
            if exam.start_time <= current_time <= exam.end_time:
                exam.status = "Active"
            elif current_time < exam.start_time:
                pass  # The provided time is in the future
            else:
                exam.status = "Completed"
        else:
            if exam.start_date < current_date:
                exam.status = "Completed"
            else:
                pass  # The provided date is in the future
        exam.save()

