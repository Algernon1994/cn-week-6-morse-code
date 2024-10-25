text_to_morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', 
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', 
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def text_to_morse(words):
    morse_code = []
    for word in words:
        morse_word = []
        for char in word.upper():
            if char in text_to_morse_code:
                morse_word.append(text_to_morse_code[char])  # converts each character to morse code
        morse_code.append(' '.join(morse_word))  # put a space between each letter
    return '   '.join(morse_code)  # puts three spaces between words, if i haven't misscounted

# let someone type words until they type 'done' like i learned from either yesterday or last week
words = []
while True:
    word = input("Enter a word to convert to Morse code (type 'done' to finish): ")
    if word.lower() == 'done':
        break
    words.append(word)

morse_result = text_to_morse(words)
print("Morse Code:", morse_result)