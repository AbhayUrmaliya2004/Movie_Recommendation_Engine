# Movie Recommendation System

This project is a **Movie Recommendation System** designed to provide personalized movie suggestions to users. It leverages **content-based filtering** by calculating **cosine similarity** on movie genres and tags, ensuring recommendations are relevant and aligned with user preferences.

---

## Features
- **Content-Based Filtering**: Recommends movies by analyzing genres and tags.
- **Efficient Matching**: Uses cosine similarity to identify the most relevant movies.
- **Streamlit Interface**: Provides an interactive and user-friendly experience for exploring recommendations.

---

## How to Run
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the application using Streamlit:
   ```bash
   streamlit run app.py
   ```

3. Access the application in your browser at `http://localhost:8501`.

---

## Tech Stack
- **Programming Language**: Python
- **Data Processing**: Pandas (for data cleaning and processing)
- **Natural Language Processing**: NLTK 

---

## Future Improvements
1. **Fine-Tuned Model Integration**:
   - Develop a fine-tuned model to create tags and embeddings based on user queries and movie descriptions.
   - Expand filtering capabilities to include movie summaries and descriptions, allowing for more nuanced recommendations.

2. **Enhanced Query Handling**:
   - Support for broader search options based on keywords and themes.

---

Feel free to contribute and enhance the system further!

