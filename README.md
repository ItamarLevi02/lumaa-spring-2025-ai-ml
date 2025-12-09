# Movie Recommender System using RAG

This project is a movie recommendation chatbot that leverages OpenAI embeddings, Pinecone vector search, and LangChain to provide movie recommendations based on user input. The chatbot processes a dataset of movies, transforms them into embeddings, which are stored in a vector database which allows for more acurate and fast retrevial then most traditional methods. Because of the fast retreival, I was able to use a dataset a bit bigger then the specified length or even bigger if wanted. I believe that this is a more forward thinking approach and one that looks to the future of machine learning, and that is why I decided to levereage a RAG system over a TF-IDF system

## 📂 Dataset

The project uses a _CSV file (imdb_movie_dataset.csv)_, which can also be found at: https://www.kaggle.com/datasets/yusufdelikkaya/imdb-movie-dataset. The features included in the dataset are:
- Title
- Genre
- Description
- Director
- Actors
- Year
- Rating
- Metascore

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

- PINECONE_API_KEY = ""
- PINECONE_API_ENV = ""
- OPENAI_API_KEY = ""

### 4. Run the final model

navigate into the model directory and run the Recommender_System.py file:

```bash
cd model
python3 Recommender_System.py

```

### 5. Querey Model

wait for model to prompt you and have fun!

## Example Output
You: I enjoy romantic novels

Bot: Based on your interest in romantic movies, here are five recommendations that you might enjoy:

1. "The Notebook" (2004) - Directed by Nick Cassavetes, this film is a classic romantic drama featuring Ryan Gosling and Rachel McAdams. It tells the story of a young couple who fall in love during the summer of 1940.

2. "Pride and Prejudice" (2005) - This adaptation of Jane Austen's classic novel is directed by Joe Wright and stars Keira Knightley and Matthew Macfadyen. It's a romantic drama set in the 18th century England.

3. "Before Sunrise" (1995) - Directed by Richard Linklater, this film is a romantic drama featuring Ethan Hawke and Julie Delpy. It tells the story of a young man and woman who meet on a train in Europe and wind up spending one evening together in Vienna.

4. "A Walk to Remember" (2002) - This romantic drama directed by Adam Shankman features Mandy Moore and Shane West. It's a touching story about a high school bad boy who falls in love with a minister's daughter.

5. "Eternal Sunshine of the Spotless Mind" (2004) - This romantic sci-fi film directed by Michel Gondry stars Jim Carrey and Kate Winslet. It's a unique love story about a couple who undergo a procedure to erase each other from their memories when their relationship turns sour.

## Salary Expectation:

$30/hr


