import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smartphone Recommender", layout="wide")

st.title("📱 Smartphone Analysis & Recommendation System")

# Load dataset
df = pd.read_csv("data.csv")

# Sidebar filters
st.sidebar.header("🔍 Filter Options")

brand = st.sidebar.multiselect("Select Brand", df["Brand"].unique())
max_price = st.sidebar.slider("Select Max Budget", 10000, 100000, 30000)
min_ram = st.sidebar.slider("Minimum RAM (GB)", 2, 16, 6)

filtered_df = df[df["Price"] <= max_price]
filtered_df = filtered_df[filtered_df["RAM"] >= min_ram]

if brand:
    filtered_df = filtered_df[filtered_df["Brand"].isin(brand)]

# Show data
st.subheader("📊 Filtered Smartphones")
st.dataframe(filtered_df)

# Top recommendations
st.subheader("🏆 Top Recommended Phones")
top = filtered_df.sort_values(by="Rating", ascending=False).head(5)
st.table(top)

# Graphs
st.subheader("📈 Price vs Rating")

fig, ax = plt.subplots()
ax.scatter(df["Price"], df["Rating"])
ax.set_xlabel("Price")
ax.set_ylabel("Rating")
st.pyplot(fig)

# Battery comparison
st.subheader("🔋 Battery Comparison")

fig2, ax2 = plt.subplots()
ax2.bar(df["Model"], df["Battery"])
plt.xticks(rotation=45)
st.pyplot(fig2)

# Smart recommendation
st.subheader("🤖 Smart Recommendation")

choice = st.selectbox("What do you prioritize?", ["Camera", "Battery", "Performance"])

if st.button("Recommend Best Phone"):
    if choice == "Camera":
        best = df.sort_values(by="Camera", ascending=False).head(1)
    elif choice == "Battery":
        best = df.sort_values(by="Battery", ascending=False).head(1)
    else:
        best = df.sort_values(by="RAM", ascending=False).head(1)

    st.success("Best Phone for You:")
    st.table(best)