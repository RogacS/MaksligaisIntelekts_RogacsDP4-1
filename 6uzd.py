import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import heapq

text = "Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm."
stop_words = [
    "ir", "tās", "un", "ar", "vai", "kā", "kas", "tā", "tai", "par", "no", "pie", "mēs", "bija", "tai", "vai", "viņš", "viņa"
]

sentences = sent_tokenize(text)

words = word_tokenize(text.lower())
filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

vectorizer = TfidfVectorizer(stop_words=stop_words)
tfidf_matrix = vectorizer.fit_transform([' '.join(filtered_words)])

sentence_scores = {}
for i, sentence in enumerate(sentences):
    sentence_words = word_tokenize(sentence.lower())
    score = 0
    for word in sentence_words:
        if word in vectorizer.get_feature_names_out():
            word_idx = vectorizer.get_feature_names_out().tolist().index(word)
            score += tfidf_matrix[0, word_idx]
    sentence_scores[i] = score

important_sentences = heapq.nlargest(2, sentence_scores, key=sentence_scores.get)

summary = ' '.join([sentences[i] for i in important_sentences])
print("Rezumējums:", summary)
