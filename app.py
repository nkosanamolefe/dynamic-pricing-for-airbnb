import streamlit as st
import pandas as pd
from utils import adjust_price

st.set_page_config(page_title="Cape Town Airbnb Pricing", layout="wide")

st.title("🏡 Dynamic Pricing for Airbnb – Cape Town")

# Load data
@st.cache_data
def load_data():
    listings = pd.read_csv("data/listings.csv.gz")
    calendar = pd.read_csv("data/calendar.csv.gz")
    return listings, calendar

listings, calendar = load_data()

# Sidebar filters
neighborhood = st.sidebar.selectbox("Select Neighborhood", listings["neighbourhood_cleansed"].unique())
room_type = st.sidebar.selectbox("Select Room Type", listings["room_type"].unique())

# Filtered data
filtered = listings[(listings["neighbourhood_cleansed"] == neighborhood) & (listings["room_type"] == room_type)]

st.subheader(f"Listings in {neighborhood} ({room_type})")
st.dataframe(filtered[["name", "price", "minimum_nights", "availability_365"]])

# Pricing simulation
st.subheader("📈 Price Adjustment Simulator")
base_price = st.number_input("Base Price (ZAR)", value=1200)
demand_mult = st.slider("Demand Multiplier", 0.5, 2.0, 1.2)
supply_mult = st.slider("Supply Multiplier", 0.5, 2.0, 0.85)

adjusted = adjust_price(base_price, demand_mult, supply_mult)
st.metric(label="Adjusted Price", value=f"R {adjusted:.2f}")
