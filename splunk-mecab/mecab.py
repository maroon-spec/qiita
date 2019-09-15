# -*- coding: utf-8 -*-
import splunk.Intersplunk
import sys
import MeCab

results, dummyresults, settings = splunk.Intersplunk.getOrganizedResults()
m = MeCab.Tagger("-Owakati")
#print(m.parse ("今日は晴天なり"))

for result in results:
    word = m.parse(result['text'])
    result['mecab'] = word
