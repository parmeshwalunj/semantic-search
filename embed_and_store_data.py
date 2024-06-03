# Parmesh Mohan Walunj
# 1002149428
"""
- Prepare the text to embed for each reccord of your dataset.
    - Create the reccord.
        - Clean the text.
        - Concatenate fields.
- Choose a Sentence Embedding Model.
- Embed the text generated in the previous step for each reccord.
- Store the embeddings in a vector database (i.e. elasticsearch).
"""

import pandas as pd
from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
from indexMapping import indexMapping


cleaned_dataset = pd.read_csv('/Users/parmesh/My Mac/MS/ML2/semantic_search/cleaned_imdb_top_1000.csv')


# model = SentenceTransformer('all-MiniLM-L6-v2')
model = SentenceTransformer('all-mpnet-base-v2')

cleaned_dataset['vectoredDetails'] = cleaned_dataset['Cleaned_Text'].apply(lambda x: model.encode(x))

# es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

es = Elasticsearch("https://localhost:9200", basic_auth=("elastic", "elastic_pass"), ca_certs="mypath/elastic/elasticsearch-8.12.1/config/certs/http_ca.crt")
print(es.ping())

# es.indices.create(index="imdb_movies", mappings = indexMapping)
# print("Successfully created Index")
try:
    es.indices.create(index="imdb_movies", mappings=indexMapping)
    print("Successfully created Index")
except Exception as e:
    if 'resource_already_exists_exception' in str(e):
        print("Index 'imdb_movies' already exists.")
    else:
        # Handle other Elasticsearch exceptions
        print("An error occurred:", e)

records_list = cleaned_dataset.to_dict("records")
# print(records_list[10])

for record in records_list:
    try:
        print(record)
        break
        # es.index(index="imdb_movies", document=record)
    except Exception as e:
        print(e)
print(es.count(index="imdb_movies"))
exit()
# chunk_size = 512

# text_chunker = TextChunker(chunk_size, tokens=False)

# for index, row in cleaned_dataset.iterrows():
    # text_to_embed = row['Series_Title'] + ' ' + row['Overview']
    # text_to_embed = row['Cleaned_Text']
    # chunks = text_chunker.chunk(text_to_embed)
    
    # embeddings = []
    # for chunk in chunks:
    #     embedding = model.encode(chunk)
    #     embeddings.append(embedding)
    
    # combined_embedding = [e.tolist() for e in embeddings]
    
# doc = {
#     'Series_Title': row['Series_Title'],
#     'Overview': row['Overview'],
#     'embedding': combined_embedding
# }
# es.index(index='movie_embeddings', body=doc)

