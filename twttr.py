text = input("Text: ")
new_text = ""

vowels = ("a", "e", "i", "o", "u")
for i in range(len(text)):
    if text[i].lower() not in vowels:
        new_text += text[i]
print(new_text)
