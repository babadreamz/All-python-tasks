payroll_statement = []

def employee_details(employee_name, hours_entered, wage, fed_tax, state_tax):
	if not employee_name:
		raise ValueError("name cannot be empty")
	payroll = {"name": employee_name, "no_of_hours": hours_entered, "hourly_pay": wage, "fed_tax": fed_tax, "state_tax": state_tax}
	payroll_statement.append(payroll)

def number_of_hours_worked(index, hours_entered):
	if hours_entered < 0 or hours_entered > 168:
		raise ValueError("number of hours must be between 0 and 168 in a week ")
	payroll_statement[index]["no_of_hours"] = hours_entered
	return payroll_statement[index]["no_of_hours"]

def current_fed_tax(index, fed_tax):
	if fed_tax < 1 or fed_tax > 100:
		raise ValueError("number of hours must be between 0 and 168 in a week ")
	fed_tax_percent = fed_tax /100
	payroll_statement[index]["fed_tax"] = fed_tax_percent
	return payroll_statement[index]["fed_tax"]

def current_state_tax(index, state_tax):
	if state_tax < 1 or state_tax > 100:
		raise ValueError("number of hours must be between 0 and 168 in a week ")
	state_tax_percent = state_tax /100
	payroll_statement[index]["state_tax"] = state_tax_percent
	return payroll_statement[index]["state_tax"]


def pay_per_hour(index, wage):
	if wage < 0:
		raise ValueError("Your pay cannot be less 0 ")
	payroll_statement[index]["hourly_pay"] = wage
	return payroll_statement[index]["hourly_pay"]

def set_employee_name(index, employee_name):
	if not isinstance(employee_name, str):
		raise TypeError("Name must be a string ")
	payroll_statement[index]["name"] = employee_name
def get_payroll_statement():
	if not payroll_statement:
		raise ValueError
	return payroll_statement


def update_payroll(search_input):
	for payroll in payroll_statement:
		if search_input.lower() == payroll["name"].lower():
			return payroll
		raise ValueError ("Search does not match either an payroll")