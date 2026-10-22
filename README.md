# World Happiness Report Analysis

## General info
The aim of the project was the data analysis of world happiness data with SQL and python. The reasults of analysis showed what determines about happy of given country.  The project includes analysis of 'World Happiness Report' over 5 years (2015-2019) and it performed by SQL with python libraries (pandas, matplotlib and seaborn). 

### Dataset
The dataset contains details of the 'World Happiness Report' reports from five years (2015-2019). It comes from Kaggle and can be find [here](https://www.kaggle.com/datasets/unsdsn/world-happiness).

## Motivation
The World Happiness Report is a survey of the state of global happiness. The reports review the state of happiness in the world today and show how the new science of happiness explains personal and national variations in happiness. The happiness scores and rankings use data from the Gallup World Poll. The scores are based on answers to the main life evaluation question asked in the poll. It base rate their own current lives on scale where the best possible life for them being a 10 and the worst possible life being a 0. The scores are from nationally representative samples for the years 2015-2019. The columns following the happiness score estimate the extent to which each of six factors – economic production, social support, life expectancy, freedom, absence of corruption, and generosity – contribute to making life evaluations higher in each country.

## Summary
The data insights concluded the following questions:
- Which countries are the best to live in?
- What countries and regions are the happiest and which are the least?
- Which factors the most influence happiness (GDP, social support, health, freedom)?
- What is the relationship between economy (GDP per capita) and happiness score?
- Where does Poland rank in the ranking?
- What changes over time - which countries advanced and which fell in the ranking between 2015 and 2017?

### Project contains:
- Report analysis from 2015-2017 years - **happiness_part_1.ipynb**
- Report analysis from 2018-2019 years - **happiness_part_2.ipynb**
- Python script to put data to sql database - **data_to_database.py**

## Technologies

**The project is created with:**
- SQL: SQLite3.
- Python: libraries (pandas, matplotlib, seaborn).

**Running the project:**

To run this project use Jupyter Notebook or Google Colab.

You can run the scripts in the terminal:

    data_to_database.py
