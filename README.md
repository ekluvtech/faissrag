# faissrag
RAG pipeline - using langchain, ollama and FAISS

## Create python env using following command and activate
  ``python3 -m venv faissenv``

  ``.\faissenv\Scripts\activate``
  
## Run the following command to install dependencies
  ``pip instsall -r .\requirements.txt``

## Make sure to setup ollama locally, please follow the below blog to setup, Please skip the Qdrant setup as we are using faiss vector db.
  https://ekluvtech.com/2025/04/10/setup-ollama-and-qdrant/
  
## Replace the config parameters in config.py
  
## Once the setu is ready run the following command to run the main program. It will load the documents already placed in the project under data folder. once the embeddings are loaded into faiss db, it will create the index locally. And then it will ask for query input for question. 
  ``python3 main.py``


![Output](https://github.com/user-attachments/assets/742f5198-0d24-4d14-a103-0df24b043e30)
