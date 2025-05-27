tasks_list = []
list_menu = ["1 - add_task", "2 - view_tasks", "3 - mark_as_completed", "4 - delete_task", "5 - exit"]

def menu():
	print('''
	1. Add Tasks
	2. View Tasks
	3. Mark as Completed
	4. Delete Task
	5. Exit
		''')
def view_tasks(tasks_list):
	return tasks_list

def add_tasks(task_name):
	tasks_list.append(task_name)

def delete_task(index):
	tasks_list.pop(index)

'''
def mark_completed(task_done):
	task_1 = int(task_done)
	marked_task = tasks(task_done)
	task_1
'''






