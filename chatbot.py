import streamlit as st
import os
# from streamlit_chat import message
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage


class Chatbot:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=self.google_api_key,
                                          convert_system_message_to_human=True)

    def answer(self, inp, lvl):
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro", google_api_key=self.google_api_key)
        messages = [
            ("system",
             f"You are TalkMate, a helpful and intelligent assistant. Based on the user's proficiency level {lvl}, adjust your communication style to match their understanding. Respond to the user input: {inp} with appropriate language complexity. If the input contains any grammatical or sentence structure errors, politely point them out and explain how to improve. Additionally, suggest a few synonyms or similar vocabulary words suited to their level to help them expand their language skills. Provide feedback on how much they’ve improved, with examples to show progress and areas for further development"),
            ("human", f"{inp}"),
        ]

        stream = llm.stream(messages)

        return stream

    def run_bot(self):
        st.header("Welcome to TalkTuner")

        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "level" not in st.session_state:
            st.session_state.level = None

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        # Select level if not previously selected
        if st.session_state.level is None:
            st.session_state.level = st.selectbox("Select your proficiency level:",
                                                  ["Beginner", "Intermediate", "Advanced"])

        # Accept user input
        if prompt := st.chat_input("Say Something.."):  # Changed to st.text_input
            # store output
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("assistant"):

                stream = self.answer(prompt, st.session_state.level)

                if st.session_state.level == "Beginner":
                    response = st.write_stream(stream)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                elif st.session_state.level == "Intermediate":
                    response = st.write(stream)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                elif st.session_state.level == "Advanced":
                    response = st.write(stream)
                    st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    bot = Chatbot()
    bot.run_bot()
