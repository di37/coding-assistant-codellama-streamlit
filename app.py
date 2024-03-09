from utils import *

# app config
st.set_page_config(page_title="🤖 Friendly Coding Assistant ✨", page_icon="🤖")
st.title("🤖 CodyBot - Your Friendly, Coding Assistant! ✨")

# Setting generation configuration - This will override the parameter that is set in the Modelfile
get_config_gen = configure_generation()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello, I am CodyBot - Your Friendly, Coding Assistant!. How can I help you?"),
    ]

for message in st.session_state.chat_history:
    with st.chat_message("AI" if isinstance(message, AIMessage) else "Human"):
        st.write(message.content)

# user input
if user_query := st.chat_input("Type your message here..."):
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    with st.chat_message("Human"):
        st.write(user_query)

    with st.chat_message("AI"):
        response_placeholder = st.empty()
        full_response = ""
        for chunk in get_realtime_response(user_prompt=user_query, **get_config_gen):
            full_response += chunk
            response_placeholder.write(full_response)
        logger.info("Response successfully generated.")
    
    st.session_state.chat_history.append(AIMessage(content=full_response))
