import os
#import the module nltk
import nltk
#import this module for drawing graphs
import matplotlib
# Reader of NLTK to access our own text files and treat them as regular corpora
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
#This is the directory in which we can store our text file
corpusdir = 'newcorpus/'
#this will make the directory in the folder you are working.
if not os.path.isdir(corpusdir):
    os.mkdir(corpusdir)
#accesing the file which is inside the directory
newcorpus = PlaintextCorpusReader('newcorpus/', '.*')
#Now Let us perform some of the operation using Natural Language processing
#displaying the content of the file in the newcorpus which has been made
print(newcorpus.raw().strip())
#displaying the length of the words of the file which is inside the directory newcorpus
a=(len(newcorpus.words()))
print("This will tell me the words inside the file",a)
#displaying the length of the words of the file which is inside the directory newcorpus
b=(len(newcorpus.sents()))
print("This will tell me the sentence inside the file",b)
#calculating average words per sentence
aws= a/b;
print("This will give me average words per sentence",aws)
#**********************************************************************
words_dispalyed = newcorpus.words()
#This function will tell me the frequency distribution of each word in the text file
fre_dis = nltk.FreqDist(words_dispalyed)
#Let us plot each word and their frequency distribution using plot function.
fre_dis.plot(title="Frequency Distribution")
