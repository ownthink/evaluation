# 常用分词工具使用教程
>>> 以下分词工具均能在Python环境中直接调用（排名不分先后）。

* jieba（结巴分词）                                      免费使用
* HanLP（汉语言处理包）                           免费使用
* SnowNLP（中文的类库）                          免费使用
* FoolNLTK（中文处理工具包）                  免费使用
* Jiagu（甲骨NLP）                                      免费使用
* pyltp（哈工大语言云）                              商用需要付费
* THULAC（清华中文词法分析工具包）     商用需要付费
* NLPIR（汉语分词系统）                             付费使用

---
### jieba（结巴分词）
>>> “结巴”中文分词：做最好的 Python 中文分词组件。

项目Github地址：[jieba](https://github.com/fxsjy/jieba)

安装：
```shell
pip install jieba
```

使用：
```python
import jieba

jieba.initialize()

text = '化妆和服装'

words = jieba.cut(text)

words = list(words)

print(words)
```

### HanLP（汉语言处理包）
>>> HanLP是一系列模型与算法组成的NLP工具包，由大快搜索主导并完全开源，目标是普及自然语言处理在生产环境中的应用。HanLP具备功能完善、性能高效、架构清晰、语料时新、可自定义的特点。

项目Github地址：[pyhanlp](https://github.com/hankcs/pyhanlp)

安装：
```shell
pip install pyhanlp
```

使用：
```python
import pyhanlp

text = '化妆和服装'

words = []
for term in pyhanlp.HanLP.segment(text):
	words.append(term.word)

print(words)
```

### SnowNLP（中文的类库）
>>> SnowNLP是一个python写的类库，可以方便的处理中文文本内容，是受到了TextBlob的启发而写的，由于现在大部分的自然语言处理库基本都是针对英文的，于是写了一个方便处理中文的类库，并且和TextBlob不同的是，这里没有用NLTK，所有的算法都是自己实现的，并且自带了一些训练好的字典。

项目Github地址：[snownlp](https://github.com/isnowfy/snownlp)

安装：
```shell
pip install snownlp
```

使用：
```python
import snownlp

text = '化妆和服装'

words = snownlp.SnowNLP(text).words

print(words)
```

### FoolNLTK（中文处理工具包）
>>> 可能不是最快的开源中文分词，但很可能是最准的开源中文分词。

项目Github地址：[FoolNLTK](https://github.com/rockyzhengwu/FoolNLTK)

安装：
```shell
pip install foolnltk
```

使用：
```python
import fool

text = '化妆和服装'

words = fool.cut(text)

print(words)
```

### Jiagu（甲骨NLP）
>>> 基于BiLSTM模型，使用大规模语料训练而成。将提供中文分词、词性标注、命名实体识别、关键词抽取、文本摘要、新词发现等常用自然语言处理功能。参考了各大工具优缺点制作，将Jiagu回馈给大家。

项目Github地址：[jiagu](https://github.com/ownthink/Jiagu)

安装：
```shell
pip3 install jiagu
```

使用：
```python
import jiagu

jiagu.init()

text = '化妆和服装'

words = jiagu.seg(text)

print(words)
```

### pyltp（哈工大语言云）
>>> pyltp 是 LTP 的 Python 封装，提供了分词，词性标注，命名实体识别，依存句法分析，语义角色标注的功能。

项目Github地址：[pyltp](https://github.com/HIT-SCIR/pyltp)，3.4模型下载链接：[网盘](https://pan.baidu.com/share/link?shareid=1988562907&uk=2738088569#list/path=%2F)

安装：
```shell
pip install pyltp
```

使用：
```python
import pyltp

segmentor = pyltp.Segmentor()
segmentor.load('model/ltp_data_v3.4.0/cws.model') # 模型放置的路径

text = '化妆和服装'

words = segmentor.segment(text)

words = list(words)

print(words)
```

### THULAC（清华中文词法分析工具包）
>>> THULAC（THU Lexical Analyzer for Chinese）由清华大学自然语言处理与社会人文计算实验室研制推出的一套中文词法分析工具包，具有中文分词和词性标注功能。

项目Github地址：[THULAC-Python](https://github.com/thunlp/THULAC-Python)

安装：
```shell
pip install thulac
```

使用：
```python
import thulac

thu = thulac.thulac(seg_only=True)

text = '化妆和服装'

words = thu.cut(text, text=True).split()

print(words)
```

### NLPIR（汉语分词系统）
>>> 主要功能包括中文分词；英文分词；词性标注；命名实体识别；新词识别；关键词提取；支持用户专业词典与微博分析。NLPIR系统支持多种编码、多种操作系统、多种开发语言与平台。

项目Github地址：[pynlpir](https://github.com/tsroten/pynlpir)

安装：
```shell
pip install pynlpir
```
下载证书覆盖到安装目录，[NLPIR.user](https://github.com/NLPIR-team/NLPIR/blob/master/License/license%20for%20a%20month/NLPIR-ICTCLAS%E5%88%86%E8%AF%8D%E7%B3%BB%E7%BB%9F%E6%8E%88%E6%9D%83/NLPIR.user)
例如安装目录：/usr/lib64/python3.4/site-packages/pynlpir/Data

使用：
```python
import pynlpir

pynlpir.open()

text = '化妆和服装'

words = pynlpir.segment(text, pos_tagging=False)

print(words)

pynlpir.close()
```


