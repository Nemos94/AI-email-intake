from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


import os

KNOWLEDGE_PATH = "knowledge"
VECTORSTORE_PATH = "vectorstore"

documents = []

for file in os.listdir(KNOWLEDGE_PATH):
    if file.endswith(".md") or file.endswith(".txt"):
        loader = TextLoader(os.path.join(KNOWLEDGE_PATH, file))
        documents.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

db = Chroma.from_documents(
    chunks,
    OpenAIEmbeddings(),
    persist_directory=VECTORSTORE_PATH
)

db.persist()

print("✅ Vector store criado com sucesso")
