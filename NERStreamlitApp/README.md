# 🎤 Taylor Swift's Lyrical Legacy: Custom NER + Visual Insights 🎤

Calling all Swifties! This interactive Streamlit combines Natural Language Processing (NLP) and data visualization to explore the storytelling evolution of one of the greatest lyricists of our time. This app uses spaCy to implement custom Named Entity Recognition (NER) on Taylor Swift’s lyrics and provides album-based analytics, such as total word counts, to examine lyrical trends.

## insert image
![TSPIANO]()

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
## How to run the App

You can try the app live here: [**Streamlit App Link**](https://your-app-url.streamlit.app)  
*(Replace with your deployed URL)*

Or, you can download the app locally. Follow these instructions to learn how to do so!

1. Clone the repository:
```bash
git clone https://github.com/jsmall16/Small-Python-Portfolio/tree/main/NERStreamlitApp
cd NERStreamlitApp
```

2. Run this command to view the files in the project folder:
```bash
ls
```
3. Move into the directory containing your Streamlit app
```bash
cd path/to/your/project
```
4. Launch the Streamlit app by running
```bash
streamlit run Home.py
```
5. Open the App in Your Browser Once the app starts, your terminal will display a local URL (e.g., http://localhost:8501). Click this link or copy and paste it into your web browser to start exploring the app.
