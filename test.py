from dotenv import load_dotenv
from pypdf import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from io import BytesIO
import os
import boto3


# def main():
def main():

    
    # load_dotenv(os.getenv("OPENAI_API_KEY"))
   
    s3 = boto3.resource("s3",aws_access_key_id="",aws_secret_access_key="")
    obj = s3.Object("", "us_consti.pdf")
    fs = obj.get()["Body"].read()
    pdf_reader = PdfReader(BytesIO(fs))
        
    # pdf_reader = PdfReader("us_consti.pdf")
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        
        # st.write(text)
        print(text)

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
    embeddings = OpenAIEmbeddings(openai_api_key = "")
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    # print(knowledge_base)
        
    #     # show user input
    user_question = "why was nato created?"  #st.text_input("Ask a question about your PDF:")
    if user_question:
        docs = knowledge_base.similarity_search(user_question)
            
        llm = OpenAI(openai_api_key = "")
        chain = load_qa_chain(llm, chain_type="stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=user_question)
            # print(cb)
            
        print(response)
    return response



if __name__ == "__main__":
    main()
