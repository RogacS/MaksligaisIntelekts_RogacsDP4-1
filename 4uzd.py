from textblob import TextBlob
from deep_translator import GoogleTranslator

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

def translate_and_analyze(sentences):
    results = []
    for sentence in sentences:
        translation = GoogleTranslator(source='auto', target='en').translate(sentence)
        sentiment = TextBlob(translation).sentiment.polarity
        
        if sentiment > 0.5:
            emotion = "pozitīvs"
        elif sentiment < -0.5:
            emotion = "negatīvs"
        else:
            emotion = "neitrāls"
        results.append((sentence, translation, emotion))
    return results

analysis_results = translate_and_analyze(sentences)

for original, translated, emotion in analysis_results:
    print(f"Original: {original}")
    print(f"Translated: {translated}")
    print(f"Emotion: {emotion}\n")
