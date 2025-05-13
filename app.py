import streamlit as st


from libs.llm_utils import send_msg_to_llm,start_session
from libs.menu_loader import load_menu


cake_menu=load_menu()

st.title("🎂 Home Bakery AI Assistant 🎂")
st.markdown("Serving Dubai and Sharjah | Home made cakes 🎂| COD")

if "messages" not in st.session_state:
    start_session()
    welcome_message = (
        " Hi there! Welcome to Habibi Cakes\n\n"
        "Here's our Menu :\n\n" + cake_menu + "\n\n"
        "What would you like to order today? \n\n"
    )
    st.session_state.messages=[{
        "role":"ai",
        "content" : welcome_message
    }]

user_input= st.chat_input("Enter Your Message")

if user_input:
    st.session_state.messages.append({
        "role":"user",
        "content" : user_input
    })
    llm_response=send_msg_to_llm(user_input)
    st.session_state.messages.append({
        "role":"ai",
        "content" : llm_response
    })

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
