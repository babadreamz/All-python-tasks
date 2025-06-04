from employee_payroll import *
print("<<=====WELCOME TO SEMICOLON EMPLOYEES PORTAL=====>>")
while True:
	print("""
	1. Add employee payroll
	2. View Employee payroll
	3. Update Employee payroll
	4. Exit
		""")
	user_input = input("Enter a selection (1 - 4) ")
	match (user_input):
		case "1":
			employee_name = input(" Enter Employee name:  ")
			number_hours = int(input("Enter number of hours:  "))
			wage = int(input("Enter the hourly per rate:  "))
			fed_tax = int(input("Enter federal withholding rate: "))
			state_tax = int(input("Enter state withholding rate: "))
			print(employee_details(employee_name, number_hours, wage, fed_tax, state_tax))
			print("ACCOUNT ADDED SUCCESSFULLY")
			print("Do you wish to Continue with anything? yes/no")
			userchoice = input()
			if userchoice.lower() == "no":
				break
			else:
				continue
		case "2":
			print(get_payroll_statement())
			userchoice = input()
			if userchoice.lower() == "no":
				print("Goodbye")
				break
			else:
				continue
		case "3":
			print("Search by employee name")
			search = input("Enter employee name here: ")
			print(update_payroll(search))
			userchoice = input()
			if userchoice.lower() == "no":
				break
			else:
				continue
		case "4":
			print("Goodbye")
			break
		case _:
			continue