import to_do_list
print("======= To-Do list manager =========")
while True:
	print(to_do_list.menu())
	choice = input("Select one option above ")
	match choice:
		case "5":
			break
		case "1":
			to_do_list.add_tasks(input("Enter task here: "))
			break
		case "2":
			to_do_list.view_tasks(to_do_list.tasks_list)
			break
		case "3":
			"Mark any one as completed"
			to_do_list.view_tasks(to_do_list.tasks_list)
			break
		case "4":
			what_to_delete = input("Select an index to delete from, start from 0 ")
			to_do_list.delete_task((what_to_delete))
			break
		

