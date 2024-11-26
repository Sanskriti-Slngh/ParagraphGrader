# import libararies
from featureExtractor import extractFeature

import re
import codecs
import numpy as np
from sklearn import linear_model
import pickle
import os.path
import language_check
tool = language_check.LanguageTool('en-US')

fin = codecs.open('../data/checkData.txt', 'r', "utf-8")
data = fin.read()
#for line in fin.readlines():
#    line = line.strip()
#    data += line.encode('utf-8', 'ignore')

fin.close()

# classifier
if os.path.isfile('clf.object'):
    infile = open('clf.object', 'rb')
    clf = pickle.load(infile)
    infile.close()
    print data
    features =  extractFeature(data.encode('utf-8'), 1)
    print features
    grade = clf.predict([features])
    score = features[0]*10 + features[1]*1 + \
            features[2]*5 - \
            features[3]*10 - features[4]*5 - features[5]*5
    if score > 600:
       ruleBasedGrade  = 10
    elif score < 0:
        ruleBasedGrade = 0
    else:
        ruleBasedGrade = int(score/50)
    print '********************************'
    print 'You earned grade of %d' %(grade)
    print 'Rule based score is %d and grade is %s' %(score, ruleBasedGrade)
    print '********************************'
    #print Grammar(data)

else:
    print 'Run training first'
    exit()
   
