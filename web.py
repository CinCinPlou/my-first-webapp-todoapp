# streamlit run web.py

import streamlit as st
import functions
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.set_page_config(layout="wide")

st.title("My Todo App")
st.subheader("This is my first web app, a todo app.")
st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True )

st.text_input(label="input", placeholder="Add new todo..",
             on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # to delete from session sate dictionary
        del st.session_state[todo]
        st.experimental_rerun()




