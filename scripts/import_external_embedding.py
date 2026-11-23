python scripts/import_external_embedding.py external/mat2vec_200d.csv \
  --output data/mat2vec_200d.json \
  --name "mat2vec-200D" \
  --family "nlp-literature" \
  --description "Full 200D Word2Vec elemental embeddings trained on 3.3M materials science abstracts." \
  --strengths "Captures nuanced literature synthesis co-occurrence across functional oxides and alloys." \
  --limitations "Reflects corpus frequency biases." \
  --citation "Tshitoyan et al., Nature 571, 95-98 (2019)"
