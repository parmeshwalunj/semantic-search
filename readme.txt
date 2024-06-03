Name: Parmesh Mohan Walunj
StudentID: 1002149428

This project implements Semantic Search Engine using the Elasticsearch.

Dataset: https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows

Flow:
1. Importing the dataset from kaggle
2. Preprocessing the dataset 
    - Removing the NaN values and converting string values to int values from Certificate, Gross, Meta_score and Released_Year.
    - Removing the stopwords for the data from the Overview column.
3. Making a new column vectoredDetails by concatenating the Series_Title + Genre + Overview.
4. Performing the Embedding by Vectorizing the vectoredDetails columns using the BERT model from SentenceTransformer library.
5. Creating the index in the Elasticsearch and adding documents (data) to the created index and making the vectoredDetails column searchable.
6. Creating the UI using streamlit to input the user query and show the search results.

File to be executed: search_app.py

References:
https://docs.streamlit.io/get-started/tutorials
https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/index.html
https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/installation.html
https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/examples.html#ex-index
https://github.com/gborn/Semantic-Search-Engine-Using-ElasticSearch/blob/main/app.py
https://github.com/abidsaudagar/semantic-search-elastic-search-and-BERT-vector-embedding
https://medium.com/version-1/vector-based-semantic-search-using-elasticsearch-48d7167b38f5