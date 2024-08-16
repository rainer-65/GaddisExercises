def cap_string(text):
    new_sentence_list = []
    sentence_list = text.split('.')
    sentence_list = sentence_list[:-1]
    for sentence in sentence_list:
        new_sentence = sentence.strip().capitalize()
        new_sentence_list.append(new_sentence)
    return new_sentence_list


# Main function
if __name__ == '__main__':
    text = input('Enter an arbitrary text: ')
    new_text = cap_string(text)
    for item in new_text:
        print(item, end='. ')
