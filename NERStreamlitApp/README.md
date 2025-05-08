# 🎤 Taylor Swift's Lyrical Legacy: Custom NER + Visual Insights 🎤
![TSPIANO](maxresdefault.jpg)

**Calling all Swifties!** This interactive Streamlit app combines Natural Language Processing (NLP) and data visualization to explore the storytelling evolution of one of the greatest lyricists of our time. This app uses spaCy to implement custom Named Entity Recognition (NER) on Taylor Swift’s lyrics, and also provides album-based analytics to examine lyrical trends.

---

## Project Overview

### Purpose
This app allows fans and analysts to:
- Upload or paste Taylor Swift lyrics
- Define custom entities
- Visualize entity recognition results using spaCy’s EntityRuler and displacy
- Analyze word counts across albums 

### Why spaCy?
spaCy is a library in Python that is used to conduct Natural Language Processing.

- One component of spaCy, Named Entity Recognition, allows users to extract text pertaining to pre-defined categories
- The EntityRuler allows users to build their own recognition rules and make the analysis more personalized

---
## Dataset Description
Source: [Taylor Swift Lyrics Dataset - ShaynaK (GitHub)](https://github.com/shaynak/taylor-swift-lyrics/blob/main/songs.csv)

- This dataset contains Over 258 songs from over 11 studio and special-edition albums. 
- Each song includes:
    - Title
    - Album
    - Corresponding lyric

---

## **Data Pre-Processing Steps**

To ensure that the data was ready for analysis, I performed a few different pre-processing steps:

- **New columns** - Created a new column (word_count) that counts the number of words in each lyric
- **Aggregations** - Filtered albums to only include Taylor's main discography and aggregated by album
- **Text cleaning** - Renamed column names to be lowercase, removed trailing spaces to ensure consistency, and converted album titles to Title case 

---

##  App Features 

### 1️⃣ Visualize Total Word Count per Album

![TSDATA](TSDATA.png)

This bar chart shows the total word count for each of Taylor Swift’s main studio albums, arranged in chronological order. It highlights how her lyrical volume has evolved over time, with a noticeable peak in Red (Taylor’s Version) and The Tortured Poets Department. Albums like Folklore and Taylor Swift feature more concise writing, while 1989 and Midnights strike a nice balance in songwriting length. Each bar is color-coded to reflect the aesthetic of its corresponding era, offering a data-driven, stylistic look at Taylor’s discography.


### 2️⃣ Custom Named Entity Recognition 
- Add your own entity labels and keyword patterns (ex- "James" under "LOVE_INTEREST")
- Upload .txt files, paste in your own lyrics, or use the sample lyrics provided
- Visualize output with entities highlighted using spaCy’s displacy

A custom Entity Ruler is especially useful for Swifties because it lets fans tag and track recurring names, places, and motifs across Taylor’s lyrics. By creating custom labels like LOVE_INTEREST, CITY, or SYMBOL, fans can uncover deeper patterns in her storytelling, whether it’s identifying how often she references New York or spotting easter eggs tied to specific eras.

## Example Usage
**1. Define a pattern:**
  - Label: CITY
  - Pattern: LONDON

![APPUI](APP_UI.png)

**2. Paste, upload, or use sample lyrics:**


![text](Text_type.png)


**3. View results:**

Using the sample lyrics, this is what the output may look like, depending on the types of entities and patterns you define. 

![DISPLACY](SpaCy_display.png)

---
## How to run the App

You can try the app live here: [**Streamlit App Link**](https://small-python-portfolio-tswift-ner.streamlit.app/)  

Or, you can download the app locally. Follow these instructions to learn how to do so!

### Make sure you have the required libraries installed

- matplotlib==3.10.1
- pandas==2.2.3
- seaborn==0.13.2
- spacy==3.8.5
- streamlit==1.37.1

To install them manually using pip:
```bash
pip install streamlit spacy pandas matplotlib seaborn
python -m spacy download en_core_web_sm
```
To get started installing the app:

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/jsmall16/Small-Python-Portfolio.git
```

### **Step 2: Run this command to view the files in the project folder**
```bash
ls
```
### **Step 3: Move into the directory containing your Streamlit app**
```bash
cd NERStreamlitApp
```
### **Step 4:  Launch the Streamlit app by running**
```bash
streamlit run Home.py
```
Once the app starts, your terminal will display a local URL. Click this link or copy and paste it into your web browser to start exploring the app.
   
---

## 👤 Accessibility Notes

This app is best utilized with dark mode viewing. The display and visual contrast settings were designed with dark mode in mind.  

For the best user experience:
- Enable dark mode in your system or browser
- To do so in Streamlit Community Cloud:
  - Click the three dots
  - Go to Settings
  - Go to "Choose app theme, colors and fonts"
  - Select "Dark"
---
## 💡 Sources & Acknowledgements

### Data

- [Taylor Swift Lyrics Dataset - ShaynaK (GitHub)](https://github.com/shaynak/taylor-swift-lyrics/blob/main/songs.csv)

### Documentation 

- [The Basics of SpaCy](https://spacy.pythonhumanities.com/01_01_install_and_containers.html)
- [Entity Ruler](https://spacy.io/api/entityruler)
- [Streamlit Cheat sheet](https://cheat-sheet.streamlit.app/) 
