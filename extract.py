# -*- coding: utf-8 -*-
'''
python version: 2.7

extract text from xml dump file
tranfer complex Chinese into Simplified Chinese
'''


import logging
import sys
from hanziconv import HanziConv
#HanziConv.toSimplified(element.text)
from gensim.corpora import WikiCorpus

# start extracting
def main(wikiXmlPath, outputPath):
	# map
	wiki_corpus = WikiCorpus(sys.argv[1], dictionary={})
        wiki_corpus.LEMMATIZE = False
	# iterate wiki articles
	count = 0
	with open(outputPath, 'wb') as output:
		for article in wiki_corpus.get_texts():
			article = [HanziConv.toSimplified(text.decode('utf-8')) for text in article]
                        #import pdb
                        #pdb.set_trace()
			output.write((u' '.join(article)+ u'\n').encode('utf-8'))
			count = count + 1
			if count % 10000 == 0:
				logging.info("%d articles processed", count)



if __name__ == '__main__':
	if len(sys.argv) != 3:
		print ("please input a wiki xml dump file path and output path.")
		exit()
	# logging congiurationg
	logging.basicConfig(format='%(asctime)s: %(levelname)s : %(message)s', level = 1)
        # turn off lemmatization
        main(sys.argv[1], sys.argv[2])
