#this is list that will store the individual payroll of each employee
payroll_statement = [] 

# here i want to create the payroll of each employee with those details listed as parameters
def employee_details(employee_name, hours_entered, wage, fed_tax, state_tax):
	if not employee_name:
		raise ValueError("name cannot be empty")
	payroll = {"name": employee_name, "no_of_hours": hours_entered, "hourly_pay": wage, "fed_tax": fed_tax, "state_tax": state_tax}
	payroll_statement.append(payroll)

# here i want to weekly hours worked
def number_of_hours_worked(index, hours_entered):
	if hours_entered < 0 or hours_entered > 168:
		raise ValueError("number of hours must be between 0 and 168 in a week ")
	payroll_statement[index]["no_of_hours"] = hours_entered
	return payroll_statement[index]["no_of_hours"]

# here i want to set the federal tax
def current_fed_tax(index, fed_tax):
	if fed_tax < 1 or fed_tax > 100:
		raise ValueError("federal tax must be between 1 and 100")
	fed_tax_percent = fed_tax /100
	payroll_statement[index]["fed_tax"] = fed_tax_percent
	return payroll_statement[index]["fed_tax"]

# here i want to set state tax
def current_state_tax(index, state_tax):
	if state_tax < 1 or state_tax > 100:
		raise ValueError("state tax must be between 1 and 100 ")
	state_tax_percent = state_tax /100
	payroll_statement[index]["state_tax"] = state_tax_percent
	return payroll_statement[index]["state_tax"]

# here i want to set the hourly_pay
def pay_per_hour(index, wage):
	if wage < 0:
		raise ValueError("Your pay cannot be less 0 ")
	payroll_statement[index]["hourly_pay"] = wage
	return payroll_statement[index]["hourly_pay"]
# here i want to set employee name
def set_employee_name(index, employee_name):
	if not isinstance(employee_name, str):
		raise TypeError("Name must be a string ")
	payroll_statement[index]["name"] = employee_name

#Here i want to view the payroll
def get_payroll_statement():
	if not payroll_statement:
		raise ValueError("No payroll records found")
	return payroll_statement

# Here I want to search the payroll by name, and the update the said payroll e.g change employee_name etc
def update_payroll(search_input):
	for payroll in payroll_statement:
		if search_input.lower() == payroll["name"].lower():
			update = employee_details(employee_name, hours_entered, wage, fed_tax, state_tax)
			payroll_statement.append(update)
			return update
		raise ValueError ("Search does not match either an payroll")