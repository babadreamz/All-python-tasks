import to_do_list
import unittest
class TestToDoList(unittest.TestCase):
	def test_if_view_exists(self):
		to_do_list.view_tasks(to_do_list.tasks_list)
	def test_that_view_works(self):
		to_do_list.view_tasks(to_do_list.tasks_list)
		self.assertEqual(to_do_list.view_tasks(to_do_list.tasks_list), to_do_list.view_tasks(to_do_list.tasks_list))

	def test_if_addtasks_exists(self):
		expected = to_do_list.add_tasks("Groceries")
		actual = to_do_list.view_tasks(to_do_list.tasks_list)
		self.assertListEqual(actual,["Groceries"])

	def test_if_addtasks_works(self):	
		to_do_list.tasks_list.clear()
		to_do_list.add_tasks("Buy Groceries")
		actual = to_do_list.view_tasks(to_do_list.tasks_list)
		expected = ["Buy Groceries"]
		self.assertEqual(actual, expected)
	def test_if_delete_task_works(self):
		to_do_list.delete_task(0)
		actual = actual = to_do_list.view_tasks(to_do_list.tasks_list)
		expected = []
		self.assertEqual(actual, expected)
