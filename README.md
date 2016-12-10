# wikiEmbedding
1. download wiki dump
wget https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
2. install gensim
pip3 install --upgrade gensim
3. install jieba and hanziconv
pip3 install --upgrade jieba 
pip3 install --upgrade hanziconv
4. extract and fan2jian
python ./extract xml/file/path ./output.txt
5. segment
python ./jiebaSegmentation_noEn.py ./output.txt stopwords.txt wordsEn.txt output_seg.txt
6. train
python ./trainWord2Vec.py ./output_seg.txt embed256.bin
7. test
python ./testWord2Vec.py embed256.bin