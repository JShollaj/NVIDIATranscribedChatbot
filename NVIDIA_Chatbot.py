import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader

# Extract Keys
openai.api_key = st.secrets.openai_key

st.header("Extract Information From NVIDIA Videos")

# Display the background image
st.image(
    "https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/logo-and-brand/02-nvidia-logo-color-blk-500x200-4c25-p.png",
    use_column_width=True
)

green_text = "<span style='color:green;'>Summarize the following 'Accelerate AI-Powered Drug Discovery With NVIDIA BioNeMo'</span>"

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{
        "role": "assistant",
        "content": (
            "Hello there! Feel free to ask me questions about specific NVIDIA videos. "
            "Can start with the given: "
            + green_text
        )
    }]

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
        if green_text in message["content"]:
            st.markdown(message["content"].replace(green_text, f"<span style='color:green;'>{green_text}</span>"), unsafe_allow_html=True)
        else:
            st.write(message["content"])

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message)
