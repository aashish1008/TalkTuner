import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


class YourCompanion:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=self.google_api_key,
                                          convert_system_message_to_human=True)

    def answer(self, inp, catg):
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro", google_api_key=self.google_api_key)
        messages = [
            ("system",
             f'''You are a helpful assistant named TalkMate. Based on the selected role '{catg}', provide the best 
             possible responses to the user input: '{inp}'. When the user selects '{catg}', begin the role-specific 
             process. If the input contains grammar or sentence mistakes, notify the user and offer feedback on their 
             performance and improvement. If the input is not relevant to the selected role '{catg}', kindly inform 
             the user that their response is off-topic and request input related to '{catg}'.'''),

            ("human", f"{inp}"),
        ]

        stream = llm.stream(messages)

        return stream

    def run_companion(self):
        st.subheader("Your Companion : TalkMate is here for you.")

        if "companion_history" not in st.session_state:
            st.session_state.companion_history = []
        if "categories" not in st.session_state:
            st.session_state.categories = None

        for message in st.session_state.companion_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Initialize the session state for categories if not already set
        if 'categories' not in st.session_state:
            st.session_state.categories = None

        # Initialize the session state for categories if not already set
        if 'categories' not in st.session_state:
            st.session_state.categories = None

        # Role selection logic
        if st.session_state.categories is None:
            selected_category = st.selectbox("Select your desired role:",
                                             ["Role Play", "Case Study", "Stress Management", "Group Discussion"])
            if st.button("Confirm Role"):
                st.session_state.categories = selected_category
                st.experimental_rerun()  # Refresh the app to reflect the new role selection
        else:
            st.write(f"Current Role: {st.session_state.categories}")
            if st.button("Change Roles"):
                st.session_state.categories = None
                st.experimental_rerun()  # Refresh the app to allow for new role selection

        # Accept user input
        if prompt := st.chat_input("Say Something.."):  # Changed to st.text_input
            # Store output
            st.session_state.companion_history.append({"role": "user", "content": prompt})

            with st.chat_message("assistant"):
                stream = self.answer(prompt, st.session_state.categories)

                if st.session_state.categories == "Role Play":
                    response = st.write_stream(stream)
                    st.session_state.companion_history.append({"role": "assistant", "content": response})
                elif st.session_state.categories == "Case Study":
                    response = st.write(stream)
                    st.session_state.companion_history.append({"role": "assistant", "content": response})
                elif st.session_state.categories == "Stress Management":
                    response = st.write(stream)
                    st.session_state.companion_history.append({"role": "assistant", "content": response})
                elif st.session_state.categories == "Group Discussion":
                    response = st.write(stream)
                    st.session_state.companion_history.append({"role": "assistant", "content": response})
