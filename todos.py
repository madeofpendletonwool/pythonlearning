print('''
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/

Welcome to Todos. Your friendly commandline
todo list. 
****************************************************
''')

todo_list = []
finished_list = []

def list_todos():
        ordered_number = 1
        list_item = 0
        for item in todo_list:
            print(f"{ordered_number}. {todo_list[list_item]}")
            list_item += 1
            ordered_number += 1


while True:
    print("Please enter a command. Otherwise type 'h' for help:")
    user_input = input("> ")
    if user_input == "h":
        print('''TODO LIST HELP
    Type 'q' to quit
    To add a todo to the list, type it and hit enter
    To complete a todo enter its number
    ''')
    elif user_input.isdigit() == True:
        remove_item = int(user_input)
        remove_item -= 1
        finished_item = todo_list.pop(remove_item)
        finished_list.append(finished_item)

        list_todos()

    elif user_input == "q":
        finished_count = len(finished_list)
        print(f"Great job today! You finished {finished_count} tasks!")
        
        finish_number = 1
        finish_list_count = 0
        for item in finished_list:
            print(f"{finish_number}. {finished_list[finish_list_count]}")
            finish_number += 1
            finish_list_count += 1
        break
    else:
        todo_list.append(user_input)

        ordered_number = 1
        list_item = 0
        for item in todo_list:
            print(f"{ordered_number}. {todo_list[list_item]}")
            list_item += 1
            ordered_number += 1