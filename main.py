from employee_class import Employee

print("*==================================*")
print("* 1. show employee list            *")
print("* 2. add employee                  *")
print("* 3. update employee               *")
print("* 4. delete employee               *")
print("* 5. quit app                      *")
print("*==================================*")

employees = []

while True:

    input_number = int(input("insert number >>>> "))

    if input_number == 1:
        
        number = 0

        for info in employees:
            print(number," :Name: ",info.name)
            number += 1

    elif input_number == 2:
        add_employee_name = input("insert employee's name >>>> ")
        add_employee_age = int(input("insert age >>>> "))
        add_employee_phone_number = int(input("insert phone number >>>> "))
        add_employee_id = int(input("insert id >>>> "))
        
        employee = Employee(add_employee_name,add_employee_age,add_employee_phone_number,add_employee_id)
        
        employees.append(employee)
        
        print("new employee added >>>> {}".format(employee.name))

    elif input_number == 3:

        number = 0

        for info in employees:
            print(number," :Name: ",info.name)
            number += 1

        before_employee = int(input("insert number of employee to change"))
        
        add_employee_name = input("insert new employee's name >>>> ")
        add_employee_age = int(input("insert age >>>> "))
        add_employee_phone_number = int(input("insert phone number >>>> "))
        add_employee_id = int(input("insert id >>>> "))
        
        employee  = Employee(add_employee_name,add_employee_age,add_employee_phone_number,add_employee_id)
        employees[before_employee] = employee
        
        print("[] is a added".format(add_employee_name))

    elif input_number == 4:
        
        number = 0

        for info in employees:
            print(number," :Name: ",info.name)
            number += 1
        
        
        delete_employees = int(input("insert the number of employee to delete >>>> "))
        print("{} is deleted ".format(employees[delete_employees]))
        employees.pop(delete_employees)
        
    
    elif input_number == 5:
        break

    else:
        print("this number does not exist")

print("exit")
