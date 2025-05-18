menu_choice = True
while menu_choice:
	print("""====== WELCOME TO NOKIA 3310 ======
		1. Phone book
		2. Messages
		3. Chat
		4. Call register	
		5. Tones
		6. Settings
		7. Call divert	
		8. Games		
		9. Calculator	
 		10. Reminders
		11. Clock	
		12. Profiles	
		13. SIM services	
		Enter 0 to turnoff
	""")
	menu = int(input())
	if menu == 0:
		print('Goodbyee...')
		menu_choice = False
	elif menu == 1:
		while True:
			print(''' 
			1. Search
			2. Search NOs.
			3. Add name
			4. Erase
			5. Edit
			6. Assign tone
			7. Send b'card
			8. Options	
			9. Speed dials
			10. Voice tags	
			Enter 0 to return to previous menu			
			''')
			phone_choice = int(input())
		
			if phone_choice == 0:
				break

			elif phone_choice == 1:
				while True:
					print("Search")
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break

			elif phone_choice == 2:
				while True:
					print("Search NOs.")
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break

			elif phone_choice == 3:
				while True:
					print("Add name")
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break

			elif phone_choice == 4:
				while True:
					print("Erase")
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break

			elif phone_choice == 5:
				while True:
					print("Edit")
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break

			elif phone_choice == 6:
				while True:
					print("Assign tone")
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break

			elif phone_choice == 7:
				while True:
					print("Send b'card")
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break

			elif phone_choice == 8:
				while True:
					print(''' 
						1. Type of view
						2. Memory status
						Enter 0 to return
					''')
					phone_choice_8 = int(input())
					if phone_choice_8 == 0:
						break
					elif phone_choice_8 == 1:
						while True:
							print('Type of view')
							back = int(input("Enter 0 to return to previous menu: "))
							if back == 0:
								break

					elif phone_choice_8 == 2:
						while True:
							print('Memory status')
							back = int(input("Enter 0 to return to previous menu: "))
							if back == 0:
								break

					else:
						print('Invalid selection')

			elif phone_choice == 9:
				while True:
					print("Speed dials")
					back = input("Enter 0 to return to previous menu: ")
					if back == 0:
						break

			elif phone_choice == 10:
				while True:
					print("Voice tags")
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break
			else:
				print('Invalid Selection')

	elif menu == 2:
		while True:
			print(''' 
			1. Write messages 
			2. Inbox
			3. Outbox
			4. Picture messages
			5. Templates
			6. Smileys
			7. Message settings
			8. Info service
			9. Voice mailbox number
			10. Service command editor
			Enter 0 to return to previous menu
			''')
			message_option = int(input())
			if message_option == 0:
				break
			elif message_option == 1:
				while True:
					print('Write messages')
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break
			elif message_option == 2:
				while True:
					print('Inbox')
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break
			elif message_option == 3:
				while True:
					print('Outbox')
					back = int(input("Enter 0 to return to messages menu: "))
					if back == 0:
						break
			elif message_option == 4:
				while True:
					print('Picture messages')
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break
			elif message_option == 5:
				while True:
					print('Templates')
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break
			elif message_option == 6:
				while True:
					print('Smileys')
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break
			elif message_option == 7:
				while True:
					print(''' 
						1. Set 1^2
						2. Common^3
						''')
					message_option_7 = int(input())
					if message_option_7 == 0:
						break
					elif message_option_7 == 1:
						while True:
							print('''
							1. Message Centre number
							2. Message sent as
							3. Message validity
							Enter 0 to return''')
							message_option_7_1 = int (input())
							if message_option_7_1 == 0:
								break
							elif message_option_7_1 == 1:
								while True:
									print('Message centre number')
									back = int(input("Enter 0 to return to Previous menu: "))
									if back == 0:
										break
							elif message_option_7_1 == 2:
								while True:
									print(' Message sent as')
									back = int(input("Enter 0 to return to previous menu: "))
									if back == 0:
										break
							elif message_option_7_1  == 3:
								while True:
									print('Message validity')
									back = int(input("Enter 0 to return to previous menu: "))
									if back == 0:
										break
							else: 
								print('Invalid selection')
										
					elif message_option_7 == 2:	
						while True:
							print(''' 
							1.Delivery reports
							2.Message sent as
							3.Character support
							Enter 0 to return
								''')
							message_option_7_2 = int(input())
							if message_option_7_2 == 0:
								break
							elif message_option_7_2 == 1:
								while True:
									print('Message sent as')
									back = int(input("Enter 0 to return to previous menu: "))
									if back == 0:
										break
							elif message_option_7_2  == 2:
								while True:
									print('Message sent as')
									back = int(input("Enter 0 to return to previous menu: "))
									if back == 0:
										break
							elif message_option_7_2 == 3:
								while True:
									print('Character support')
									back = int(input("Enter 0 to return to previous menu: "))
									if back == 0:
										break
							else:
								print('Invalid selection')
			elif message_option == 8:
				while True:
					print('Info service')	
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break
			elif message_option == 9:
				while True:
					print('Voice mailbox')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break
			elif message_option == 10:
				while True:
					print('Service command editor')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break
	elif menu == 3:
		while True:
			print('Chat')
			back = int(input("Enter 0 to return to phonebook menu: "))
			if back == 0:
				break
	elif menu == 4:
		while True:
			print('''
				1. Missed calls
				2. Recieved calls
				3. Dialled numbers
				4. Erase recent call lists
				5. Show call duration
				6. Show call costs
				7. Call cost settings
				8. Prepaid credit
				Enter 0 to return to previous menu 	
				''')
			call_reg_options = int(input())
			if call_reg_options == 0:
				break;
			elif call_reg_options == 1:
				while True:
					print('Missed calls')
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break
			elif call_reg_options == 2:
				while True:
					print('Recieved calls')
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break
			elif call_reg_options == 3:
				while True:
					print('Dialled numbers')
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break
			elif call_reg_options == 4:
				while True:
					print('Erase recent call lists')
					back = int(input("Enter 0 to return to previous menu: "))
					if back == 0:
						break
			elif call_reg_options == 5:
				while True:
					print(''' 
					1. Last call duration
					2. All calls duration
					3. Recieved calls duration
					4. Dialled calls duration
					5. Clear timers
					Enter 0 to return to previous menu
						''')
					call_reg_options_5 = int(input())
					if call_reg_options_5 == 0:
						break
					elif call_reg_options_5 == 1:
						while True:
							print('Last call duration')
							back = int(input("Enter 0 to return to previous menu: "))
							if back == 0:
								break
					elif call_reg_options_5 == 2:
						while True:
							print('All calls duration')
							back = int(input("Enter 0 to return to previous menu: "))
							if back == 0:
								break
					elif call_reg_options_5 == 3:
						while True:
							print('Recieved calls duration')
							back = int(input("Enter 0 to return to previous menu: "))
							if back == 0:
								break
					elif call_reg_options_5 == 4:
						while True:
							print('Dialled calls duration')
							back = int(input("Enter 0 to return to previous menu: "))
							if back == 0:
								break
					elif call_reg_options_5 == 5:
						while True:
							print('Clear timers')
							back = int(input("Enter 0 to return to previous menu: "))
							if back == 0:
								break
					else:
						print('Invalid selection')
			elif call_reg_options == 6:
				while True:
					print(''''
					1. Last call cost
					2. All call costs
					3. Clear counters
					Enter 0 to return to previous menu''')
					call_reg_options_6 = int(input())
					if call_reg_options_6 == 0:
						break
					elif call_reg_options_6 == 1:
						while True:
							print('Last call cost')
							back = int(input("Enter 0 to return to previous menu: "))
							if back == 0:
								break
					elif call_reg_options_6 == 2:
						while True:
							print('All call costs')
							back = int(input("Enter 0 to return to previous menu: "))
							if back == 0:
								break
					elif call_reg_options_6 == 3:
						while True:
							print('Clear counterss')
							back = int(input("Enter 0 to return to previous menu: "))
							if back == 0:
								break
					else:
						print('Invalid selection')
						
			elif call_reg_options == 7:
				while True:
					print(''' 
					1. Call cost limit
					2. Show costs in
					Enter 0 to return to previous menu
					''')			
					call_reg_options_7 = int(input())
					if call_reg_options_7 == 0:
						break
					elif call_reg_options_7 == 1:
						while True:
							print('Call cost limit')
							back = int(input("Enter 0 to return to previous menu: "))
							if back == 0:
								break
					elif call_reg_options_7 == 2:
						while True:
							print('Show costs in')
							back = int(input("Enter 0 to return to previous menu: "))
							if back == 0:
								break
					else:
						print('Invalid selection')
			elif call_reg_options == 8:
				while True:
					print('Prepaid Credit')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break
	elif menu == 5:
		while True:
			print(''' 
			1. Ringing tone
			2. Ringing volume
			3. Incoming call alert
			4. Composer
			5. Message alert tone
			6. Keypad tones
			7. Warning and game tones
			8. Vibrating alert
			9. Screen saver	
			Enter 0 to return to previous menu
			''')
			tones_options = int(input())
			if tones_options == 0:
				break
			elif tones_options == 1:
				while True:
					print('Ringing tone')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break
			elif tones_options == 2:
				while True:
					print('Ringing volume')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break
			elif tones_options == 3:
				while True:
					print('Incoming call alert')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break	
			elif tones_options == 4:
				while True:
					print('Composer')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break	
			elif tones_options == 5:
				while True:
					print('Message alert tone')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break
			elif tones_options == 6:
				while True:
					print('Keypad tones')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break	
			elif tones_options == 7:
				while True:
					print('Warning and game tones')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break	
			elif tones_options == 8:
				while True:
					print('Vibrating alert')
					back = input("Enter 0 to return to phonebook menu: ")
					if back == 0:
						break	
			elif tones_options == 9:
				while True:
					print('Screen saver')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break	
			else:
				print('Invalid selection')
	
	elif menu == 6:
		while True:
			print(''' 
			1. Call settings
			2. Phone settings
			3. Security settings
			4. Restore factory settings
			Enter 0 to return to previous menu
			''') 
			settings_options = int(input())
			if settings_options == 0:
				break
			elif settings_options == 1:
				while True:
					print(''' 
					1. Automatic redial
					2. Speed dialling
					3. Call waiting options
					4. Own number sending
					5. Phone line in use
					6. Automatic answer
					Enter 0 to return to previous menu	
					''')
					settings_options_1 = int(input())
					if settings_options_1 == 0:
						break
					elif settings_options_1 == 1:
						while True:
							print('Automatic redial')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					elif settings_options_1 == 2:
						while True:
							print('Speed dialling')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					elif settings_options_1 == 3:
						while True:
							print('Call waiting options')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					elif settings_options_1 == 4:
						while True:
							print('Own number sending')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					elif settings_options_1 == 5:
						while True:
							print('Phone line in use')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					elif settings_options_1 == 6:
						while True:
							print('Automatic answer')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					else:
						print('Invalid selection')
			elif settings_options == 2:
				while True:
					print(''' 
					1. Language 
					2. Cell info display
					3. Welcome note
					4. Network selection
					5. Lights
					6. Confirm SIM service actions
					Enter 0 to return to previous menu
					''')
					settings_options_2 = int(input())
					if settings_options_2 == 0:
						break
					elif settings_options_2 == 1:
						while True:
							print('Language')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					elif settings_options_2 == 2:
						while True:
							print('Cell info display')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					elif settings_options_2 == 3:
						while True:
							print('Welcome note')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					elif settings_options_2 == 4:
						while True:
							print('Network selection')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					elif settings_options_2 == 5:
						while True:
							print('Lights')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					elif settings_options_2 == 6:
						while True:
							print('Confirm SIM service actions')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					else:
						print('Invalid input')
			elif settings_options == 3:
				while True:
					print(''' 
					1. Pin code request
					2. Call info display
					3. Welcome note
					4. Closed user group
					5. Phone security
					6. Change access codes
					Enter 0 to return
					''')
					settings_options_3 = int(input())
					if settings_options_3 == 0:
						break
					elif settings_options_3 == 1:
						while True:
							print('Pin code request')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					elif settings_options_3 == 2:
						while True:
							print('Call info display')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					elif settings_options_3 == 3:
						while True:
							print('Welcome note')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break	
					elif settings_options_3 == 4:
						while True:
							print('Closed user group')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break
					elif settings_options_3 == 5:
						while True:
							print('Phone security')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break
					elif settings_options_3 == 6:
						while True:
							print('Change access codes')
							back = int(input("Enter 0 to return to phonebook menu: "))
							if back == 0:
								break
					else:
						print('Invalid selection')
			elif settings_options == 4:
				while True:
					print('Restore factory settings')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break	
			else:
				print('Invalid selection')
	elif menu == 7:
		while True:
			print('Call divert')
			back = int(input("Enter 0 to return to phonebook menu: "))
			if back == 0:
				break
	elif menu ==8:
		while True:
			print('Games')
			back = int(input("Enter 0 to return to phonebook menu: "))
			if back == 0:
				break
	elif menu == 9:
		while True:
			print('Calculator')
			back = int(input("Enter 0 to return to phonebook menu: "))
			if back == 0:
				break
	elif menu == 10:
		while True:
			print('Reminders')
			back = int(input("Enter 0 to return to phonebook menu: "))
			if back == 0:
				break
	elif menu == 11:
		while True:
			print(''' 
			1. Alarm clock
			2. Clock settings 
			3. Date setting
			4. Stopwatch
			5. Countdown timer
			6. Auto update of date and time
			Enter 0 to return to previous menu
			''')
			clock_options = int(input())
			if clock_options == 0:
				break
			elif clock_options == 1:
				while True:
					print('Alarm clock')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break
			elif clock_options == 2:
				while True:
					print('Clock settings')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break
			elif clock_options == 3:
				while True:
					print('Date setting')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break
			elif clock_options == 4:
				while True:
					print('Stopwatch')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break
			elif clock_options == 5:
				while True:
					print('Countdown timer')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break
			elif clock_options == 6:
				while True:
					print('Auto update of date and time')
					back = int(input("Enter 0 to return to phonebook menu: "))
					if back == 0:
						break
			else:
				print('Invalid selection')
	elif menu == 12:
		while True:
			print('Profiles')
			back = int(input("Enter 0 to return to phonebook menu: "))
			if back == 0:
				break
	elif menu == 13:
		while True:
			print('SIM services')
			back = int(input("Enter 0 to return to phonebook menu: "))
			if back == 0:
				break
	else:
		print('Invalid selection')