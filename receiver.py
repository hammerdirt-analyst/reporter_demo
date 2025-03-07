# dataoperations


import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage, SystemMessage, BaseMessageChunk
)

from langchain_mongodb import MongoDBAtlasVectorSearch
from typing import Union
load_dotenv()

consumer = os.getenv("MONGO_DB_CONSUMER_URI")
admin = os.getenv("MONGO_DB_ADMIN_URI")

client = MongoClient(consumer)
collection = client["ragtest"]["textchunks"]
query_embedding = OpenAIEmbeddings(model="text-embedding-ada-002")
model_args_streaming = dict(name='openai', model="gpt-4o-mini", temperature=0.6, max_tokens=1000)
chat_llm = ChatOpenAI(**model_args_streaming)


def embed_query(query):
    embedded = query_embedding.embed_query(query)
    return query_embedding


def query_pipeline(aquery):

    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index_rag",  # Ensure this matches your MongoDB index
                "path": "embeddings",  # Ensure this matches the MongoDB field
                "queryVector": query_embedding.embed_query(aquery),
                "numCandidates": 100,
                "limit": 10,
                "similarity": "cosine"
            }
        }
    ]
    return pipeline

def query_mongodb(query):
    pipeline = query_pipeline(query)
    results = list(collection.aggregate(pipeline))
    text = [x['content'] for x in results]
    context = '\n\n'.join(text)

    return results, context

chat_llm = ChatOpenAI(**model_args_streaming)

def summarize_retrieved_docs_prompt(context, question):

    aprompt = (
        f"You have recieved the results of a vector similarity search to the following: {question}.",
        "Make a concise reporting of the contents of the results. Then compose an answer using your existing knowledge and the results.\n\n",
        )
    messages = [
        SystemMessage(content=' '.join(aprompt)),
        HumanMessage(content=context)
    ]
    return messages

# a_report_prompt = ChatPromptTemplate.from_messages(
#             [
#                 (
#                     'system',
#                     the_report_prompt
#                 ),MessagesPlaceholder(variable_name="messages")
#             ]
#         )
#
#         the_report_agent = a_report_prompt | chat_llm

def rag_response_prompt(question, context):
    prompt = (
        f"You have recieved the following question: {question}.",
        "Compose an answer using your existing knowledge and the results.\n\n",
        )
    messages = [
        SystemMessage(content=' '.join(prompt)),
        HumanMessage(content=context)
    ]
    return messages



def response_with_question(message):
    pass


def response_to_question(message: str = None) -> dict:

    rag_docs, context = query_mongodb(message)
    prompt = summarize_retrieved_docs_prompt(context, message)
    response = chat_llm.invoke(prompt)
    return response

def langchain_receiver(message: str) -> []:
    vectorstore = MongoDBAtlasVectorSearch.from_connection_string(
        connection_string=consumer,
        namespace = "ragtest.textchunks",
        embedding = query_embedding,
        index_name = "vector_index_rag",
        embedding_key = "embeddings",
        text_key = "content"
        )


    retriever = vectorstore.as_retriever(search_kwargs={"k": 5}, search_type='similarity')
    docs = retriever.invoke(message)
    # print(docs[0])
    content = [x.page_content for x in docs]
    context = '\n\n'.join(content)


    return docs, context