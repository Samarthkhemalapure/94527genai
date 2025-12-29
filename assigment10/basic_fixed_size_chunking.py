from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)

with open("dummy_data.txt", 'r') as file:
    raw_text = file.read()
 

docs = text_splitter.create_documents([raw_text])
i = 1
for doc in docs:
    print(f" chunk_{i}--->> {doc.page_content}")
    i=i+1
    print("\n\n")