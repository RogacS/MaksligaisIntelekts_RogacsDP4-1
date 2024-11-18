import re

raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

def clean_text(text):
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)  
    text = text.lower()
    return text

cleaned_text = clean_text(raw_text)
print("Tīrītais teksts:", cleaned_text)
