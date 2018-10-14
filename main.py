from flask import Flask, jsonify, request
import requests
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from gensim.summarization import keywords
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import nltk
from goose3 import Goose
import heapq

app = Flask(__name__)

def summarize(url):
    g = Goose()
    article = g.extract(url=url)
    clean = article.cleaned_text
    stopword_set = set(stopwords.words("english"))
    sentence_list = nltk.sent_tokenize(clean)

    word_frequencies = {}
    for word in nltk.word_tokenize(clean):
        if word not in stopword_set:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
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

    return summary
    # print('Summary:', summary)

def get_topic(url):
    g = Goose()
    article = g.extract(url=url)
    clean = article.cleaned_text
    rando = '’' + 'The' + '”' +'“' +'Â' + 'â'

    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(clean)
    filtered_sentence = ""
    for w in word_tokens:
        if w not in stop_words and w not in string.punctuation and w not in rando:
            filtered_sentence += (str(w) + " ")
    final_count_words = Counter(filtered_sentence.split())
    assorted_values = sorted(final_count_words.items(), key=lambda x: x[1], reverse=True)
    print(assorted_values)
    topic = assorted_values[0][0]

    return topic
    # print(final_count_words)


def make_json():
    url_req = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=4447d852b5264e1dab136e3f15d4089c')
    url_dict = url_req.json()
    final_dict = {}
    final_dict['articles'] = []

    for i in range(10):
        temp_dict = {}
        article_dict = url_dict['articles'][i]

        url = article_dict['url']

        temp_dict['title'] = article_dict['title']
        temp_dict['topic'] = get_topic(url)
        temp_dict['url'] = url
        temp_dict['summary'] = summarize(url)

        publisher = article_dict['source']['name']
        if "." in publisher:
            publisher = publisher.split('.')[0]

        temp_dict['image'] = article_dict['urlToImage']
        temp_dict['source'] = publisher

        final_dict['articles'].append(temp_dict)

    return final_dict

make_json()
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         some_json = request.get_json()
#         return jsonify({'you sent': some_json}), 201
#     else:
#         finished_dict = make_json()
#         return jsonify(finished_dict)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
