# Lesson 21 - Build a Translator

def translate_word(word:str):
    translated_word = ""
    for letter in word:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translated_word = translated_word + "G"
            else:
                translated_word = translated_word + "g"
        else:
            translated_word = translated_word + letter
    return translated_word


print(translate_word(input("Enter your word: ")))
