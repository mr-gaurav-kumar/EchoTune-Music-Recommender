import streamlit as st
import joblib
import random

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="EchoTune - Music Recommender",
    page_icon="🎵",
    layout="wide"
)

# --------------------------------
# LOAD DATA
# --------------------------------

df = joblib.load("models/music_df.pkl")
similarity = joblib.load("models/similarity.pkl")

# CHANGE COLUMN NAME IF NEEDED
SONG_COLUMN = "song"

# --------------------------------
# CUSTOM CSS
# --------------------------------

st.markdown("""
<style>

body {
    background-color: #050816;
}

.main {
    background: linear-gradient(to bottom right, #050816, #0a0f2c);
    color: white;
}

h1, h2, h3 {
    color: white;
}

.stApp {
    background: linear-gradient(to bottom right, #050816, #0d102d);
}

section[data-testid="stSidebar"] {
    background-color: #0b1023;
    border-right: 1px solid #20263d;
}

.song-card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    transition: 0.3s;
    margin-bottom: 20px;
}

.song-card:hover {
    transform: scale(1.03);
    border: 1px solid #9b5cff;
    box-shadow: 0px 0px 20px rgba(155,92,255,0.5);
}

.song-title {
    font-size: 20px;
    font-weight: bold;
    color: white;
}

.song-sub {
    color: #b3b3b3;
    margin-top: 10px;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #9333ea, #c084fc);
    color: white;
    border: none;
    border-radius: 12px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #7e22ce, #a855f7);
    color: white;
}

.footer {
    text-align: center;
    padding: 20px;
    margin-top: 50px;
    color: #b3b3b3;
    border-top: 1px solid #20263d;
    font-size: 16px;
}

.footer a {
    color: #c084fc;
    text-decoration: none;
}

.footer a:hover {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------
# SIDEBAR
# --------------------------------

# st.sidebar.title("🎵 EchoTune")
# st.sidebar.markdown("### Navigation")
# st.sidebar.markdown("🏠 Home")
# st.sidebar.markdown("🔥 Trending")
# st.sidebar.markdown("⭐ Favorites")
# st.sidebar.markdown("---")
# st.sidebar.info("Feel the vibe before you play 🎧")

# --------------------------------
# HEADER
# --------------------------------

st.markdown("""
<h1 style='font-size:60px;'>
🎵 EchoTune - A Music Recommendation System
</h1>

<p style='font-size:20px;color:#b3b3b3;'>
Discover songs you'll love ✨
</p>
""", unsafe_allow_html=True)

# --------------------------------
# SONG LIST
# --------------------------------

song_list = sorted(df[SONG_COLUMN].dropna().unique())

selected_song = st.selectbox(
    "🔍 Search or Select a Song",
    song_list
)

# --------------------------------
# RECOMMEND FUNCTION
# --------------------------------

def recommend(song):

    index = df[df[SONG_COLUMN] == song].index[0]

    distances = similarity[index]

    # TAKE MORE SONGS
    recommended_songs = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:20]

    # RANDOMLY PICK 5 DIFFERENT SONGS EVERY TIME
    random_recommendations = random.sample(recommended_songs, 5)

    return random_recommendations

# --------------------------------
# BUTTON
# --------------------------------

if st.button("✨ Recommend"):

    recommendations = recommend(selected_song)

    st.markdown("## 🎧 Recommended Songs")

    cols = st.columns(5)

    for idx, i in enumerate(recommendations):

        song_name = df.iloc[i[0]][SONG_COLUMN]

        with cols[idx]:

            st.markdown(f"""
            <div class="song-card">
                <div style="font-size:50px;">🎵</div>
                <div class="song-title">{song_name}</div>
                <div class="song-sub">Recommended for you</div>
            </div>
            """, unsafe_allow_html=True)

# --------------------------------
# FOOTER
# --------------------------------

st.markdown("""
<div class="footer">

<p>Developed by <b>Gaurav Kumar</b></p>

<p>
📧 Contact:
<a href="mailto:gauravkr.pro@gmail.com">
gauravkr.pro@gmail.com
</a>
</p>

</div>
""", unsafe_allow_html=True)