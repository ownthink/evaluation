import jieba
import pyltp
import jiagu
import pyhanlp
import thulac	
import pynlpir
import snownlp
import fool
	
class Segment:
	def __init__(self):
		jieba.initialize()
		self.ltpseg = pyltp.Segmentor()
		self.ltpseg.load('model/ltp_data_v3.4.0/cws.model')
		self.thu1 = thulac.thulac(seg_only=True)
		pynlpir.open()
		
	def __del__(self):
		pynlpir.close()
		
	def jiagu(self, text):
		# 甲骨分词
		jiagu_result = jiagu.seg(text)
		return jiagu_result
		
	def jieba(self, text):
		# 结巴分词
		jieba_result = list(jieba.cut(text))
		return jieba_result
		
	def pyltp(self, text):
		# 哈工大LTP
		pyltp_result = self.ltpseg.segment(text)
		return pyltp_result
		
	def hanlp(self, text):
		# HanLP
		pyhanlp_result = []
		for term in pyhanlp.HanLP.segment(text):
			pyhanlp_result.append(term.word)
		return pyhanlp_result
		
	def thulac(self, text):
		# 清华分词
		thulac_result = self.thu1.cut(text, text=True).split()
		return thulac_result
	
	def pynlpir(self, text):
		# NLPIR
		pynlpir_result = pynlpir.segment(text, pos_tagging=False)
		return pynlpir_result
		
	def snownlp(self, text):
		# SnowNLP
		snownlp_result = snownlp.SnowNLP(text).words
		return snownlp_result
		
	def foolnltk(self, text):
		# FoolNLTK
		fool_result = fool.cut(text)
		return fool_result
		
class Report:
	def __init__(self):
		pass
		
	def compare_line(self, reference, candidate): # reference 标注
		ref_len = len(reference.replace(' ', ''))
		can_len = len(candidate.replace(' ', ''))
		
		# if ref_len != can_len:
			# print('error len')
			# return None
		
		ref_words = reference.split()
		can_words = candidate.split()
		
		ref_words_len = len(ref_words)
		can_words_len = len(can_words)
		
		ref_index = []
		index = 0
		for word in ref_words:
			word_index = [index]
			index += len(word)
			word_index.append(index)
			ref_index.append(word_index)
			
		can_index = []
		index = 0
		for word in can_words:
			word_index = [index]
			index += len(word)
			word_index.append(index)
			can_index.append(word_index)
			
		tmp = [val for val in ref_index if val in can_index]
		acc_word_len = len(tmp)
		
		return ref_words_len, can_words_len, acc_word_len
		
		
if __name__=='__main__':
	# seg = Segment()
	# text = '你好啊'
	# print(seg.foolnltk(text))
	
	report = Report()
	
	reference = '你 只有 槽'
	candidate = '你 只 有 槽'
	
	
	
	
	report.compare_line(reference, candidate)
	
	
	
	tools = ['jieba', 'hanlp', 'snownlp', 'foolnltk', 'jiagu', 'pyltp', 'thulac', 'pynlpir']
	
	
	
	
	

