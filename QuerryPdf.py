from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback



# def main():
def QuerryPdf(querry, chunks):      
        # create embeddings
    embeddings = OpenAIEmbeddings(openai_api_key = "open AI key")
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    print(knowledge_base)
        
        # show user input
    user_question = querry  #st.text_input("Ask a question about your PDF:")
    if user_question:
        docs = knowledge_base.similarity_search(user_question)
            
        llm = OpenAI(openai_api_key = "open AI key")
        chain = load_qa_chain(llm, chain_type="stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=user_question)
            # print(cb)
            
    #     print(response)
    return response




