# -*- coding: utf-8 -*-
'''
python version: 2.7

segment Chinese words
'''

import jieba
import logging

# start segmentation
def main(rawTextPath ,stopWordsPath, outputPath):
	# iterate wiki articles

	# make stop words dictionary
	stopWords = set()
	with open(stopWordsPath, 'rb') as f_sw:
		for line in f_sw:
			stopWords.add(line.strip().decode('utf-8'))

	# do the real segmentation work
	with open(outputPath, 'wb') as f_out:
		count = 0
		with open(rawTextPath, 'rb') as f_raw:
			for line in f_raw:
				words = jieba.cut(line.decode('utf-8'), cut_all = False)
				for word in words:
					if word notin stopWords:
						f_out.write((word+u' '.encode('utf-8')))
						count = count + 1
						if count % 10000 == 0:
						logging.info("%d words segmented", count)



if __name__ == '__main__':
	if len(sys.argv) != 4:
		print ("please input a raw text file path, stop words file path, and a output path.")
		exit()
	# logging congiurationg
	logging.basicConfig(format='%(asctime)s: %(levelname)s : %(message)s', level = 1)
        # turn off lemmatization
        main(sys.argv[1], sys.argv[2], sys.argv[3])





