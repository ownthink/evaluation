import os
import sys
import time
from utils import Segment, Report

def seg_test(seg, name, test_set):
	start = time.time()
	fin = open('data/test_%s.txt'%test_set, 'r', encoding='utf8')
	fout = open('result/%s.%s'%(test_set, name), 'w', encoding='utf8')
	for index, line in enumerate(fin):
		line = line.strip()
		if line == '':
			fout.write('\n')
		else:
			words = getattr(seg, name)(line)
			if type(words[0])==list:
				words = words[0]
			fout.write(' '.join(words) + '\n')
	fin.close()
	fout.close()
	
	end = time.time() - start
	
	print(name + ' time：\t' , end)


def test_value(name, test_set):
	report = Report()
	
	fref = open('data/%s.txt'%test_set, 'r', encoding='utf8')
	fcan = open('result/%s.%s'%(test_set, name), 'r', encoding='utf8')
	reference_all = fref.readlines()
	candidate_all = fcan.readlines()
	fref.close()
	fcan.close()
	
	ref_count = 0
	can_count = 0
	acc_count = 0
	for reference, candidate in zip(reference_all, candidate_all):
		reference = reference.strip()
		candidate = candidate.strip()

		ref_words_len, can_words_len, acc_word_len = report.compare_line(reference, candidate)
		ref_count += ref_words_len
		can_count += can_words_len
		acc_count += acc_word_len
	
	P = acc_count / ref_count * 100
	R = acc_count / can_count * 100
	F1 = (2 * P * R) / (P+R)
	
	print(name)
	print('准确率', P)
	print('召回率', R)
	print('F1', F1)
	print()
	
	
if __name__=='__main__':
	seg = Segment()
	
	tools = ['jieba', 'hanlp', 'snownlp', 'foolnltk', 'jiagu', 'pyltp', 'thulac', 'pynlpir']

	print('msr test...')
	for cur in tools:
		seg_test(seg, cur, 'msr')

	print()
	
	print('pku test...')
	for cur in tools:
		seg_test(seg, cur, 'pku')
		
	print()
	print('other test...')
	for cur in tools:
		seg_test(seg, cur, 'other')
		
	print('-----------------------------------')

	print('msr value...')
	for cur in tools:
		test_value(cur, 'msr')
	
	print('pku value...')
	for cur in tools:
		test_value(cur, 'pku')
		
	print('other value...')
	for cur in tools:
		test_value(cur, 'other')
		
		
		