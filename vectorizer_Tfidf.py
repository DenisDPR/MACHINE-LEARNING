
from sklearn.feature_extraction.text import TfidfVectorizer

# create instance of TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words = 'english')
word_data_transformed = vectorizer.fit_transform(word_data)

# fit vectorizer instance of TfidfVectorizer
vectorizer.fit_transform(word_data)
# call attributes of fitted vectorizer
vocab_list = vectorizer.get_feature_names()


print len(vocab_list)
#what is word 34597
print vocab_list[34597]
