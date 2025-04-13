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

## 🛠️ Setup & Installation

### 🔗 Deployed App
You can try the app live here: [**Streamlit App Link**](https://your-app-url.streamlit.app)  
*(Replace with your deployed URL)*

### 💻 Local Installation

1. Clone the repo:
```bash
git clone https://github.com/yourusername/TaylorSwiftNERApp.git
cd TaylorSwiftNERApp
