# 
import pandas as pd
import plotly.express as px
import streamlit as st

# Load your dataset
df = pd.read_csv("dataframe.csv")

# Display column names for debugging
st.write(df.columns)

# Sidebar filters
st.sidebar.header("Filter Options")

# Add filters for Locality
locality_filter = st.sidebar.multiselect(
    "Select Locality:",
    options=df["Locality"].unique(),
    default=df["Locality"].unique()
)

# Add filters for Cuisines
cuisine_filter = st.sidebar.multiselect(
    "Select Cuisines:",
    options=df["Cuisines"].unique(),
    default=df["Cuisines"].unique()
)

# Add filters for Ratings
rating_filter = st.sidebar.slider("Select Minimum Rating:", min_value=0.0, max_value=5.0, value=0.0, step=0.1)

# Handle Sponsored filter
if 'Sponsored' in df.columns:
    sponsored_filter = st.sidebar.selectbox("Select Sponsored:", options=["All"] + df["Sponsored"].unique().tolist())
    df_selection = df[
        (df["Locality"].isin(locality_filter)) &
        (df["Cuisines"].isin(cuisine_filter)) &
        (df["Ratings_out_of_5"] >= rating_filter) &
        (df["Sponsored"].isin([sponsored_filter] if sponsored_filter != "All" else df["Sponsored"].unique()))
    ]
else:
    st.warning("'Sponsored' column is not available in the dataset!")
    df_selection = df[
        (df["Locality"].isin(locality_filter)) &
        (df["Cuisines"].isin(cuisine_filter)) &
        (df["Ratings_out_of_5"] >= rating_filter)
    ]

# Display a warning if no data matches the filters
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop()

# Main content area
st.title(":bar_chart: Restaurant Explorer")

# Display filtered dataset
st.dataframe(df_selection)

# Add charts or visualizations based on the filtered data
# Example: Scatter plot using Plotly Express
fig_scatter = px.scatter(
    df_selection,
    x="Ratings_out_of_5",
    y="Cost",
    color="Cuisines",
    size="Number of votes",
    title="Restaurant Ratings vs Cost"
)
st.plotly_chart(fig_scatter, use_container_width=True)
