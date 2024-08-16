from googletrans import Translator


# Define function
def translate_text(text_from_lang) -> str:
    translator = Translator()
    text_to_lang = translator.translate(text_from_lang, dest="english", src="auto")
    print(translator.detect(text_from_lang))
    return text_to_lang.text


# Read from console
text_from_lang = input("Please enter a text to translate ('stop' to quit): ")

while text_from_lang != "stop":
    print(translate_text(text_from_lang))
    text_from_lang = input("Please enter a text to translate ('stop' to quit): ")

print("Bye ...")
