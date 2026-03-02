# 🎬 Movie Recommender System

A content-based movie recommendation engine built with **Python**, **Streamlit**, and **Machine Learning**. This application suggests five similar movies based on a user's selection and fetches high-quality movie posters in real-time using the **TMDB API**.

---

## 🚀 Overview

The system utilizes a dataset of 5,000+ movies to find similarities between titles. By analyzing metadata such as genres, keywords, cast, and crew, the engine calculates a **Cosine Similarity** score to provide accurate recommendations.

### Key Features
* **Search Functionality:** Dropdown menu with auto-complete for thousands of movies.
* **Dynamic Poster Fetching:** Real-time API calls to The Movie Database (TMDB).
* **Optimized UI:** Grid-based layout with built-in caching for faster loading.
* **Error Handling:** Fallback placeholders for movies missing poster art.

---

## 🛠️ Technical Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Data Analysis:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
* **Machine Learning:** Scikit-Learn (CountVectorizer & Cosine Similarity)
* **API:** [TMDB API](https://www.themoviedb.org/documentation/api)
* **Serialization:** Pickle

---

## ⚙️ How It Works

1.  **Vectorization:** Text data (tags) is converted into numerical vectors using `CountVectorizer`.
2.  **Similarity Calculation:** We calculate the "distance" between movies using **Cosine Similarity**. 
3.  **The Formula:** $$similarity = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$
4.  **Recommendation:** When a movie is selected, the system identifies the top 5 movies with the highest similarity scores.

---

## 💻 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/movie-recommender.git](https://github.com/your-username/movie-recommender.git)
    cd movie-recommender
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **API Key Setup:**
    * Get an API Key from [The Movie Database (TMDB)](https://www.themoviedb.org/settings/api).
    * Replace the `api_key` variable in `app.py` with your 32-character key.

4.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

---

## 📂 Project Structure

```text
├── movies.pkl             # Pickled DataFrame containing movie titles and IDs
├── similarity.pkl         # Pre-computed similarity matrix
├── app.py                 # Main Streamlit application code
└── requirements.txt       # List of required Python libraries
