import pandas as pd
import glob
import sqlite3

path = 'Datasets\world_happines\*.csv'


def rename_column(df):
    '''Rename columns of data'''
    data = df.rename(columns = {'Happiness Rank':'Ranking', 'Happiness Score':'Score', 'Standard Error':'Std_error',
                     'Economy (GDP per Capita)':'Economy', 'Health (Life Expectancy)':'Health',
                     'Trust (Government Corruption)':'Trust', 'Dystopia Residual':'Dystopia_Residual',
                     'Lower Confidence Interval':'Lower_CI', 'Upper Confidence Interval':'Upper_CI', 
                     'Happiness.Rank':'Ranking', 'Happiness.Score':'Score', 'Whisker.high':'Whisker_high',
                     'Whisker.low':'Whisker_low', 'Economy..GDP.per.Capita.':'Economy', 'Health..Life.Expectancy.':'Health',
                     'Trust..Government.Corruption.':'Trust', 'Dystopia.Residual':'Dystopia_Residual'}, inplace=True)
    return data


def rename_columns(df):
    '''Rename columns of data'''
    table = df.rename(columns = {'Overall rank':'Ranking', 'Country or region':'Country', 'GDP per capita':'Economy',
                     'Social support':'Social_support', 'Healthy life expectancy.':'Health',
                     'Freedom to make life choices':'Freedom', 'Perceptions of corruption':'Trust'}, inplace=True)
    return table


'''Read data'''

dfs = dict(("df{}".format(i), pd.read_csv(file)) for i,file in enumerate(glob.iglob(path), 1))

df1 = dfs['df1']
df2 = dfs['df2']
df3 = dfs['df3']
df4 = dfs['df4']
df5 = dfs['df5']

'''Cleaning dataset'''

# removing unnecessary column
for df in (df1,df2,df3):
    if 'Dystopia Residual' in df:
        del df['Dystopia Residual']

# applying functions
for df in (df1,df2,df3):
    df = rename_column(df)

for df in (df4,df5):
    df = rename_columns(df)
 
'''Connecting with database'''

conn = sqlite3.connect("happines.db")

cur = conn.cursor()

# Files to sql database
df1.to_sql("Report2015", conn, if_exists="replace")
df2.to_sql("Report2016", conn, if_exists="replace")
df3.to_sql("Report2017", conn, if_exists="replace")
df4.to_sql("Report2018", conn, if_exists="replace")
df5.to_sql("Report2019", conn, if_exists="replace") 

print('The data added successfully')
