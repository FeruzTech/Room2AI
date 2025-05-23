# RAG and LLM integration service
from vectorstore import ingest_urls_to_chromadb  # Import vectorstore logic
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import MessagesPlaceholder
import os
from dotenv import load_dotenv

def summarize_with_rag(age_group: str, prompt: str) -> str:
    load_dotenv()
    """
    Summarize the prompt for the given age group using RAG and LLM.
    """
    # Load Chroma vector store
    persist_directory = os.getenv("CHROMA_DB_DIR", "./chroma_db")
    embeddings = FastEmbedEmbeddings()
    vectorstore = Chroma(
        embedding_function=embeddings,
        persist_directory=persist_directory
    )
    # Retrieve relevant documents
    retriever = vectorstore.as_retriever()
    relevant_docs = retriever.get_relevant_documents(prompt)
    print(f"Relevant documents: {relevant_docs} (type: {type(relevant_docs)})")
    if not relevant_docs:
        raise ValueError("No relevant documents found for the given prompt.")
    # Prepare prompt template for LLM
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a kind and knowledgeable teacher chatbot designed to help children learn.
         Your job is to provide safe, clear, and age-appropriate explanations.NEVER make up answers. You MUST ONLY use the information provided in the <Context> section.If the answer is not directly found in the context, say:I'm not sure about that based on what I have here.Always respond kindly, simply, 
         and concisely.CONTEXT:{context}"""),
        ("human", """The student is {age_group} years old.They asked this question:{input}""")
    ])

    # Load OpenAI API key from environment
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set.")
    model = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=openai_api_key
    )

    document_chain = create_stuff_documents_chain(
        model,
        chat_prompt
    )

    chain = create_retrieval_chain(retriever, document_chain)
    # Run the chain
    result = chain.invoke({
        #"context": "\n\n".join([doc.page_content for doc in relevant_docs]),
        "input": prompt,
        "age_group": age_group
    })
    print(f"chain.invoke result: {result} (type: {type(result)})")
    if isinstance(result, dict) and "output" in result:
        return result["output"]
    elif isinstance(result, str):
        return result
    else:
        raise ValueError(f"Unexpected result from chain.invoke: {result}")
