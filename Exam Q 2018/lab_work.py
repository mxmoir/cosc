import time

# Answer code
def print_word_counts(filename, words_of_interest):
    word_dict = {}
    words_of_interest = set(words_of_interest)
    for word in words_of_interest:
        word_dict[word] = 0

    with open(filename, "r") as file:
        file_list = file.read().splitlines()
        for line in file_list:
            line = line[:-1] # Remove newline char
            if line in words_of_interest:
                word_dict[line] += 1
    

    for word in words_of_interest:
        print(word + ': ' + str(word_dict[word]))
        pass



# Generate words of interest, roughly half not appearing in word list
def get_words_of_interest():
    words_of_interest = []
    with open("wordlist.txt", "r") as file:
            counter = 0
            for line_unformatted in file:
                line = line_unformatted[:-1]
                if counter % 2 == 0:
                    words_of_interest.append(line) 
                else:
                    words_of_interest.append(line + "xxx")
                counter += 1
    return words_of_interest


print("Starting...")
start = time.time()
print_word_counts('words.txt', get_words_of_interest())
print("Time taken: " + str(time.time() - start))