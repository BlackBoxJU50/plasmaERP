import os
import django
import random
from datetime import timedelta, date, time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from faker import Faker
from apps.hrm.models import Employee, Department, Designation, LeaveType, Attendance, LeaveRequest, Payroll
from apps.core.models import Company, Branch
from apps.accounts.models import User

fake = Faker()

# Bangladeshi Name Data
first_names_m = ["Rahim", "Karim", "Tariq", "Hasan", "Arif", "Imran", "Sajid", "Rakib", "Mehedi", "Faisal", "Nafis", "Sakib", "Tanvir", "Mahmud", "Ahsan"]
first_names_f = ["Fatema", "Ayesha", "Khadija", "Nusrat", "Sadia", "Sumaiya", "Tania", "Mithila", "Farhana", "Nadia", "Tasnim", "Sabrina", "Zareen"]
last_names = ["Rahman", "Islam", "Hossain", "Ahmed", "Chowdhury", "Khan", "Sikder", "Miah", "Ali", "Haque", "Uddin", "Akter", "Khatun", "Begum"]

# IT Company Data
departments_list = ["Software Engineering", "Quality Assurance", "Product Management", "UI/UX Design", "DevOps & Cloud", "Data Science", "Human Resources", "IT Support", "Cybersecurity", "Sales & Marketing"]
roles_list = ["Junior Software Engineer", "Software Engineer", "Senior Software Engineer", "Tech Lead", "QA Engineer", "Senior QA Engineer", "UI/UX Designer", "Product Manager", "Scrum Master", "DevOps Engineer", "Data Analyst", "Data Scientist", "HR Executive", "System Administrator", "Cybersecurity Analyst", "Marketing Executive"]
leave_types_list = ["Casual Leave", "Sick Leave", "Annual Leave", "Maternity Leave", "Paternity Leave", "Unpaid Leave", "Compensatory Off", "Study Leave", "Bereavement Leave", "Marriage Leave"]

def generate_bd_phone():
    prefixes = ["017", "019", "018", "016", "015", "013", "014"]
    return "+88" + random.choice(prefixes) + "".join([str(random.randint(0, 9)) for _ in range(8)])

def run():
    print("Deleting old records...")
    Payroll.objects.all().delete()
    LeaveRequest.objects.all().delete()
    Attendance.objects.all().delete()
    Employee.objects.all().delete()
    LeaveType.objects.all().delete()
    Designation.objects.all().delete()
    Department.objects.all().delete()

    print("Seeding database for a Bangladeshi IT Company...")
    company, _ = Company.objects.get_or_create(name="Plasma IT Solutions Ltd.", defaults={'status': True})
    branch, _ = Branch.objects.get_or_create(company=company, name="Dhaka HQ", code="DHK01", defaults={'status': True, 'address': 'Banani, Dhaka, Bangladesh'})
    user, _ = User.objects.get_or_create(username="admin_approver", defaults={'email': 'admin@plasma.com'})
    user.set_password('password')
    user.save()

    print("Creating 100 Departments (Teams)...")
    departments = []
    for i in range(100):
        base_dept = random.choice(departments_list)
        name = f"{base_dept} - Team {fake.word().capitalize()} {i}"
        dept = Department.objects.create(name=name[:150], description=f"Focuses on {base_dept} operations.")
        departments.append(dept)

    print("Creating 100 Designations...")
    designations = []
    for i in range(100):
        name = random.choice(roles_list) + f" Level {random.randint(1,5)} (ID:{i})"
        desig = Designation.objects.create(name=name[:150], department=random.choice(departments))
        designations.append(desig)

    print("Creating 100 Leave Types...")
    leave_types = []
    for i in range(100):
        name = random.choice(leave_types_list) + f" Category {i}"
        lt = LeaveType.objects.create(name=name[:100], days_allowed=random.randint(5, 30))
        leave_types.append(lt)

    print("Creating 100 Bangladeshi IT Employees...")
    employees = []
    for i in range(100):
        gender = random.choice(['M', 'F'])
        first_name = random.choice(first_names_m) if gender == 'M' else random.choice(first_names_f)
        last_name = random.choice(last_names)
        emp = Employee.objects.create(
            employee_code=f"EMP-BD-{str(i+1).zfill(4)}",
            first_name=first_name,
            last_name=last_name,
            email=f"{first_name.lower()}.{last_name.lower()}{i}@plasmait.com.bd",
            phone=generate_bd_phone(),
            gender=gender,
            dob=fake.date_of_birth(minimum_age=22, maximum_age=45),
            joining_date=fake.date_between(start_date='-5y', end_date='today'),
            designation=random.choice(designations),
            department=random.choice(departments),
            branch=branch,
            salary=random.randint(30000, 200000), # BDT salary
            status=True
        )
        employees.append(emp)

    print("Creating 100 Attendances...")
    for emp in employees:
        Attendance.objects.create(
            employee=emp,
            date=date.today(),
            check_in=time(9, random.randint(0, 30)),
            check_out=time(18, random.randint(0, 45)),
            working_hours=random.choice([8.0, 8.5, 9.0]),
            status='Present'
        )

    print("Creating 100 Leave Requests...")
    for emp in employees:
        LeaveRequest.objects.create(
            employee=emp,
            leave_type=random.choice(leave_types),
            start_date=date.today() + timedelta(days=random.randint(1, 30)),
            end_date=date.today() + timedelta(days=random.randint(31, 35)),
            reason=random.choice(["Family emergency", "Vacation to Cox's Bazar", "Medical checkup", "Personal reasons", "Eid Holidays"]),
            status=random.choice(['Pending', 'Approved', 'Rejected']),
            approved_by=user
        )

    print("Creating 100 Payrolls...")
    for emp in employees:
        allowance = 5000.0  # House rent & transport
        deduction = 1000.0  # Tax or provident fund
        Payroll.objects.create(
            employee=emp,
            month=date.today().replace(day=1),
            basic_salary=emp.salary,
            allowance=allowance,
            bonus=0.0,
            deduction=deduction,
            net_salary=float(emp.salary) + allowance - deduction,
            paid_status=random.choice(['Paid', 'Processing'])
        )

    print("Database seeding completed successfully! Added 100 Bangladeshi IT records.")

if __name__ == '__main__':
    run()
