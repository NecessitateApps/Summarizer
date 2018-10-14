# from sumy.parsers.plaintext import PlaintextParser
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

url = 'https://www.cnn.com/2018/10/10/politics/steele-dossier-letter/index.html'
parser = HtmlParser.from_url(url, Tokenizer("english"))
summarizer = LexRankSummarizer()

summary = summarizer(parser.document, 3)

for sentence in summary:
    print(sentence)


# from lexrank import STOPWORDS, LexRank
# from pathlib import Path
#
# documents = []
# directory = Path('bbc/politics')
#
# for file_path in directory.glob('*.txt'):
#     with file_path.open(mode='rt', encoding='utf-8') as fp:
#         documents.append(fp.readlines())
# print(documents)
# lxr = LexRank(documents, stopwords=STOPWORDS['en'])
#
# sentences = [
#     'One of David Cameron\'s closest friends and Conservative allies, '
#     'George Osborne rose rapidly after becoming MP for Tatton in 2001.',
#
#     'Michael Howard promoted him from shadow chief secretary to the '
#     'Treasury to shadow chancellor in May 2005, at the age of 34.',
#
#     'Mr Osborne took a key role in the election campaign and has been at '
#     'the forefront of the debate on how to deal with the recession and '
#     'the UK\'s spending deficit.',
#
#     'Even before Mr Cameron became leader the two were being likened to '
#     'Labour\'s Blair/Brown duo. The two have emulated them by becoming '
#     'prime minister and chancellor, but will want to avoid the spats.',
#
#     'Before entering Parliament, he was a special adviser in the '
#     'agriculture department when the Tories were in government and later '
#     'served as political secretary to William Hague.',
#
#     'The BBC understands that as chancellor, Mr Osborne, along with the '
#     'Treasury will retain responsibility for overseeing banks and '
#     'financial regulation.',
#
#     'Mr Osborne said the coalition government was planning to change the '
#     'tax system \"to make it fairer for people on low and middle '
#     'incomes\", and undertake \"long-term structural reform\" of the '
#     'banking sector, education and the welfare state.',
# ]
#
# summary_cont = lxr.get_summary(sentences, threshold=None)
# print(summary_cont)