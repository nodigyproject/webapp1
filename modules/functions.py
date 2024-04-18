import os

# FILEPATH = os.getcwd() + r"\files\todos.txt"
FILEPATH = r"todos.txt"
# print(f"Current directory = {FILEPATH}")


def get_todos(path=FILEPATH): #default parameter
    """
    Read text file and
    return the list of to-do items
    """
#    print(path)
    try:
        # 'with automatically close the file, recommended to use this way, not file = open()'
        with open(path, 'r') as file_local:
            todos_local = file_local.readlines()
        return todos_local
    except:
        print(f"Read - Something wrong with variables path = {path}")
        quit()


# print(help(get_todos)) # Will print function documentation


def write_todos(path=FILEPATH, todos_local=[]):
    """
    Write to-do items
    to the text file
    """
    try:
        with open(path, 'w') as file_local:
            file_local.writelines(todos_local)
        return "Success"
    except:
        print(f"Write - Something wrong with variables todos_local or path = {path}")
        quit()


# print(__name__)

# Conditional block
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
