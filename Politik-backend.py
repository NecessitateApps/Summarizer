from flask import Flask, jsonify, request
import requests
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

app = Flask(__name__)

def make_json():
    url = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=4447d852b5264e1dab136e3f15d4089c')
    url_dict = url.json()
    final_dict ={}
    final_dict['articles'] = []

    for i in range(10):
        temp_dict = {}
        article_dict = url_dict['articles'][i]
        temp_dict['title'] = article_dict['title']
        temp_dict['url'] = article_dict['url']

        parser = HtmlParser.from_url(temp_dict['url'], Tokenizer("english"))
        summarizer = LexRankSummarizer()

        summary = summarizer(parser.document, 3)

        summary_str = ''

        for line in summary:
            # print(line)
            summary_str += (str(line) + ' ')

        # print(summary_str)

        temp_dict['summary'] = summary_str[:-1]

        publisher = article_dict['source']['name']
        if "." in publisher:
            publisher = publisher.split('.')[0]


        temp_dict['image'] = article_dict['urlToImage'] #if there is no image put a generic one ya
        temp_dict['source'] = publisher

        final_dict['articles'].append(temp_dict)


    return final_dict

# print(make_json())

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent': some_json}), 201
    else:
        dict = make_json()
        return jsonify(dict)



if __name__ =='__main__':
    app.run(debug=True)
