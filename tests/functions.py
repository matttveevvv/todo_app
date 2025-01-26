FILEPATH = "todos.txt"

def get_todos(filepeth = FILEPATH):

    with open("todos.txt", "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepeth = FILEPATH):
    with open("todos.txt", "w") as file:
        file.writelines(todos)

if __name__ == "__maine__":
    print("Hello")
    print(get_todos())