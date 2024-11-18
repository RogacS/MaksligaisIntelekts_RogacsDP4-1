import nltk
from nltk.tokenize import word_tokenize

text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

tokens1 = word_tokenize(text1.lower())
tokens2 = word_tokenize(text2.lower())

words1 = {word for word in tokens1 if word.isalpha()}
words2 = {word for word in tokens2 if word.isalpha()}

common_words = words1.intersection(words2)

total_words = len(words1.union(words2))
common_percentage = (len(common_words) / total_words) * 100

print(f"Kopīgie vārdi: {common_words}")
print(f"Sakritības līmenis: {common_percentage:.2f}%")
