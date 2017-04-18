from datasets.sentences import sentences

# from pprint import pprint

import gensim, logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# dictionary = gensim.corpora.Dictionary(sentences)
# dictionary.save('vectors_0.0.1.dict')
# print(dictionary.token2id)

# corpus = [dictionary.doc2bow(sentence) for sentence in sentences]
# gensim.corpora.MmCorpus.serialize('vectors_0.0.1.mm', corpus)
# pprint(corpus)

model = gensim.models.Word2Vec(sentences, size=10, window=5, min_count=1, workers=4)
model.save('vectors_0.0.1_10.model')

print(model)
