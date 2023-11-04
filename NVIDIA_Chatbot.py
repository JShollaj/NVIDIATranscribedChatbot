import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader

# Constants
DATA_DIR = "./data"
MODEL_NAME = "gpt-3.5-turbo"
TEMPERATURE = 0.5
SYSTEM_PROMPT = ("You are a smart assistant providing insights on transcript from NVIDIA videos provided and help with details requested.")

# Functions
@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the Streamlit docs – hang tight! This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir=DATA_DIR, recursive=True)
        docs = reader.load_data()
        
        # Define chunk size for chunking data
        chunk_size = 1000  # Adjust this value based on your data and requirements
        
        # Update the service context to include the chunk_size
        service_context = ServiceContext.from_defaults(
            llm=OpenAI(model=MODEL_NAME, temperature=TEMPERATURE, system_prompt=SYSTEM_PROMPT),
            chunk_size=chunk_size  # Include chunk_size here
        )
        
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

def init_chat_history():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Ask me a question about NVIDIA videos!"}
        ]

def process_user_input(chat_engine):
    if prompt := st.chat_input("Your question"):  # Prompt for user input and save to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state.messages:  # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # If last message is not from assistant, generate a new response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chat_engine.chat(prompt)
                st.write(response.response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(message)  # Add response to message history

def main():
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://futurumgroup.com/wp-content/uploads/2019/12/NVIDIA-Is-Poised-to-Dominate-the-AI-Inferencing-Chipset-Market-through-2021.jpg");
    background-size: cover;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    openai.api_key = st.secrets.openai_key
    init_chat_history()
    index = load_data()
    chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=False)
    process_user_input(chat_engine)

if __name__ == "__main__":
    main()
