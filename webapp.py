# If getting error -> Error: Streamlit requires raw Python (.py) files, but the provided file has no extension.
# It's because space in the path, to fix it needs to place path to " "
# Example: streamlit run "E:/Doc/Python course/Tasks-python311/webapp.py"
# To create file for lib dependencies: pip freeze > requirements.txt

import streamlit as st
from modules import functions as fn


todos = fn.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    fn.write_todos(todos_local=todos)
    st.session_state["new_todo"] = ""


st.title("My ToDo App")
st.subheader("This is my todo app.")
st.write('This app is to do increase productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"cb{index}")
    if checkbox:
        todos.pop(index)
        del st.session_state[f"cb{index}"]
        fn.write_todos(todos_local=todos)
        st.rerun()


st.text_input(label="Enter todo:", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")


st.session_state
