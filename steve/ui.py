import uuid

import streamlit as st
from streamlit_chat import message

# Setting page title and header
st.title("Steve")
message("""How can I help you today?""",
        avatar_style="thumbs")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


# generate a response
def generate_response(user_input):
    import time
    time.sleep(2)
    return "test"


placeholder = st.empty()
st.markdown("""---""")
user_input = st.text_input("Your message:", key='input')


def render_messages():
    if st.session_state['chat_history']:
        for i in range(len(st.session_state['chat_history'])):
            msg_obj = st.session_state["chat_history"][i]
            message(msg_obj["message"],
                    is_user=msg_obj["is_user"],
                    key=str(uuid.uuid4()),
                    avatar_style="thumbs" if not msg_obj["is_user"] else "adventurer-neutral")


if user_input:
    st.session_state['chat_history'].append({"is_user": True, "message": user_input})
    with placeholder.container():
        render_messages()

if user_input:
    ai_response = generate_response(user_input)
    st.session_state['chat_history'].append({"is_user": False, "message": ai_response})

with placeholder.container():
    render_messages()
