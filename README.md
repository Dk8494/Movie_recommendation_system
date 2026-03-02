# 🎬 Movie Recommender System

A content-based movie recommendation engine built with **Python**, **Streamlit**, and **Machine Learning**. This application suggests five similar movies based on a user's selection and fetches high-quality movie posters in real-time using the **TMDB API**.

---

## 🚀 Overview

The system utilizes the TMDB 5000 dataset to find similarities between titles. By analyzing metadata such as genres, keywords, and plot overviews, the engine calculates a **Cosine Similarity** score to provide accurate recommendations.

### Key Features
* **Search Functionality:** Dropdown menu with auto-complete for thousands of movies.
* **Dynamic Poster Fetching:** Real-time API calls to The Movie Database (TMDB).
* **Optimized UI:** Grid-based layout with built-in caching for faster loading.
* **Error Handling:** Fallback placeholders for movies missing poster art.

---

## 📊 Dataset Information

This project uses the **TMDB 5000 Movie Dataset** sourced from Kaggle.
* **Dataset Link:** [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* **Description:** The dataset contains information on 4,803 movies, including budget, genres, keywords, cast, and crew.
* **Files Used:** * `tmdb_5000_movies.csv`: Primary movie metadata.
  * `tmdb_5000_credits.csv`: Cast and crew information.

---

## 🛠️ Technical Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Data Analysis:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
* **Machine Learning:** Scikit-Learn (CountVectorizer & Cosine Similarity)
* **API:** [TMDB API](https://www.themoviedb.org/documentation/api)
* **Serialization:** Pickle

---

## ⚙️ How It Works

1.  **Vectorization:** Text data (tags) is converted into numerical vectors using `CountVectorizer` (Bag of Words).
2.  **Similarity Calculation:** We calculate the "distance" between movies using **Cosine Similarity**. The closer the vectors, the more similar the movies.
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

## ⚠️ Troubleshooting: Poster Loading Issues
If posters are not loading, ensure:
1.  **API Key:** Your TMDB API key is active and correctly pasted in the `fetch_poster` function.
2.  **Internet Connection:** High-latency connections may cause timeouts.
3.  **ID Mapping:** Ensure `movies.pkl` contains the correct `movie_id` column as used by TMDB.

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgements
* Dataset provided by [TMDb](https://www.themoviedb.org/).
* Inspired by the data science community on Kaggle.
