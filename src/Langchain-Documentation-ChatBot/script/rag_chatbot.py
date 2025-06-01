
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from gemini_llm import generate_answer





# Load vector store
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = FAISS.load_local("/home/alpha-lencho/Projects/Ready-Tensor/Langchain-Documentation-ChatBot/src/Langchain-Documentation-ChatBot/faiss_index", embedding_model, allow_dangerous_deserialization=True)

retriever = vector_store.as_retriever()

# Basic CLI RAG
print("💬 LangChain + Gemini RAG ChatBot (type 'exit' to quit)")
while True:
    query = input("\nAsk a question: ")
    if query.lower() in ['exit', 'quit']:
        break
    context_docs = retriever.get_relevant_documents(query)
    context = "\n\n".join([doc.page_content for doc in context_docs])
    full_prompt = f"""Use the context below to answer the question.

Context:
{context}

Question: {query}

Answer:"""
    answer = generate_answer(full_prompt)
    print("🤖", answer)
