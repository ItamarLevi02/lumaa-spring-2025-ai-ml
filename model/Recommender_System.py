import pandas as pd
import os
from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceEmbeddings
from pinecone import Pinecone as PineconeClient
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Pinecone as PineconeLang
from langchain.prompts import PromptTemplate
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI


#loading api keys
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#initalize embedding
embeddings = OpenAIEmbeddings(model='text-embedding-3-small')

#Connects to Vector DB
pc = PineconeClient(api_key=PINECONE_API_KEY)
docsearch = PineconeLang.from_existing_index(index_name="lumaa", embedding=embeddings)


prompt_template="""

You are an expert movie recommender who can understand what the person is asking and what kind of movies they like based on the given information that they give you.
Context: {context}
Question: {question}

Return the helpful answer that gives them 5 total recommendations that they should look at. 
Helpful answer:
"""

# Binds our prompt to this varaible "PROMPT that will be fed to the llm later"
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs = {"question_prompt": PROMPT}

# Setting the memory buffer
memory = ConversationBufferMemory(
    memory_key="chat_history",  # This key is used in the prompt template for conversation history.
    return_messages=True         # Returns the chat history as a list of messages.
)

# This chain binds together both our llm and the vector database we made 
qa = ConversationalRetrievalChain.from_llm(
    llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=OPENAI_API_KEY),
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    memory=memory,
    combine_docs_chain_kwargs={"prompt": PROMPT},
)


#Conversational Chain that highlights the use of the Memmory that the system holds

while True:
    query = input("Explain what type of movie you want: ")  # Get user input

    if query.lower() in ["exit", "quit", "stop"]:  # Allow user to exit
        print("Goodbye!")
        break

    response = qa.run(query)  # Get response from the chatbot
    print("Bot:", response)
