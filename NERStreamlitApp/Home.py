# Import necessary libraries 
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Title and header image
st.title("Taylor Swift's Lyrical Legacy")
st.image('NERStreamlitApp/TSNERIMAGE.jpeg')

# Intro Section 
st.subheader("The Power of Her Pen")
st.write("""
    Taylor Swift stands as one of the most influential artists of our generation. 
    Beginning her career in country music, she has effortlessly explored and mastered 
    multiple genres, redefining the boundaries of pop along the way. Her lyrics resonate 
    across generations, offering a song for every emotion and moment.
    """)

st.subheader("What You'll Find Here")
st.write("""
This app explores Taylor’s discography using data and natural language processing. 
You’ll uncover trends in:
- **Total Words used across her albums**
- **Custom Named Entity Recognition (NER)** for identifying places, names, and symbols in her lyrics

Together, these tools offer a fresh lens into her storytelling evolution
""")

# Album overview section 
st.markdown("### 💿 Taylor Swift Albums at a Glance")
st.markdown("""
                Below is a quick tour through Taylor's main albums (excluding holiday albums and songs used in films).
                Taylor is known for reinventing herself with her music, and each album represents a distinct era in her lyrical evolution. 
                From country storytelling to poetry, explore how her words have grown alongside her sound:
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
Below is the **total word count** for each album, displayed in release order, using colors that reflect each era’s mood and aesthetic.
""")

# Load and clean song lyric dataset to perform visualizations 
swift_songs = pd.read_csv("Data/songs.csv")

# Rename and standardize column names
swift_songs = swift_songs.rename(columns={"Title": "song", "Album": "album", "Lyrics": "lyrics"})
swift_songs['album'] = swift_songs['album'].str.strip().str.title() # Removes any leading or trailing whitespace from each album name.
                                                                    # Makes Album Names title case 

# Establish only her main discography (exclude holiday albums and albums for movies)
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

# Custom colors to match each album's aesthetic
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

### Anlayze Word Counts 

# Filter only albums in list
main_df = swift_songs[swift_songs['album'].isin(release_order)].copy()

# Summarize total word count per album
main_df['word_count'] = main_df['lyrics'].str.split().apply(len)
album_totals = main_df.groupby('album')['word_count'].sum().reset_index()
album_totals.columns = ['album', 'total_word_count']

# Sorts the DataFrame based on the custom order I set
album_totals['album'] = pd.Categorical(album_totals['album'], categories=release_order, ordered=True)
album_totals = album_totals.sort_values('album')
# Assigns each album a specific color based on colors I created 
album_totals['color'] = album_totals['album'].map(album_colors)

# Plot data visualization of word counts per album
st.markdown("### Total Word Count by Album")
fig, ax = plt.subplots(figsize=(12, 6))

# Create a bar plot using Seaborn
sns.barplot(
    data=album_totals, # Data source
    x='album',          # X-axis: album names
    y='total_word_count', # Y-axis: total word counts per album
    palette=album_totals['color'].tolist(),  #Use custom colors defined per album
    ax=ax               # Use the axes object created above
)
# Label the y-axis
ax.set_ylabel("Total Word Count")
# Label the x-axis
ax.set_xlabel("Album")
# Rotate x-axis labels for better readability and align to the right
ax.set_xticklabels(album_totals['album'], rotation=45, ha="right")
# Render the plot in the Streamlit app
st.pyplot(fig)

# Closing Section
st.markdown("""
From her debut album to her latest album, Taylor’s songwriting 
reflects a continuous evolution in both style and substance.

Navigate through this app to explore deeper insights into her storytelling!""")