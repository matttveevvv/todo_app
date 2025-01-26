def get_todos(filepeth = "todos.txt"):

    with open("todos.txt", "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepeth = "todos.txt"):
    with open("todos.txt", "w") as file:
        file.writelines(todos)