from pypdf import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import os

# def main():
def ChatBot(querry):
    
    # st.set_page_config(page_title="Ask your PDF")
    # st.header("Ask Your PDF")
    # pdf = st.markdown()
    # pdf = st.file_uploader("Upload Your PDF", type="pdf")
    
    
    # if pdf is not None:
        
    pdf_reader = PdfReader("us_consti.pdf")
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        
        # st.write(text)
        # print(text)

         # split into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
        )
    chunks = text_splitter.split_text(text)
    # print(chunks)
      
        # create embeddings
    embeddings = OpenAIEmbeddings(openai_api_key = "open AI Key")
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    # print(knowledge_base)
        
    #     # show user input
    user_question = querry  #st.text_input("Ask a question about your PDF:")
    if user_question:
        docs = knowledge_base.similarity_search(user_question)
            
        llm = OpenAI(openai_api_key = "open Ai key")
        chain = load_qa_chain(llm, chain_type="stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=user_question)
            # print(cb)
            
        print(response)
    return response



# if __name__ == "__main__":
#     main()
