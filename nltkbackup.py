import nltk
import random
from nltk.tokenize import sent_tokenize, word_tokenize,PunktSentenceTokenizer
from nltk.corpus import qc, movie_reviews
import pickle



documents = []
                                                                   for category in movie_reviews.categories():
     for fileid in movie_reviews.fileids(category):
         documents.append((list(movie_reviews.words(fileid)),category))
random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)


word_features = list(all_words.keys())[:189]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features



featuresets = [(find_features(rev), category) for (rev, category) in documents]


training_set= featuresets[:75]
testing_set= featuresets[75:]

reviewList = []
for feature in testing_set:
     (review,cat) = feature
     reviewList.append(review)




classifier = nltk.NaiveBayesClassifier.train(training_set)

print((classifier.classify_many(reviewList)))


##classifier_f = open("naivebayes.pickle","rb")
##classifier = pickle.load(classifier_f)
##classifier_f.close()



print("Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

##save_classifier = open("naivebayes.pickle","wb")
##pickle.dump(classifier,save_classifier)
##save_classifier.close()


