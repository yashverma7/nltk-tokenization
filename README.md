# nltk-tokenization

Natural Language Processing (NLP) is a subfield of computer science, artificial intelligence,
information engineering, and human-computer interaction. This field focuses on how to program
computers to process and analyze large amounts of natural language data. It is difficult to perform 
as the process of reading and understanding languages is far more complex than it seems at first glance. Tokenization is the process of tokenizing or 
splitting a string, text into a list of tokens. One can think of token as parts like a word is a token in a sentence, and a sentence is a token in a paragraph.

# types of tokenization

1.Sentence Tokenization – Splitting sentences in the paragraph
How sent_tokenize works ? The sent_tokenize function uses an instance of PunktSentenceTokenizer from the nltk.tokenize.punkt module, 
which is already been trained and thus very well knows to mark the end and beginning of sentence at what characters and punctuation.

2.PunktSentenceTokenizer – When we have huge chunks of data then it is efficient to use it.

3.Tokenize sentence of different language – One can also tokenize sentence from different languages using different pickle file other than English.

4.Word Tokenization – Splitting words in a sentence.
How word_tokenize works? word_tokenize() function is a wrapper function that calls tokenize() on an instance of the TreebankWordTokenizer class.

5.Using TreebankWordTokenizer These tokenizers work by separating the words using punctuation and spaces. And as mentioned in the code outputs above, 
it does not discard the punctuation, allowing a user to decide what to do with the punctuations at the time of pre-processing.

6.WordPunctTokenizer – It seperates the punctuation from the words.

7.Using Regular Expression

8.Twitter-aware tokenizer, Is designed to be flexible and easy to adapt to new domains and tasks.
Because there are many popular Twitter language and very colloquial things,I think it is vary useful for analyzing data from Twitter.
And one of the most interesting features of TweetTokenizer is parameter of reduce_len parameters
which is to replace repeated character sequences of length 3 or greater
with sequences of length 3 and parameter of remove_handles which is to remove Twitter username handles from text.

9.SExprTokenizer
It divides the string into tokens based on parenthesized expressions and whitespace. 
When there are non-matching parentheses there will be a „valueerror‟ exception. 
The “strict" argument can be set to False to allow for non-matching parentheses.
