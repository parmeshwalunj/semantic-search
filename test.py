# Parmesh Mohan Walunj
# 1002149428

from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

import pandas as pd
# model = SentenceTransformer('all-mpnet-base-v2')

es = Elasticsearch("https://localhost:9200", basic_auth=("elastic", "elastic_pass"), ca_certs="mypath/elastic/elasticsearch-8.12.1/config/certs/http_ca.crt")
# s = es.indices.delete(index="imdb_movies",)
es.indices.refresh(index="imdb_movies")
# print(s)
print(es.count(index="imdb_movies"))

# cd = pd.read_csv("cleaned_imdb_top_1000.csv")
# print(cd['Certificate'][999])

# input_keyword = "show me some car movies"
# vector_input_keyword = model.encode(input_keyword)

# query = {
#     "field":"vectoredDetails",
#     "query_vector":vector_input_keyword,
#     "k":2,
#     "num_candidates":890,
# }

# res = es.knn_search(index="imdb_movies",knn=query, source=["Series_Title","Overview"])
# print(res["hits"]["hits"])
# print(es.ping())
