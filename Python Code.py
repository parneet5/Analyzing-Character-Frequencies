def sort_key(char):
    return -frequency_dictionary[char], char

def analyze_character_frequencies(text):
    text = text.lower()
    filt_text = ''.join(char for char in text if char.isalnum())
    
    global frequency_dictionary
    frequency_dictionary = {}
    for char in filt_text:
        if char in frequency_dictionary:
            frequency_dictionary[char] += 1
        else:
            frequency_dictionary[char] = 1
    
    sorted_characters = sorted(frequency_dictionary.keys(), key=sort_key)
    return sorted_characters

def main():
    text = input()
    print(analyze_character_frequencies(text))

if __name__ == "__main__":
    main()
