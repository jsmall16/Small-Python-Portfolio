# 🏅 2008 Olympic Medalists: Data Analysis🏅

## Project Overview  
The 2008 Summer Olympics brought together the world’s top athletes competing in various sports, earning gold, silver, and bronze medals for their performances.  

This project cleans, organizes, and analyzes* Olympic medalist data to uncover meaningful insights, including:  
- Which sports had the most medals?
- How were medals distributed between male and female athletes?
- Which gender won the most gold medals in athletics? 
- How does the overall medal distribution break down by type? 

This analysis follows the Tidy Data Principles by restructuring the dataset into a more usable format, making it easier for aggregation, visualization, and further analysis.  


## Dataset Description

📌 Source: OlympicsGoNUTS 2008 Dataset
The dataset contains 1,875 Olympic medalists across 70 different sports in the 2008 Olympics.
******Insert description about where the data comes from ******

--- 

## Pre-Processing Steps:
- Converted wide format data (sports as columns) to tidy long format
- Extracted gender and sport into separate columns
- Removed NaN values and checked for duplicates

After cleansing, here are the column names in the dataset:
- **medalist_name**: Athlete's name
- **sport**: Sport category
- **gender**: Male or Female
- **medal**: Type of medal (Gold, Silver, Bronze)
---

## Data Aggregation 
- Counted total medals per sport
- Analyzed medal distribution by gender
- Focused on Athletics as the highest-medal sport
---
## Data Visualization 
During my analysis, I discovered several compelling insights that reveal interesting trends and patterns:

### Overall Medal Distribution
![1stvis](Overall%20Medal%20Distribution.png)

This pie chart illustrates the overall medal distribution, with gold medals accounting for 35.6%, silver medals at 33.1%, and bronze medals at 31.3%. The data suggests a relatively balanced distribution among the three medal types, with gold being the most awarded.

### Medal County by Sport
![2ndvis](Sport%20Medal%20Count.png)

This bar chart showcases the top 10 sports by total medal count in the 2008 Olympics, with athletics, rowing, and swimming leading the rankings. The distribution of gold, silver, and bronze medals varies across sports, with athletics and rowing securing the most medals overall.

### Athletics Medal Count by Gender
![3rdvis](Athletics%20Medal%20Count%20by%20Gender.png)

This bar chart illustrates the 2008 Olympics athletics medal count by gender, showing a fairly balanced distribution between male and female athletes. While silver medals were the most awarded for both genders, males received slightly more bronze medals and females received slightly more gold medals. 

### Concluding Thoughts
This analysis provides a clear overview of how medals were distributed across sports and genders in the 2008 Olympics, highlighting key trends in athletic performance. The findings emphasize the competitive balance across events while showcasing slight differences in medal distribution between male and female athletes.

---

##  How to Run This Project  

### 1️⃣ Download the Jupyter Notebook  
- Go to the **GitHub repository**.  
- Click on the **Jupyter Notebook file (`.ipynb`)**.  
- Click **"Download raw"** or **"Download"** and save it to a folder on your computer.  

### 2️⃣ **Ensure Python or Anaconda are installed**

### 3️⃣**Download Required Dependencies**
- This installs pandas, matplotlib, and seaborn, which are required for data analysis and visualization.
  
**For Python users**
```bash
pip install pandas matplotlib seaborn
```
**For Anaconda users**
```bash
conda install pandas matplotlib seaborn
```

### 4️⃣ **Open Jupyter Notebook**
Navigate to the folder where you saved the .ipynb file:
Launch Jupyter Notebook and open the Olympic_Medal_Analysis.ipynb file:
```
cd path/to/folder
jupyter notebook
```

---

## Acknowledgments & References  
