Statistical language modeling(maximum-likelihood-estimate)
In this problem, you will explore some simple statistical models of English text. Download and examine the data files on Piazza for this assignment. (Start with the readme.txt file.) These files contain unigram and bigram counts for 500 frequently occurring tokens in English text. These tokens include actual words as well as punctuation symbols and other textual markers. In addition, an “unknown” token is used to represent all words that occur outside this basic vocabulary.


The data files for homework 3 are:

  vocab.txt
  unigram.txt
  bigram.txt
  
The file vocab.txt contains a list of 500 tokens, corresponding to words, punctuation symbols, and other textual markers.

The file unigram.txt contains the counts of each of these tokens in a large text corpus of Wall Street Journal articles.  The corpus consisted of roughly 3 million sentences.

The file bigram.txt contains the counts of pairs of adjacent words in this same corpus.  Let count(w1,w2) denote the number of times that word w1 is followed by word w2.  The counts are stored in a simple three column format: 

  index(w1)  index(w2)  count(w1,w2)


