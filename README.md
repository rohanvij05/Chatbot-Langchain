# Chatbot-Langchain
This project builds a custom chatbot using Langchain, FAISS, and Hugging Face embeddings. It extracts technical course data from a website, generates embeddings, stores them in FAISS, and exposes a Flask RESTful API. Users can send questions and receive relevant answers based on the course data.

# Custom Chatbot with Langchain

This project implements a custom chatbot that uses Langchain to extract technical course data, generate embeddings, and store them in a FAISS vector store. It exposes a Flask RESTful API to allow users to ask questions and get relevant answers based on the stored data.

## Project Structure

- **app.py**: Main Flask application handling API requests.
- **data_extraction.py**: Code to extract and process course data.
- **requirements.txt**: Lists the required Python libraries.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/custom-chatbot.git
    cd custom-chatbot
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:
    ```bash
    python app.py
    ```

4. The chatbot API will be available at `http://127.0.0.1:5000/`.

## How it Works

1. **Data Extraction**: Data is extracted from a given URL using Langchain's `WebBaseLoader`.
2. **Embeddings**: Embeddings are generated using Hugging Face's pre-trained model.
3. **Vector Store**: The data is stored in a FAISS vector store for fast retrieval.
4. **Chatbot API**: The Flask API allows users to send a question and receive an answer based on the vector store.

## Technologies Used

- Langchain
- FAISS
- Hugging Face Embeddings
- Flask

## Contribution

Feel free to fork and contribute to this project.

