from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.documents import Document

# Example usage (uncomment and implement document loading if needed):

# documents = [WebBaseLoader(url).load()[0].page_content for url in urls]
# ingest_documents_chromadb(documents)



# def ingest_documents_chromadb(urls: list[str], persist_directory: str = "./chroma_db"):
#     """
#     Ingests a list of documents into a ChromaDB vector store using default embeddings.
#     Splits documents into chunks of size 1024 with overlap 100.
#     Args:
#         documents (list[str]): List of document texts to ingest.
#         persist_directory (str): Directory to persist the ChromaDB database.
#     Returns:
#         Chroma: The Chroma vector store instance.
#     """
#     print ("Ingesting documents into ChromaDB...", urls)
#     # Load documents into LangChain Document objects
#     docs = [Document(page_content=doc) for doc in urls]

#     # Split documents
#     splitter = CharacterTextSplitter(chunk_size=1024, chunk_overlap=100)
#     split_docs = splitter.split_documents(docs)

#     # Use default embedding (FastEmbedEmbeddings)
#     embeddings = FastEmbedEmbeddings()

#     # Create or load Chroma vector store
#     vectorstore = Chroma.from_documents(
#         split_docs,
#         embedding=embeddings,
#         persist_directory=persist_directory
#     )
#     vectorstore.persist()
#     return vectorstore



def ingest_urls_to_chromadb(urls: list[str], persist_directory: str = "./chroma_db"):
    """
    Loads web pages from the given URLs, splits them into chunks, and ingests them into ChromaDB.
    Args:
        urls (list[str]): List of URLs to ingest.
        persist_directory (str): Directory to persist the ChromaDB database.
    Returns:
        Chroma: The Chroma vector store instance.
    """
    
    # Load documents from URLs
    docs = []
    for url in urls:
        try:
            loaded = WebBaseLoader(url).load()
            docs.extend(loaded)
        except Exception as e:
            print(f"Failed to load {url}: {e}")
    if not docs:
        raise ValueError("No documents loaded from URLs.")

    # Split documents
    splitter = CharacterTextSplitter(chunk_size=1024, chunk_overlap=100)
    split_docs = splitter.split_documents(docs)

    # Use default embedding (FastEmbedEmbeddings)
    embeddings = FastEmbedEmbeddings()

    # Create or load Chroma vector store
    vectorstore = Chroma.from_documents(
        split_docs,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    vectorstore.persist()
    return vectorstore

# # Example usage:
# if __name__ == "__main__":
#     urls = [
#         "https://www.nationalgeographic.com/latest-stories",
#         "https://www.smithsonianmag.com/smart-news/",
#         "https://www.bbc.com/news/science_and_environment",
#         "https://www.nasa.gov/news/all-news/",
#         "https://blog.khanacademy.org/",
#         "https://www.history.com/this-day-in-history",
#         "https://www.cdc.gov/media/index.html",
#         "https://www.nih.gov/news-events/news-releases",
#         "https://www.scientificamerican.com/section/news/",
#         "https://www.unicef.org/press-releases"
#     ]


