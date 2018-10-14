from gensim.summarization import keywords
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import nltk
from goose3 import Goose
import heapq
def summarize():
    url = input('URL here:')
    g = Goose()
    article = g.extract(url=url)
    clean = article.cleaned_text
    stopword = set(stopwords.words("english"))
    sentence_list = nltk.sent_tokenize(clean)

    word_frequencies = {}
    for word in nltk.word_tokenize(clean):
        if word not in stopword:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    summary_sentences = heapq.nlargest(4, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    print('Summary:', summary)

def get_topic():
    url = input("URL here:")
    g = Goose()
    article = g.extract(url=url)
    title = article.title.upper()
    clean = article.cleaned_text
    rando = '’' + 'The' + '”' +'“' +'Â' + 'â'
    clean_lower = clean.lower()

    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(clean)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = ""
    for w in word_tokens:
        if w not in stop_words and w not in string.punctuation and w not in rando:
            filtered_sentence += (str(w) + " ")
    final_count_words = Counter(filtered_sentence.split())
    print(final_count_words)
summarize()
