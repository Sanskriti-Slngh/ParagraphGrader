# We are using nltk library.
import nltk
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords
import enchant
import re
import language_check
tool = language_check.LanguageTool('en-US')

otherStopWords = []
f = open('stopwords.txt', 'r')
for line in f.readlines():
    line = line.strip()
    otherStopWords.append(line)
f.close()

#fin = open('checkData.txt', 'r')
#data = fin.read()
#print data
#fin.close()

## define a function that finds out number of sentences in data
## Input is sentnces from sent_tokenize
def getNumberOfSentences(x):
    return len(x)

## number of words in each sentence
def getNumberOfWordsInEachSentences(x):
    # list that contains number of words in each sentence
    ans = []
    for sent in x:
        words = word_tokenize(sent)
        ans.append(len(words))
    return ans

## number of unique words in paragraph
def getNumberOfWords(x):
    # list that contains number of words in each sentence
    filteredWords = []
    for sent in x:
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            if word not in stopwords.words('english'):
                if word not in otherStopWords:
                    filteredWords.append(word)
    return len(set(filteredWords))

## Check capitalization of first letter in first word
def IsFirstLetterCapitalInEachSentence(x):
    ans = []
    for sent in x:
        words = word_tokenize(sent)
        firstWord = words[0]
        firstLetter = firstWord[0]
        if firstLetter.upper() == firstLetter:
            ans.append(True)
        else:
            ans.append(False)

    return ans


## 
#sentences = sent_tokenize(Data)

#print getNumberOfSentences(sentences)
#print getNumberOfWordsInEachSentences(sentences)
#print IsFirstLetterCapitalInEachSentence(sentences)

def MisSpelledWords(x, verbose):
    misSpelledWordCount = 0
    d = enchant.Dict('en_US')
    for sent in x:
        words = word_tokenize(sent)
        for item in words:
            if re.match('!',item) or \
                re.match('"', item) or \
                re.match("''", item) or \
                re.match(",", item) or \
                re.match("``", item) or \
                re.match("'", item) or \
                re.match(";", item) or \
                re.match("\?", item) or \
                re.match("\$", item) or \
                re.match("\&", item) or \
                re.match("\-", item) or \
                re.match("\+", item) or \
                re.match("#", item) or \
                re.match("%",  item) or \
                re.match("\[]", item) or \
                re.match("\/", item) or \
                re.match("\:", item):
                continue
            d.check(item)
            if d.check(item) == False:
                if verbose > 0:
                    print "misspelled word " + item
                misSpelledWordCount = misSpelledWordCount + 1
    return misSpelledWordCount

#print MisSpelledWords(sentences)

def Grammar(data, verbose):
    data = re.sub('"','', data)
    text = data.encode('utf8','ignore')
    matches = tool.check(text)
    if verbose:
        for i in range(len(matches)):
            print matches[i]
    return len(matches)
    
#Grammar(data)

## extract features given a text paragraph
## returns a list of values of features like
## [2 43 4 4]
def extractFeature(text, verbose):
    ans = []
    # break into sentences using nltk sent_tokenize
    sentences = sent_tokenize(text)

    # first feature is number of sentences
    ans.append(getNumberOfSentences(sentences))

    # total number of words
    n = sum(getNumberOfWordsInEachSentences(sentences))
    ans.append(n)

    # number of unique words
    ans.append(getNumberOfWords(sentences))

    # count of false capitallization
    n = 0
    for item in IsFirstLetterCapitalInEachSentence(sentences):
        if item == False:
            n = n+1

    ans.append(n)

    # mis-spelled word count
    ans.append(MisSpelledWords(sentences, verbose))
    

    # grammar mistakes
    ans.append(Grammar(text, verbose))

    return ans

    

    
