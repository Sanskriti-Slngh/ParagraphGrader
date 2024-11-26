import re
import nltk
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords
import enchant
import language_check
tool = language_check.LanguageTool('en-US')

otherStopWords = []
f = open('stopwords.txt','r')
for line in f.readlines():
    line = line.strip()
    otherStopWords.append(line)
f.close()

def getNumberOfSentences(x):
    return len(x)

def getNumberOfWordsInEachSentences(x):
    ans = []
    for sent in x:
        words = word_tokenize(sent)
        ans.append(len(words))
    return ans

def getNumberOfWords(x):
    filteredWords = []
    for sent in x:
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            if word not in stopwords.words('english'):
                if word not in otherStopWords:
                    filteredWords.append(word)
    return len(set(filteredWords))

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


def MisSpelledWords(x, verbose):
    MisSpelledWordCount = 0
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

def Grammar(data, verbose):
    data =re.sub('"','',data)
    text = data.encode('utf8', 'ignore')
    matches = tool.check(text)
    if verbose:
        for i in range(len(matches)):
            print matches[i]
    return len(matches)


def extractFeature(text, verbose):
    ans = []

    sentences = sent_tokenize(text)

    ans.append(getNumberOfSentences(sentences))

    n = sum(getNumberOfWordsInEachSentences(sentences))
    ans.append(n)

    ans.append(getNumberOfWords(sentences))

    n = 0
    for item in IsFirstLetterCapitalInEachSentence(sentences):
        if item == False:
            n = n+1

    ans.append(n)

    ans.append(MisSpelledWords(sentences, verbose))
    
    ans.append(Grammar(text, verbose))

    return ans                    
