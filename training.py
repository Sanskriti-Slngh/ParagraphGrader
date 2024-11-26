# import feature extractor

from featureExtractor import extractFeature
import re
import codecs
import numpy as np
from sklearn import linear_model
from sklearn import svm
import pickle

# first read training file
fin = codecs.open('../data/trainingData.txt', 'r', 'utf-8')
ruleBasedGrade = 0
# understand the data and read
# indvidual paragraph and their grade.

inParagraph = 0
inText = 0
GradeLine = 0
text = ""
para_id = 0

# store points
X = []
Y = []


for line in fin.readlines():
    line = line.strip()

    # if line is blanck just skip
    # ^ beginning
    # $ end
    if re.match('^\s*$', line):
        continue

    line = line.encode('ascii', 'ignore')
    # check for start of paragraph
    if re.match(u'<paragraph>', line):
        inParagraph = 1
        continue

    # check for end of paragraph
    if re.match('</paragraph>', line):
        inParagraph = 0
        print 'Extracting features from paragraph %s' %(para_id)
        para_id = para_id + 1
        #print "Got pargraph as %s" %(text)
        #print "Grade is %s" %(grade)
        features =  extractFeature(text, 0)
        X.append(features)
        print 'paragraph id is ' + str(id)
        print features
        print grade
        # 10 marks for each sentence
        # 1 for number of words
        # 5 marks for each unique word
        # -10 for missing capitalzation
        # -5 for spelling mistakes
        # -5 for grammar
        # A good paragraph should have 5-20 lines.
        # -100 penality for paragraph larger than 20
        # maximum score for good paragraph:
        # 20*10+2*200  = 600
        # grading as:
        # score < 0: 0
        # score > 400: 10
        # grade = int(score/50).
    
        score = features[0]*10 + features[1]*1 + \
                features[2]*5 - \
                features[3]*10 - features[4]*5 - features[5]*5
        if features[0] > 30:
            score -= 100

        calculated_grade = 0
        if score > 500:
            calculated_grade = 10
        elif score < 0:
            calculated_grade = 0
        else:
            calculated_grade = int(score/50)
                
        print 'calculated score %s, grade %s' %(score, calculated_grade)
        if grade != calculated_grade:
            print 'MISMATCH: '

        if ruleBasedGrade:
            Y.append(calculated_grade)
        else:
            Y.append(grade)
        text = ""
        continue

    # check start of text
    if re.match('<text>', line):
        inText = 1
        continue

    # check end of text
    if re.match('</text>', line):
        inText = 0
        continue

    # grade line
    if re.match('<grade>([0-9]+)</grade>', line):
        a = re.match('<grade>([0-9]+)</grade>', line)
        grade = int(a.group(1))
        continue

    # id line
    if re.match('<id>([0-9]+)</id>', line):
        a = re.match('<id>([0-9]+)</id>', line)
        id = int(a.group(1))
        continue
    
    # Collect text
    if inText:
        text += line
        continue

    # error
    print inParagraph
    print "Unknown line " + line
    exit()
    


fin.close()

## fit the data
clf = linear_model.SGDClassifier(loss='log', n_iter=1000)
clf.fit(np.array(X), np.array(Y))
#clf = svm.SVC()
#clf.fit(X, Y)
print clf.coef_

# save the weights
clfFile = open('clf.object', 'wb')
pickle.dump(clf, clfFile)

# calculate error
loss = 0.0
wrongCounts = 0
for i in range(len(Y)):
    predicted_y = clf.predict([X[i]])
    if predicted_y != Y[i]:
        loss += (Y[i] - predicted_y) ** 2
        print '%s: predicted %s, actual %s' %(i, predicted_y, Y[i])
        wrongCounts += 1


print 'Total Loss is %s' %(loss)
print 'Number of paragraphs wrong %s' %(wrongCounts)

