# Frequency-distribution-plot-of-.txt-file-using-NLTK
## See the graph to know the vision of this code.
![image2](https://user-images.githubusercontent.com/3431730/43183780-f1859480-9003-11e8-90c2-d6fb1d3e5cb9.png)

---

### Elaboration  of vison of this code

If you look at thetext file, you can count manually number of times each word appears in the text file. I have used only 3- 4 lines file to make you do operation manually also. Same is done using nltk and matlibplot programmatically
Please see the lines in the txt file below
```
1. Which of the following led to the introduction of English Education in India?
1. Charter Act of 1813
2. General committee of Public Instruction 1823
3. Orientalist and Anglicist Controversy
```

---

### How a new corpus is created by me to count the occurence of each words in the text file
I have used PlaintextCorpusReader to read the text file and then created a directory where I Kept my txt file. Please see the following code to create your own corpus
```
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
#This is the directory in which we can store our text file
corpusdir = 'newcorpus/'
#this will make the directory in the folder you are working.
if not os.path.isdir(corpusdir):
    os.mkdir(corpusdir)
#accesing the file which is inside the directory
newcorpus = PlaintextCorpusReader('newcorpus/', '.*')
```
#### How to run the code
Download the files and run the file. 
```
python Frequency_Distribution_plot.py
```
If you want to create another name of your corpus where you want to keep your .txt file, you may modify this line of code
```
corpusdir = 'newcorpus/  #Please write the other name which you wish to rename.
```
