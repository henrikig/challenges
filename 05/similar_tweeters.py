import sys
import nltk
import gensim

from spacy.lang.en import English

from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from gensim import corpora
import pickle

from usertweets import UserTweets


parser = English()


def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            continue
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens


def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma


def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)


# Create set of English stopwords for filtering
en_stop = set(nltk.corpus.stopwords.words('english'))


def prepare_text_for_lda(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 3]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens


def prepare_tweets(user):
    text_data = []
    for tw in user:
        tokens = prepare_text_for_lda(tw.text)
        text_data.append(tokens)
    return text_data


def old_tokenize(user):
    tokens = []
    for tw in user:
        tokens += word_tokenize(tw.text)
    to_remove = {".", ",", " ", "-", "@", "/", "https", ":", "(", ")", ";", "!", "?", "$"}
    to_remove.update(str(i) for i in range(10))
    tokens = [e for e in tokens if e not in to_remove and len(e) > 2]
    return tokens
    

# if __name__ == "__main__":
#     if len(sys.argv) < 3:
#         print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
#         sys.exit(1)
#
#     user1, user2 = sys.argv[1:3]
#     similar_tweeters(user1, user2)


user1 = UserTweets("bbelderbos")

tweets = prepare_tweets(user1)
dictionary = corpora.Dictionary(tweets)
corpus = [dictionary.doc2bow(text) for text in tweets]
# Flatten list of lists
corpus1 = [y for x in corpus for y in x]


pickle.dump(corpus, open('corpus.pkl', 'wb'))


NUM_TOPICS = 5
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)
print(ldamodel)

sims = gensim.similarities.Similarity('/usr/workdir/', ldamodel[corpus1], num_features=len(dictionary))



topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)