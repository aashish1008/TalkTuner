# TalkTuner

TalkTuner is a unique communication enhancement tool that offers users interactive experiences through role-based scenarios and AI-driven chatbot conversations. It is designed to help users develop communication skills by adapting to their proficiency level or specific roles.

## Features

   **1. ChatBot:**
   Level-Based Conversations: Users can engage in conversations tailored to their communication level:
   
   - **Beginner:** Basic conversational skills.
   - **Intermediate:** Mid-level communication, including more complex sentence structures.
   - **Advanced:** High-level conversations with more intricate language usage and responses.

   
   **2. Your Companion**
   **Role-Based Scenarios:** Users can choose different roles to practice specific communication challenges, including:
   - **Group Discussions:** Practice collaborative communication in a group setting.
   - **Role Play:** Simulate specific roles in various scenarios to improve role-based communication.
   - **Case Studies:** Engage in case-based discussions to enhance critical thinking and presentation skills.
   - **Stress Management:** Practice communication in high-pressure scenarios to improve resilience and effective response under stress.

## Technologies Used
- Streamlit
- Python 3.10 or more
- Google Generative AI
- Langchain

## Installation:
  
1. **Clone the repository:**
   ``` bash
   git clone https://github.com/aashish1008/TalkTuner.git
   cd TalkTuner
2. **Install dependencies:**
   ``` bash
   pip install -r requirements.txt

3. **Set up environment variables:**
   - Obtain API keys for GOOGLE GEMINI PRO.
     ``` bash
     https://aistudio.google.com/app/apikey
   - Create a `.env` file in the root directory:
     ``` bash
     GOOGLE_API_KEY=your_google_genai_api_key
     
## Usage
1. Run the application:
   ``` bash
   streamlit run chatbot.py
   streamlit run your_companion.py
2. Open your web browser and navigate to http://localhost:8501.
3. Interact with TalkTuner by:
   ChatBot: Select your communication level (beginner, intermediate, or advanced) and start a conversation to improve your communication skills.
   Your Companion: Choose a role (group discussion, role play, case study, or stress management) and engage in structured conversations based on the selected scenario.

