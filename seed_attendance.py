import os
import django
import random
from datetime import timedelta, date, time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.hrm.models import Employee, Attendance

def run():
    employees = list(Employee.objects.all())
    if not employees:
        print("No employees found! Please run seed_hrm.py first.")
        return

    print("Adding 200+ attendance records across different dates...")

    count = 0
    # Add attendance for the past 30 working days for random employees
    today = date.today()
    for i in range(1, 31):  # last 30 days
        record_date = today - timedelta(days=i)
        # Skip weekends (Saturday=5, Sunday=6 in Python)
        if record_date.weekday() >= 5:
            continue

        # Pick random sample of employees each day (at least 10 per day)
        sampled = random.sample(employees, min(len(employees), random.randint(10, 20)))
        for emp in sampled:
            # Skip if record already exists for this employee+date
            if Attendance.objects.filter(employee=emp, date=record_date).exists():
                continue

            status = random.choices(
                ['Present', 'Absent', 'Late', 'Leave'],
                weights=[70, 10, 15, 5]
            )[0]

            check_in = None
            check_out = None
            working_hours = None

            if status == 'Present':
                check_in = time(9, random.randint(0, 15))
                check_out = time(18, random.randint(0, 45))
                working_hours = 9.0
            elif status == 'Late':
                check_in = time(10, random.randint(0, 59))
                check_out = time(18, random.randint(0, 45))
                working_hours = round(8 - random.uniform(0.5, 1.5), 2)

            Attendance.objects.create(
                employee=emp,
                date=record_date,
                check_in=check_in,
                check_out=check_out,
                working_hours=working_hours,
                status=status
            )
            count += 1

    print(f"Done! Successfully added {count} new attendance records.")
    print(f"Total attendance records in DB: {Attendance.objects.count()}")

if __name__ == '__main__':
    run()
