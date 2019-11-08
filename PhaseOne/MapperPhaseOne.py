#!/usr/bin/env python 
from string import punctuation
import sys

# TF-IDF computation: Phase One
# Mapper output: <<word, document_name>   1>
stopwords= ['a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by',
            'can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers',
            'him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my',
            'neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so',
            'some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what',
            'when','where','which','while','who','whom','why','will','with','would','yet','you','your'];
for line in sys.stdin:
    line = line.translate(None, punctuation).strip('\t')
    line_contents = line.split(" ")
    doc_name = line_contents[0]
    line_contents.remove(doc_name)
    for content in line_contents:
      content = content.rstrip()
      if content not in stopwords:
      
        key = content + "," + doc_name
        print '%s\t%s' % (key, 1)