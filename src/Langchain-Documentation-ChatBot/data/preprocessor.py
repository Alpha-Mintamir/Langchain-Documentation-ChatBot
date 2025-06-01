from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load your scraped text
with open('/home/alpha-lencho/Projects/Ready-Tensor/Langchain-Documentation-ChatBot/src/Langchain-Documentation-ChatBot/data/langchain_docs.txt', 'r', encoding='utf-8') as f:
    raw_text = f.read()

# Step 1: Clean the raw text (basic cleaning)
cleaned_text = raw_text.replace('\n', ' ').strip()

# Step 2: Split the cleaned text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,     # number of characters per chunk
    chunk_overlap=100,   # overlap between chunks
    separators=["\n\n", "\n", ".", " ", ""]
)

chunks = text_splitter.split_text(cleaned_text)

#  Save the chunks for inspection
output_path = '/home/alpha-lencho/Projects/Ready-Tensor/Langchain-Documentation-ChatBot/src/Langchain-Documentation-ChatBot/data/langchain_chunks.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    for i, chunk in enumerate(chunks):
        f.write(f"--- Chunk {i+1} ---\n{chunk}\n\n")

print(f"✅ Preprocessing complete. {len(chunks)} chunks saved to: {output_path}")
