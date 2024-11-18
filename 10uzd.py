from googletrans import Translator

translator = Translator()

latvian_texts = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

for text in latvian_texts:
    translation = translator.translate(text, src='lv', dest='en')
    print(f"Latviešu: {text}")
    print(f"Angļu: {translation.text}\n")
