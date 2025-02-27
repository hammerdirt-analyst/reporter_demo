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
from typing import Union

admin = os.getenv("MONGO_DB_CONSUMER_URI")

client = MongoClient(admin)
collection = client["ragtest"]["textchunks"]
query_embedding = OpenAIEmbeddings(model="text-embedding-ada-002")



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

def query_mongodb(pipeline):
    results = list(collection.aggregate(pipeline))
    return results