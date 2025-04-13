# 🎤 Taylor Swift's Lyrical Legacy: Custom NER + Visual Insights 🎤
![TSPIANO](maxresdefault.jpg)

Calling all Swifties! This interactive Streamlit combines Natural Language Processing (NLP) and data visualization to explore the storytelling evolution of one of the greatest lyricists of our time. This app uses spaCy to implement custom Named Entity Recognition (NER) on Taylor Swift’s lyrics and provides album-based analytics, such as total word counts, to examine lyrical trends.

---

## Project Overview

### Purpose
This app allows fans and analysts alike to:
- Upload or paste Taylor Swift lyrics
- Define custom entities (e.g., "LOVE_INTEREST", "CITY")
- Visualize entity recognition results using spaCy’s `EntityRuler` and `displacy`
- Analyze word counts across albums with themed visualizations

### Why spaCy?
spaCy is a powerful NLP library that supports customizable NER pipelines. 
- The EntityRuler allowers users to build their own recognition rules and make the analysis more fan-personalized
---

## App Features 

## Word Count Analysis per Album 
Visualize total word count per album

Albums styled using their unique aesthetic with color-coded bars

Data based on cleaned lyric dataset from major Taylor Swift album


## Customer NER
Named Entity Recognition
Add your own entity labels and keyword patterns (e.g., "James" under "LOVE_INTEREST")

Upload .txt files or paste in your own lyrics

Visual output with entities highlighted using spaCy’s displacy.render

📁 Example Usage
Define a pattern:

Label: LOVE_INTEREST

Pattern: James

Paste this lyric:

"You know I love a London boy. I enjoy walking Camden Market in the afternoon..."

View results:

James: LOVE_INTEREST

London: CITY


---
## How to run the App

You can try the app live here: [**Streamlit App Link**](https://your-app-url.streamlit.app)  
*(Replace with your deployed URL)*

Or, you can download the app locally. Follow these instructions to learn how to do so!

### Make sure you have the required libraries installed
  - streamlit
  - spacy
  - pandas
  - matplotlib
  - seaborn

To install them manually:
```bash
pip install streamlit spacy pandas matplotlib seaborn
python -m spacy download en_core_web_sm
```

1. Clone the repository:
```bash
git clone https://github.com/jsmall16/Small-Python-Portfolio/tree/main/NERStreamlitApp
cd Small-Python-Portfolio/NERStreamlitApp
```

2. Run this command to view the files in the project folder:
```bash
ls
```
3. Move into the directory containing your Streamlit app
```bash
cd NERStreamlitApp
```
4. Launch the Streamlit app by running
```bash
streamlit run Home.py
```
5. Open the App in Your Browser Once the app starts, your terminal will display a local URL (e.g., http://localhost:8501). Click this link or copy and paste it into your web browser to start exploring the app.

---

From the storytelling of Speak Now to the poetry of Folklore and The Tortured Poets Department, this app offers both fans and data enthusiasts a lyrical deep dive into Taylor Swift's evolving artistry.

---

## Sources & Acknowledgements

1. Data
2. spaCy sources
