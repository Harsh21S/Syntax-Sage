import re

def highlight_keywords(text, keywords):
    for word in keywords:
        text = re.sub(f"(?i)\\b({re.escape(word)})\\b", r"**\1**", text)
    return text
