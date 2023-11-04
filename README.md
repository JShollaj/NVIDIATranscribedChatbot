# RAG Based LLM Chatbot for NVIDIA Videos

![Header](<Documentation/NVIDIA Channels.png>)

Guide showing how to build a chatbot which extracts the content of any video on YouTube (in this case all NVIDIA related channels), and add in the data as contextual on top of a Large Language Model.

---

## Issues With GPT4 + Bing (and Other LLM)

Currently the premium extension of ChatGPT (GPT4 + Bing Search extension) has issues with retrieving information on video content from YouTube or other similar platforms.

![Alt text](<Documentation/Chat GPT 4 Screenshot.png>)

While some of the videos, have corresponding documentation or news - less obscure ones cannot be accessed / or provide an accurate summary.

To save time to the user from wasting unecessary time, we have built a chat interface which automatically provides summary for available youtube videos (in this case from the NVIDIA channel).

---

## High Level Solution Overview and Description

In order to solve this issue, we will try to extract the transcript and text from all videos related to NVIDIA channels and then collide the files to a single text document for faster access to the LLM.

Then we will utilize LlamaIndex for a RAG based LLM with access to the retrieved files. After some preprocessing and testing, we review the answers and if they correspond to the extracted text.

After we are satisfied with the solution, we rewrite the code and extend streamlit as the front end chat interface for the user.

Finally, we deploy the application for wide use, while keeping in mind things we can change for different use cases or scaling the application.

---

## Deep Dive in Architecture

![Obtaining Data](<Documentation/Getting the Data.png>)

![RAG for LLAMA](Documentation/RAG.png)


---

## Other Considerations

- VectorDB Choice (Guide)

- LLM Choice

- Front End

- Deployment

- GPU Considerations

---

## List of Resources


https://community.aws/tutorials/fullstack-llm-langchain-chatbot-on-aws

https://www.mlexpert.io/prompt-engineering/chatbot-with-local-llm-using-langchain

https://www.youtube.com/watch?v=x5SYNpfK4H0

https://www.youtube.com/watch?v=o1BCq1KJULM

https://blog.epsilla.com/build-a-chatbot-that-runs-purely-on-your-local-machine-using-llama-2-epsilla-langchain-a5053b16f85

https://medium.com/predict/crafting-an-ai-powered-chatbot-for-finance-using-rag-langchain-and-streamlit-4384a8076960

https://www.reddit.com/r/LocalLLaMA/comments/17hs77a/how_to_build_chatbot_that_knows_your_companys/

https://python.langchain.com/docs/use_cases/question_answering/local_retrieval_qa

https://www.youtube.com/watch?v=J8TgKxomS2g&t=290s

https://youtube.com/playlist?list=PLVEEucA9MYhMkc4HvgHw-TvycgoMhADOI&si=hyd64IhalJnv8XJv