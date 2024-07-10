def word_token(sentence):
    words = []
    word = ""
    
    for char in sentence:
        if char == " ":        # If the character is a space, it means we've reached the end of a word
            if word!= "":      # If the word is not empty, add it to the list of words
                words.append(word)
                word = ""
        else:
            word += char        # If the character is not a space, add it to the current word
    
    if word!= "":    # After iterating through all characters, if there's a remaining word, add it to the list
         words.append(word)
    
    return words

sentence = input("Enter a sentence: ")
print(word_token(sentence))