# AI Chatbot with Pinecone & OpenAI

This project is a movie recommendation chatbot that leverages OpenAI embeddings, Pinecone vector search, and LangChain to provide movie recommendations based on user input. The chatbot processes a dataset of movies, transforms them into embeddings, which are stored in a vector database which allows for more acurate and fast retrevial then most traditional methods. I believe that this is a more forward thinking approach and one that looks to the future of machine learning, and that is why I decided to levereage a RAG system over a TF-IDF system

## 📂 Dataset

The project uses a _CSV file (imdb_movie_dataset.csv)_, which can also be found at: https://www.kaggle.com/datasets/yusufdelikkaya/imdb-movie-dataset. The features included in the dataset are:
-Title
-Genre
-Description
-Director
-Actors
-Year
-Rating
-Metascore

## 🛠️ Installation

### 1. Create and Activate Virtual Environment

```bash
python3 -m venv lumaa
source lumaa/bin/activate  # macOS/Linux
lumaa\Scripts\activate    # Windows
```

### 2. Install Dependencies Activate the Virtual Environment

```bash
pip install -r requirements.txt
```

### 3. Set up Environment Variables

(I have attached MY API keys that way the project is easy for you guys to run, but you will need to create a .env file at the root directory and add) :

-PINECONE_API_KEY = "pcsk_5jRVqy_KMSsgNvdoujgzDxFbHULRx6JiMScHN9t95KswjU7g7qdfdWmpeUa4S8E4sfsHn5"
-PINECONE_API_ENV = "us-east-1-aws"
-OPENAI_API_KEY = "sk-proj-YuRrwLegwEDAQSAZWNNTFYPnP4ll07VOTYWJRPNXBmSH69aXNP-08Pnu5ByUOzS5H3EbVkQp5qT3BlbkFJjvxU0jtYQvCGt_ptpxqC-\_AWD8yHu8bD2QdmP76aBMjJyTI0OGYt8a6Z0u16pGuGB6FxAtTpYA"

### 4. Run the final model

navigate into the model directory and run the Recommender_System.py file:

```bash
cd model
python3 Recommender_System.py

```

### 5. Querey Model

wait for model to prompt you and have fun!

## Salary Expectation:

$30/hr
