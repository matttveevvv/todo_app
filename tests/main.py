import time
import functions

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete and exit: ")

    todo = user_action[4:].capitalize() + "\n"

    if user_action.startswith("add"):
        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        number = int(user_action[5:])
        number = number - 1

        todos = functions.get_todos()

        new_todos = input("Enter new todos: ").capitalize() + "\n"
        todos[number] = new_todos

        functions.write_todos(todos)

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = functions.get_todos()

            remove_todo = todos[number].strip("\n")
            todos.pop(number)

            functions.write_todos(todos)

            print(f"Todo {remove_todo} was removed.")

        except IndexError:
            print("Your command is not valid!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("")

print("Bye!")





