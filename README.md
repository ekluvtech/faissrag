# faissrag
![faiss2](https://github.com/user-attachments/assets/49eeb5ec-47a4-439d-ba55-285b4d6cdb15)


#### 1.Create python env using following command and activate
  ``python3 -m venv faissenv``

  ``.\faissenv\Scripts\activate``
  
#### 2.Install dependencies by running the following command
  ``pip instsall -r .\requirements.txt``

#### 3.Before proceeding, please ensure you have Ollama set up locally. For setup instructions, refer to the blog post below, skipping the Qdrant setup section as we will be using Faiss vector DB instead.
  https://ekluvtech.com/2025/04/10/setup-ollama-and-qdrant/
  
#### 4.Update the configuration parameters in config.py with your own values
  
#### 5.Once the setup is ready, run the following command to start the program, which will automatically load documents from the data folder, load embeddings into the Faiss database, create a local index, and then prompt you to enter a query, enabling you to ask questions and interact with the LLM.
  ``python3 main.py``

![Output](https://github.com/user-attachments/assets/1197cd4e-19d7-447e-9fd1-0b49ad1695ac)

For more details, Please visit https://ekluvtech.com/2025/04/26/what-is-faiss-and-its-uses/
