# Parmesh Mohan Walunj
# 1002149428

# Which columns will you use?
# Clean your columns
# Concatenate the columns needed for your embedding
# Create new column with concatenated and clean text

import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    cleaned_text = ' '.join(tokens)
    return cleaned_text

movies = pd.read_csv("imdb_top_1000.csv")

# selected_columns = ['Series_Title', 'Overview']
selected_columns = ['Overview']


def str_to_int(value):
    try:
        if pd.isnull(value):  
            return 0     
        return int(value.replace(',',''))
    except ValueError:
        return value  

def null_to_none(value):
    try:
        if pd.isnull(value):  
            return ' '  
        else:
            return value
    except ValueError:
        return value
def null_to_float(value):
    try:
        if pd.isnull(value): 
            return float(0)  
        return value
    except ValueError:
        return value     
    
# Applying lambda function to the columns
movies['Released_Year'] = movies['Released_Year'].apply(lambda x:  0 if x=='PG' else int(x))
# movies['Series_Title']=movies['Series_Title'].apply(lambda x: null_to_none(x))
movies['Certificate']=movies['Certificate'].apply(lambda x: null_to_none(x))
movies['Meta_score']=movies['Meta_score'].apply(lambda x: null_to_float(x))
movies['Gross'] = movies['Gross'].apply(lambda x: str_to_int(x))

for col in selected_columns:
    movies["Cleaned_Overview"] = movies[col].apply(clean_text)

movies['Cleaned_Text'] = movies['Series_Title'] + ' ' + movies['Genre'] + ' ' + movies['Cleaned_Overview']
del movies['Cleaned_Overview']
movies.to_csv("cleaned_imdb_top_1000.csv", index=False)