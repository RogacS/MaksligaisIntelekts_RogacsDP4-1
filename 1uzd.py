import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."
text = text.lower()
words = word_tokenize(text)

words = [word for word in words if word.isalpha()]
word_counts = Counter(words)

print("Vārdu biežums tekstā:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

