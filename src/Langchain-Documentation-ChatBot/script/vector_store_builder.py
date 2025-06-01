from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

# 1. Load text chunks
with open("/home/alpha-lencho/Projects/Ready-Tensor/Langchain-Documentation-ChatBot/src/Langchain-Documentation-ChatBot/data/langchain_chunks.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# 2. Split the chunks 
chunks = [chunk.strip() for chunk in raw_text.split("\n\n") if chunk.strip()]

# 3. Wrap chunks in LangChain Document objects
documents = [Document(page_content=chunk) for chunk in chunks]

# 4. Initialize the embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 5. Create FAISS vector store
db = FAISS.from_documents(documents, embedding_model)

# 6. Save the vector store
db.save_local("/home/alpha-lencho/Projects/Ready-Tensor/Langchain-Documentation-ChatBot/src/Langchain-Documentation-ChatBot/faiss_index")