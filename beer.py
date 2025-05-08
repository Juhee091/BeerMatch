import streamlit as st
import pandas as pd

# Load CSV
df = pd.read_csv("final_beer_recommendation_dataset.csv")

st.set_page_config(page_title="BeerMatch: Beer Recommendation System")
st.title("🍺 BeerMatch: Filter-Based Beer Recommendation")

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Settings")
aroma = st.sidebar.slider("Aroma", 1.0, 5.0, 3.0, step=0.1)
bitterness = st.sidebar.slider("Bitterness", 1.0, 5.0, 3.0, step=0.1)
carbonation = st.sidebar.slider("Carbonation", 1.0, 5.0, 3.0, step=0.1)
body = st.sidebar.slider("Body", 1.0, 5.0, 3.0, step=0.1)
abv_range = st.sidebar.slider("ABV Range", 0.0, 15.0, (4.0, 7.0), step=0.1)

# Search and Brand Filter
search_query = st.text_input("Search Beer Name")
brands = ["All"] + sorted(df["Brand"].dropna().unique().tolist())
selected_brand = st.selectbox("Select Brand", brands)

# --- Apply Filters ---
if search_query:
    # If search is used, ignore filters and search across all data
    filtered = df[df["Name"].str.contains(search_query, case=False, na=False)]
else:
    # Otherwise, apply all filters
    filtered = df.copy()
    filtered = filtered[(filtered["Aroma"] >= aroma - 0.5) & (filtered["Aroma"] <= aroma + 0.5)]
    filtered = filtered[(filtered["Bitterness"] >= bitterness - 0.5) & (filtered["Bitterness"] <= bitterness + 0.5)]
    filtered = filtered[(filtered["Carbonation"] >= carbonation - 0.5) & (filtered["Carbonation"] <= carbonation + 0.5)]
    filtered = filtered[(filtered["Body"] >= body - 0.5) & (filtered["Body"] <= body + 0.5)]
    filtered = filtered[(filtered["ABV"] >= abv_range[0]) & (filtered["ABV"] <= abv_range[1])]

# Brand filter applies regardless
if selected_brand != "All":
    filtered = filtered[filtered["Brand"] == selected_brand]

# --- Display Results ---
st.markdown(f"#### Recommendations: {len(filtered)} result(s)")

for _, row in filtered.head(50).iterrows():
    st.markdown(f"**{row['Name']}** - *{row['Style']}*  ")
    st.markdown(f"ABV: {row['ABV']}% | Aroma: {row['Aroma']} | Bitterness: {row['Bitterness']} | Carbonation: {row['Carbonation']} | Body: {row['Body']}")
    st.markdown(f"Brand: {row['Brand']}")
    st.markdown(f"_{row['Description']}_")
    st.markdown("---")
