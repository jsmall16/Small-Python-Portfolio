
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Taylor Swift's Lyrical Legacy")
st.image('TSNERIMAGE.jpeg')

with st.container():
    st.subheader("✏️ The Power of Her Pen")
    st.write("""
    Taylor Swift has redefined modern pop and country music with her deeply personal, poetic, and narrative-driven lyrics.
    From heartbreak anthems to indie introspection, her words resonate with fans across generations.
    """)
    st.subheader("🔍 What You'll Find Here")
    st.write("""
    This app dives into her discography using data and natural language analysis — 
    including lyrical word counts, sentiment trends, and even custom entity recognition.
    """)
    st.markdown("### 💿 Taylor Swift Albums at a Glance")
    st.markdown("""
                Below is a quick tour through Taylor's main albums — each representing a distinct era in her lyrical evolution. 
                From country storytelling to indie introspection, explore how her words have grown alongside her sound:
                """)
    st.markdown("""
        - **🤠 Taylor Swift** 
        - **🌟 Fearless (TV)** 
        - **💜 Speak Now (TV)** 
        - **❤️ Red (TV)**  
        - **💎 1989 (TV)** 
        - **🖤 Reputation**  
        - **💗 Lover** 
        - **🌲 Folklore** 
        - **🍂 Evermore** 
        - **🌌 Midnights** 
        - **📖 Tortured Poets Dept.** 
        """)

st.markdown("""
Let’s take a data-driven look at how Taylor’s lyrical output has changed across albums. 
Here’s the **total word count** for each album — shown in order of release, using era-inspired colors.
""")

swift_songs = pd.read_csv("Data/songs.csv")
swift_songs = swift_songs.rename(columns={"Title": "song", "Album": "album", "Lyrics": "lyrics"})
swift_songs['album'] = swift_songs['album'].str.strip().str.title()

# Define canonical album names (case matched to CSV after .title())
release_order = [
    "Taylor Swift",
    "Fearless (Taylor'S Version)",
    "Speak Now (Taylor'S Version)",
    "Red (Taylor'S Version)",
    "1989 (Taylor'S Version)",
    "Reputation",
    "Lover",
    "Folklore",
    "Evermore",
    "Midnights",
    "The Tortured Poets Department"
]

# Album colors
album_colors = {
    "Taylor Swift": "#81E6D9",
    "Fearless (Taylor'S Version)": "#E6BE8A",
    "Speak Now (Taylor'S Version)": "#A78AC5",
    "Red (Taylor'S Version)": "#C8102E",
    "1989 (Taylor'S Version)": "#ADD8E6",
    "Reputation": "#8E8E8E",
    "Lover": "#FFB6C1",
    "Folklore": "#DCDCDC",
    "Evermore": "#A0522D",
    "Midnights": "#191970",
    "The Tortured Poets Department": "#B0AFAF"
}

# Filter only albums in list
main_df = swift_songs[swift_songs['album'].isin(release_order)].copy()

# Word counts
main_df['word_count'] = main_df['lyrics'].str.split().apply(len)
album_totals = main_df.groupby('album')['word_count'].sum().reset_index()
album_totals.columns = ['album', 'total_word_count']

# Order and color match
album_totals['album'] = pd.Categorical(album_totals['album'], categories=release_order, ordered=True)
album_totals = album_totals.sort_values('album')
album_totals['color'] = album_totals['album'].map(album_colors)

# Plot
st.markdown("### Total Word Count by Album (Release Order)")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(
    data=album_totals,
    x='album',
    y='total_word_count',
    palette=album_totals['color'].tolist(),
    ax=ax
)
ax.set_ylabel("Total Word Count")
ax.set_xlabel("Album")
ax.set_xticklabels(album_totals['album'], rotation=45, ha="right")
st.pyplot(fig)

st.markdown("""
From the raw honesty of *Taylor Swift* to the poetic complexity of *The Tortured Poets Department*, Taylor’s discography shows 
how language, emotion, and storytelling evolve over time. And this is just the beginning — explore more in the pages ahead.
""")
