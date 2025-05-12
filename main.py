#from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_ollama.llms import OllamaLLM
from config import *
import logging
import json
global ollm
ollm = None

global embed_model
embed_model = None
def init_llm():
    global ollm
    global embed_model
    # llm = Ollama
    # embed_model = OpenAIEmbedding(model_name="text-embedding-3-large")
    ollm = OllamaLLM(model=f"{LLM_MODEL}",base_url=f"{OLLAMA_URL}")
    embed_model = OllamaEmbeddings(base_url=f"{OLLAMA_URL}",model=f"{EMBED_MODEL}")
     

def load_index():
    path = f"{FOLDER_PATH}"
    logging.info("*** Loading docs from %s",path)
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        logging.info("*** Loading %s",full_path)
        loader = PyPDFLoader(full_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator="\n")
        docs = text_splitter.split_documents(documents=documents)
        
       # Create vectors
        vectorstore = FAISS.from_documents(docs, embed_model)
        # Persist the vectors locally on disk
        vectorstore.save_local(f"{FAISS_INDEX_NAME}")

def query_pdf(query):
    # Load document using PyPDFLoader document loader
   
    # Load from local storage
    persisted_vectorstore = FAISS.load_local(f"{FAISS_INDEX_NAME}", embed_model,allow_dangerous_deserialization=True)
    
    qa = RetrievalQA.from_chain_type(llm=ollm, chain_type="stuff", retriever=persisted_vectorstore.as_retriever())
    result = qa.invoke(query)
    json_str = json.dumps(result, indent=4)
    print(json_str)


def main():
    init_llm()
    folder_path = f"{FOLDER_PATH}"
    #logging.info("Creating index from %s",folder_path)
    #load_index()
    query = input("Type in your query: \n")
    while query != "exit":
        query_pdf(query)
        query = input("Type in your query: \n")


if __name__ == "__main__":
    main()