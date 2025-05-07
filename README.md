
# 🍺 BeerMatch: Filter-Based Beer Recommendation System

BeerMatch is a personalized beer recommendation app that helps users discover the best beers based on their taste preferences.  
Powered by real-world beer review data, it allows filtering by **aroma, bitterness, carbonation, body, ABV**, and even searching by **name or brand**.

---

## 🔍 Features

- 🎯 **Personalized Filtering**  
  Adjust sliders for:
  - Aroma (1–5)
  - Bitterness (1–5)
  - Carbonation (1–5)
  - Body (1–5)
  - ABV Range (e.g., 4.0% ~ 7.0%)

- 🔎 **Beer Search**  
  Search beers by name

- 🏷️ **Brand Filter**  
  View beers from specific breweries

- 📊 **Real Review Data**  
  Based on thousands of user reviews from open datasets

---

## 📁 Dataset Sources

- [Beer Reviews (Kaggle)](https://www.kaggle.com/datasets/rdoume/beerreviews)
- [Craft Cans Dataset (Kaggle)](https://www.kaggle.com/datasets/nickhould/craft-cans)

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/beer-match.git
   cd beer-match
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

> Make sure `final_beer_recommendation_dataset.csv` is in the same directory.

---

## 🌐 Demo

Coming soon on [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📜 License

MIT License.  
Data used for academic, personal, or non-commercial purposes only.
