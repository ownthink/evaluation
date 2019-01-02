import jieba
import pyltp
import jiagu
import pyhanlp
import thulac	
import pynlpir
import snownlp
import fool

# https://www.zhihu.com/question/19578687/answer/15607602
sentence = [
	"柳奶奶和牛奶奶泼牛奶吓坏了刘奶奶，大骂再也不买柳奶奶和牛奶奶的牛奶。",
	"工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作",
	"工信處女幹事每月經過下屬科室都要親口交代24口交換機等技術性器件的安裝工作"
]
	
class Test:
	def __init__(self):
		jieba.initialize()
		self.ltpseg = pyltp.Segmentor()
		self.ltpseg.load('model/ltp_data_v3.4.0/cws.model')
		jiagu.init()
		self.thu1 = thulac.thulac(seg_only=True)
		pynlpir.open()
		
	def __del__(self):
		pynlpir.close()
		
	def test_seg(self):
		# 甲骨分词
		jiagu_result = []
		for sen in sentence:
			jiagu_result.append(jiagu.seg(sen))

		# 结巴分词
		jieba_result = []
		for sen in sentence:
			jieba_result.append(jieba.cut(sen))
		
		# 哈工大LTP
		pyltp_result = []
		for sen in sentence:
			pyltp_result.append(self.ltpseg.segment(sen))
			
		# HanLP
		pyhanlp_result = []
		for sen in sentence:
			words = []
			for term in pyhanlp.HanLP.segment(sen):
				words.append(term.word)
			pyhanlp_result.append(words)
		
		# 清华分词
		thulac_result = []
		for sen in sentence:
			thulac_result.append(self.thu1.cut(sen, text=True).split())
			
		# NLPIR
		pynlpir_result = []
		for sen in sentence:
			pynlpir_result.append(pynlpir.segment(sen, pos_tagging=False))
			
		# SnowNLP
		snownlp_result = []
		for sen in sentence:
			snownlp_result.append(snownlp.SnowNLP(sen).words)
			
		# FoolNLTK
		fool_result = fool.cut(sentence)

		for sen, jgr, jbr, ltp, hanlp, thu, nlpir, snow, fnltk, in zip(sentence, jiagu_result,
					jieba_result, pyltp_result, pyhanlp_result,
					thulac_result, pynlpir_result, snownlp_result, fool_result):
			print('句子：\t\t' + sen + '\n')
			print('结巴：\t\t' + ' '.join(jbr))
			print('HanLP：\t\t' + ' '.join(hanlp))
			print('SnowNLP\t\t' + ' '.join(snow))
			print('FoolNLTK\t' + ' '.join(fnltk))
			print('甲骨：\t\t' + ' '.join(jgr))
			print('哈工大：\t' + ' '.join(ltp))
			print('清华：\t\t' + ' '.join(thu))
			print('NLPIR：\t\t' + ' '.join(nlpir))
			print('\n')
		
if __name__=='__main__':
	test = Test()
	
	test.test_seg()
	
	







