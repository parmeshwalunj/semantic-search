# Parmesh Mohan Walunj
# 1002149428
"""
    Create an Streamlit app that does the following:

    - Reads an input from the user
    - Embeds the input
    - Search the vector DB for the entries closest to the user input
    - Outputs/displays the closest entries found
"""
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import streamlit as st
import pandas as pd



try:
    es = Elasticsearch("https://localhost:9200", basic_auth=("elastic", "gCu*pg8LcRYl_+TRqcYA"), ca_certs="/Users/parmesh/My Mac/MS/ML2/semantic_search/elastic/elasticsearch-8.12.1/config/certs/http_ca.crt")
except ConnectionError as e:
    print("Connection has Error:", e)
    
if es.ping()==True:
    print("Succesfully connected to ElasticSearch VectoredDB")
else:
    print("ERROR!! Can't connect to Elasticsearch!")




def search(input_keyword):
    model = SentenceTransformer('all-mpnet-base-v2')
    vector_of_input_keyword = model.encode(input_keyword)
    query = {
        "field":"vectoredDetails",
        "query_vector":vector_of_input_keyword,
        "k":10,
        "num_candidates":1000,
    }
    temp = es.knn_search(index="imdb_movies", knn=query , source=["Series_Title","Overview", "IMDB_Rating","Genre"])
    res = temp["hits"]["hits"]

    return res

st.write("""
# IMDB Movie Search
Explore movies with *keywords!*
""")
 
search_query = st.text_input("Enter your search query")
# st.button("Search")

if st.button("Search"):
    if search_query:
        results = search(search_query)

        # Display search results
        st.subheader("Search Results")
        for result in results:
            with st.container():
                if '_source' in result:
                    try:
                        st.header(f"{result['_source']['Series_Title']}")
                    except Exception as e:
                        print(e)
                    
                    try:
                        st.write(f"*Genre:* {result['_source']['Genre']}")
                        st.write(f"*Rating:* {result['_source']['IMDB_Rating']}")
                        st.write(f"*Description:* {result['_source']['Overview']}")
                    except Exception as e:
                        print(e)
                    st.divider()

# df = pd.read_csv("/Users/parmesh/My Mac/MS/ML2/semantic_search/cleaned_imdb_top_1000.csv")
# st.line_chart(df)