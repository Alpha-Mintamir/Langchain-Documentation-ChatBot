import requests
from bs4 import BeautifulSoup

# List of LangChain documentation URLs
urls = [
    'https://python.langchain.com/docs/introduction/',
    'https://python.langchain.com/docs/how_to/',
    'https://python.langchain.com/docs/how_to/installation/',
    'https://python.langchain.com/docs/how_to/pydantic_compatibility/',
    'https://python.langchain.com/docs/how_to/structured_output/',
    'https://python.langchain.com/docs/how_to/tool_calling/',
    'https://python.langchain.com/docs/how_to/streaming/',
    'https://python.langchain.com/docs/how_to/debugging/',
]

# Final text content
all_text = ""

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract text from paragraphs
    paragraphs = soup.find_all('p')
    page_text = '\n'.join([para.get_text() for para in paragraphs])

    # Add a header to separate each page
    all_text += f"\n\n=== Content from: {url} ===\n\n{page_text}"

# Save everything to one file
output_path = '/home/alpha-lencho/Projects/Ready-Tensor/Langchain-Documentation/src/LangchainDocumentation/data/langchain_docs.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(all_text)

print(f"documentation saved to: {output_path}")
