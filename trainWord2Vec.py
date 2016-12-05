# -*- coding: utf-8 -*-
'''
python version: 2.7

segment Chinese words
'''

import sys
import logging
from gensim.models import word2vec

# start segmentation
def main(segTextPath, modelSavePath):
	# iterate wiki articles
	sentences = word2vec.Text8Corpus(segTextPath)
	model = word2vec.Word2Vec(sentences, size=256, sg=1)
	model.save_word2vec_format(modelSavePath, binary=True)


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print ("please input a segmented text file path, and a model output path.")
		exit()
	# logging congiurationg
	logging.basicConfig(format='%(asctime)s: %(levelname)s : %(message)s', level = 1)
	# turn off lemmatization
	main(sys.argv[1], sys.argv[2])





