# examples from official documentation

# get most similar words
'''
model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
[('queen', 0.50882536)]
model.doesnt_match("breakfast cereal dinner lunch";.split())
'cereal'
model.similarity('woman', 'man')
0.73723527
'''


# get the mebedding of a word
'''
model['computer']  # raw NumPy vector of a word
array([-0.00449447, -0.00310097,  0.02421786, ...], dtype=float32)
'''



import sys
from gensim.models import word2vec
import logging 

'''
@input modelPath
'''
def test(modelPath):
	# get model
	model = word2vec.Word2Vec.load_word2vec_format(modelPath, binary=True)

	# get embedding of a specific word, change encoding format if necessary
	print(model['猫'].decode('utf-8'))

	# find similarity between two words
	model.similarity('华南虎'.decode('utf-8'),'东北虎'.decode('utf-8'))


	# list top 100 most similar words
	for term,value in model.similar_by_word('猫'.decode('utf-8'),topn=100):
		print(term,value)


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('please input model(embedding) path')
	test(sys.argv[1])

