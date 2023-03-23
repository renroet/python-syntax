def print_upper_words (words, must_start_with = {'e'}):
    cap_words = []

    for word in words:
        cap_word = word.upper()
        for letter in must_start_with:
            cap_letter = letter.upper()
            if cap_letter == cap_word[0]:
                # cap_words.append(cap_word)
                print(cap_word)

    
            
    

