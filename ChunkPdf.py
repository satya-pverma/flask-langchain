from pypdf import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from io import BytesIO
import boto3


# def main():
def ChunkPdf(docname):
    s3 = boto3.resource("s3",aws_access_key_id="your access key",aws_secret_access_key="your secret access")
    obj = s3.Object("bucket name", docname)
    fs = obj.get()["Body"].read()
    pdf_reader = PdfReader(BytesIO(fs))
        
    # pdf_reader = PdfReader("us_consti.pdf")
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
        )
    chunks = text_splitter.split_text(text)
    return chunks

