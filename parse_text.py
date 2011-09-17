import nltk, urllib

data = open('text','r').read()

tokens = nltk.word_tokenize(data)
text = nltk.Text(tokens)

suffixes = ['ing','s','ed','es','ly','ment']

def word_stem(word):
    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

def category_score(scores_hash, data):
    score = 0
    tokens = nltk.word_tokenize(data)
    for token in tokens:
        if scores_hash.has_key(word_stem(token.lower())):
            score = score + scores_hash[word_stem(token.lower())]
    return score

def post_termExtraction(context):
    params = urllib.urlencode(
        {'appid': 'HekkaB6s' ,
         'context': context,
         'output':'json'}
        )
    f = urllib.urlopen("http://search.yahooapis.com/ContentAnalysisService/V1/termExtraction", params)
    print f.read()
