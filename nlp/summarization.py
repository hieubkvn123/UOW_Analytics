from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

import enchant
import re

d = enchant.Dict("en_US")
def _create_frequency_table(text_string):
    text_string = text_string.lower()

    pattern = re.compile('\w+') # regex for words
    text_string_ = ''
    for char in text_string:
        if(pattern.match(char) or char == ' '):
            text_string_ += char

    # Removing all non-english words
    words = word_tokenize(text_string_)
    for word in words:
        if(not d.check(word)):
            words.remove(word)

    # Stop words removal and Stemming
    stopWords = stopwords.words("english")
    ps = PorterStemmer()

    freqTable = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    return freqTable

# This is probably wrong
def _score_sentences(sentences, freqTable):
    sentenceValue = dict()

    for sentence in sentences:
        word_count_in_sentence = len(word_tokenize(sentence)) # for fairness
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]

        sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]] / word_count_in_sentence

    return sentenceValue


def _find_average_score(sentenceValue) :
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    # Average value of a sentence from original text
    average = sumValues / len(sentenceValue)

    return average


def _generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentenceValue[sentence[:10]] > threshold:
            summary += " " + sentence
            sentence_count += 1

    return summary

def summarize(text):
    freq_table = _create_frequency_table(text)

    '''
    We already have a sentence tokenizer, so we just need
    to run the sent_tokenize() method to create the array of sentences.
    '''

    # 2 Tokenize the sentences
    sentences = sent_tokenize(text)

    # 3 Important Algorithm: score the sentences
    sentence_scores = _score_sentences(sentences, freq_table)

    # 4 Find the threshold
    threshold = _find_average_score(sentence_scores)

    # 5 Important Algorithm: Generate the summary
    summary = _generate_summary(sentences, sentence_scores, threshold)

    return summary
