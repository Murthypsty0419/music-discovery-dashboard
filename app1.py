import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Music Discovery Insights", layout="wide")

# Title
st.title("🎵 Music Discovery Database Insights")

# Load all CSVs
streams_platform = pd.read_csv('total_streams_per_platform.csv')
revenue_platform = pd.read_csv('revenue_per_platform.csv')
listeners_country = pd.read_csv('listeners_per_country.csv')
top_genres = pd.read_csv('top_genres_listeners.csv')
top_artists_revenue = pd.read_csv('top_artists_revenue.csv')
songs_year = pd.read_csv('songs_released_per_year.csv')
popularity_genre = pd.read_csv('avg_popularity_per_genre.csv')
top_songs_streams = pd.read_csv('top_songs_by_streams.csv')
avg_revenue_platform = pd.read_csv('avg_revenue_per_stream_by_platform.csv')
top_artists_streams = pd.read_csv('top_artists_by_streams.csv')

# ----------- Plot 1: Bar Chart
st.header("1. Total Streams per Platform")
fig1 = px.bar(streams_platform, x='platform_name', y='total_streams', color='platform_name', title="Streams Distribution by Platform")
st.plotly_chart(fig1, use_container_width=True)

# ----------- Plot 2: Pie Chart
st.header("2. Revenue Share per Platform")
fig2 = px.pie(revenue_platform, names='platform_name', values='total_revenue', title="Revenue Distribution Across Platforms")
st.plotly_chart(fig2, use_container_width=True)

# ----------- Plot 3: Horizontal Bar Chart
st.header("3. Number of Listeners by Country")
fig3 = px.bar(listeners_country, x='listener_count', y='country', orientation='h', title="Listeners Count by Country")
st.plotly_chart(fig3, use_container_width=True)

# ----------- Plot 4: Donut Chart
st.header("4. Top 10 Genres Preferred by Listeners")
fig4 = px.pie(top_genres, names='preferred_genre', values='listener_count', hole=0.5, title="Top Genres")
st.plotly_chart(fig4, use_container_width=True)

# ----------- Plot 5: Bar Chart
st.header("5. Top 10 Artists by Total Revenue")
fig5 = px.bar(top_artists_revenue, x='artist_name', y='total_revenue', color='artist_name', title="Top Artists by Revenue")
st.plotly_chart(fig5, use_container_width=True)

# ----------- Plot 6: Line Chart
st.header("6. Songs Released Per Year")
fig6 = px.line(songs_year, x='year', y='songs_released', markers=True, title="Songs Released Trend Over Years")
st.plotly_chart(fig6, use_container_width=True)

# ----------- Plot 7: Scatter Plot
st.header("7. Average Popularity Score per Genre")
fig7 = px.scatter(popularity_genre, x='genre', y='avg_popularity', size='avg_popularity', color='genre', title="Average Popularity by Genre")
st.plotly_chart(fig7, use_container_width=True)

# ----------- Plot 8: Polar Area Chart
st.header("8. Top 10 Songs by Total Streams")
fig8 = px.line_polar(top_songs_streams, r='total_streams', theta='title', line_close=True, title="Top Songs by Streams")
st.plotly_chart(fig8, use_container_width=True)

# ----------- Plot 9: Bar Chart
st.header("9. Average Revenue Per Stream by Platform")
fig9 = px.bar(avg_revenue_platform, x='platform_name', y='avg_revenue_per_stream', color='platform_name', title="Avg Revenue Per Stream (Higher is Better)")
st.plotly_chart(fig9, use_container_width=True)

# ----------- Plot 10: Treemap
st.header("10. Top Artists by Total Streams")
fig10 = px.treemap(top_artists_streams, path=['artist_name'], values='total_streams', title="Top Artists based on Streams")
st.plotly_chart(fig10, use_container_width=True)