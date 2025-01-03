import os
from flask import Flask, render_template, request, jsonify
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer

app = Flask(__name__)

model_name = "deepset/roberta-base-squad2" 
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

def load_and_combine_documents():
    url = "https://brainlox.com/courses/category/technical"
    loader = WebBaseLoader(url)
    documents = loader.load()
    combined_text = "\n\n".join([doc.page_content for doc in documents])
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(documents, embedding_model)
    vector_store.save_local("faiss_db")
    return combined_text, vector_store

combined_text, vector_store = load_and_combine_documents()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    
    answer = qa_pipeline(question=question, context=combined_text)['answer']
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
