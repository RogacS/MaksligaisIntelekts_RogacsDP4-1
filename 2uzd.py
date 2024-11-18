import langid

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day.",
    "Сегодня солнечный день."
]

# Функция для распознавания языка
def detect_language(text):
    try:
        language, _ = langid.classify(text)
        return language
    except Exception as e:
        return f"Ошибка: {str(e)}"

# Анализируем каждый текст
for i, text in enumerate(texts, 1):
    language = detect_language(text)
    print(f"Teksts {i} — valoda: {language}")
