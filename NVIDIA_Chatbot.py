import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader

openai.api_key = st.secrets.openai_key
st.header("Chat With NVIDIA Videos")

# Display the background image
st.image(
    "https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/logo-and-brand/01-nvidia-logo-horiz-500x200-2c50-p@2x.png",
    use_column_width=True
)


if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Ask me about NVIDIA Videos!"}]

@st.cache_resource(show_spinner=False)
def load_data():
    try:
        with st.spinner(text="Loading and indexing the documents – hang tight! This should take 1-2 minutes."):
            reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
            docs = reader.load_data()
            service_context = ServiceContext.from_defaults(
                llm=OpenAI(
                    model="gpt-3.5-turbo",
                    temperature=0.2,
                    system_prompt="Provide accurate and concise summary for requested videos and transcripts."
                )
            )
            index = VectorStoreIndex.from_documents(docs, service_context=service_context)
            return index
    except Exception as e:
        st.error(f"An error occurred: {e}")

index = load_data()
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=False)

if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message)
