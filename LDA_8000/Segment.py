#encoding=utf-8

import jieba
import codecs

class Seg(object):
    stopwords = []
    stopword_filepath="stopwordList//stopword.txt"

    def __init__(self):
        self.read_in_stopword()
		
	# 读入停用词
    def read_in_stopword(self):
        file_obj = codecs.open(self.stopword_filepath,'r','utf-8')
        while True:
            line = file_obj.readline()
            line=line.strip('\r\n')
            if not line:
                break
            self.stopwords.append(line)
        file_obj.close()
	
	# jieba分词 精确模式 去除停用词
    def cut(self,sentence,stopword=True):
        seg_list = jieba.cut(sentence)

        results = []
        for seg in seg_list:
            if seg in self.stopwords and stopword:
                continue
            results.append(seg)

        return results
	
	# jieba分词 搜索引擎模式 去除停用词
    def cut_for_search(self,sentence,stopword=True):
        seg_list = jieba.cut_for_search(sentence)

        results = []
        for seg in seg_list:
            if seg in self.stopwords and stopword:
                continue
            results.append(seg)

        return results