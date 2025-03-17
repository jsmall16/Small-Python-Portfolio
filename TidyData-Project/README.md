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

## Data Aggregation (Summarizing Trends)
- Counted total medals per sport
- Analyzed medal distribution by gender
- Focused on Athletics as the highest-medal sport
---
## Data Visualization 

![1stvis](Overall%20Medal%20Distribution.png)

![2ndvis](Sport%20Medal%20Count.png)

![3rdvis](Athletics%20Medal%20Count%20by%20Gender.png))

---

