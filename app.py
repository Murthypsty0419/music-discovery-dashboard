import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Music Discovery Insights", layout="wide")

st.markdown("""
    <h1 style='text-align: center; color: #89CFF0;'>
        🎼 Music Discovery Database Insights Dashboard 
    </h1>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; font-size:18px; padding:10px;'>
        Music streaming platforms often reinforce mainstream artists through popularity-based algorithms, limiting the discovery of hidden musical talents. 
        This dashboard visualizes insights from a structured relational database designed to track listener engagement, playlist dynamics, and revenue trends across platforms.
        By analyzing real user interactions instead of algorithmic bias, we enable fairer, data-driven exploration of underrated songs and emerging artists.
    </div>
""", unsafe_allow_html=True)

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


st.write("") 
col1, spacer, col2 = st.columns([2, 0.5, 2])

with col1:
    st.subheader("**Total Streams per Platform (Top 10)**")
    top_platforms = streams_platform.sort_values(by='total_streams', ascending=False).head(10)
    fig1 = px.bar(top_platforms, x='total_streams', y='platform_name', orientation='h', color='platform_name', color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown("The chart shows that certain platforms dominate total stream counts, offering better audience reach opportunities for artists.")

with col2:
    st.subheader("**Revenue Share per Platform (Top 10)**")
    top_revenue = revenue_platform.sort_values(by='total_revenue', ascending=False).head(10)
    fig2 = px.sunburst(top_revenue, path=['platform_name'], values='total_revenue', color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("Revenue distribution varies slightly among top platforms, indicating some platforms are financially more rewarding per stream.")


st.write("")  
col3, col4, col5 = st.columns(3)

with col3:
    st.subheader("**Number of Listeners by Country**")
    fig3 = px.bar(listeners_country, x='listener_count', y='country', orientation='h', color='country', color_discrete_sequence=px.colors.qualitative.Bold)
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown("Listener distribution highlights countries where music streaming is most popular, helping plan regional marketing strategies.")

with col4:
    st.subheader("**Top 10 Genres Preferred by Listeners**")
    fig4 = px.pie(top_genres, names='preferred_genre', values='listener_count', hole=0.5, color_discrete_sequence=px.colors.sequential.Blues_r)
    st.plotly_chart(fig4, use_container_width=True)
    st.markdown("The top genres reflect audience music preferences, which artists and platforms can use for content curation.")

with col5:
    st.subheader("**Top 10 Artists by Total Revenue**")
    fig5 = px.bar(top_artists_revenue, x='artist_name', y='total_revenue', color='artist_name', color_discrete_sequence=px.colors.qualitative.Dark2)
    st.plotly_chart(fig5, use_container_width=True)
    st.markdown("A few top artists generate significant revenue, showcasing the importance of hit songs and loyal listener bases.")


st.write("") 
col6, spacer, col7 = st.columns([2, 0.5, 2])

with col6:
    st.subheader("**Songs Released Per Year**")
    fig6 = px.line(songs_year, x='year', y='songs_released', markers=True, color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig6, use_container_width=True)
    st.markdown("Song releases show a consistent trend with occasional peaks, highlighting active periods in the music industry.")

with col7:
    st.subheader("**Average Popularity Score per Genre (Top 10)**")
    top_popularity = popularity_genre.sort_values(by='avg_popularity', ascending=False).head(10)
    fig7 = px.scatter(top_popularity, x='avg_popularity', y='genre', size='avg_popularity', color='genre', color_discrete_sequence=px.colors.sequential.Plasma_r)
    st.plotly_chart(fig7, use_container_width=True)
    st.markdown("Some genres consistently maintain higher average popularity, reflecting stable listener loyalty.")


st.write("")  
col8, col9, col10 = st.columns(3)

with col8:
    st.subheader("**Top 10 Songs by Total Streams**")
    fig8 = px.line_polar(top_songs_streams, r='total_streams', theta='title', line_close=True, color_discrete_sequence=px.colors.sequential.Magenta)
    st.plotly_chart(fig8, use_container_width=True)
    st.markdown("Certain songs outperform others massively in total streams, reflecting viral trends or artist fanbase strength.")

with col9:
    st.subheader("**Average Revenue Per Stream by Platform (Top 10)**")
    top_avg_revenue = avg_revenue_platform.sort_values(by='avg_revenue_per_stream', ascending=False).head(10)
    fig9 = px.bar(top_avg_revenue, x='platform_name', y='avg_revenue_per_stream', color='platform_name', color_discrete_sequence=px.colors.qualitative.Prism)
    st.plotly_chart(fig9, use_container_width=True)
    st.markdown("Some platforms offer higher average payouts per stream, making them more attractive for monetization.")

with col10:
    st.subheader("**Top Artists by Total Streams (Top 10)**")
    top_artists_sorted = top_artists_streams.sort_values(by='total_streams', ascending=False).head(10)
    fig10 = px.bar(top_artists_sorted, x='total_streams', y='artist_name', orientation='h', color='artist_name', color_discrete_sequence=px.colors.sequential.YlOrRd)
    st.plotly_chart(fig10, use_container_width=True)
    st.markdown("Stream counts reveal the most in-demand artists, reflecting both popularity and marketing success.")
