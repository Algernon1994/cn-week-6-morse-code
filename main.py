import mc_to_text
import text_to_mc

# print(mc_to_text.morse_code_dict)
# print(text_to_mc.text_to_morse_code)

def detectMessageType(msg):
    if "." in msg or "-" in msg: 
        return "morse"
    else: 
        return "not morse"

def parseMorse(msg):
    result = []
    words = msg.split("   ")
    for word in words:
        word = word.split(" ")
        wordResult = []

        for letter in word:
            wordResult.append(letter)
        
        result.append(wordResult)

    return result

def morseToEnglish(letter):
    return mc_to_text.morse_code_dict[letter]


def mainMsg():
    msg = input("Enter your message: ")

    msgType = detectMessageType(msg)

    if msgType == "morse": # MORSE TO ENGLISH
        words = parseMorse(msg)

        translated = []
        for word in words:
            currentWord = []
            for letter in word:
                engLetter = morseToEnglish(letter)
                currentWord.append(engLetter)
            translated.append(currentWord)
        
        print(translated)

            

    elif msgType == "not morse": # ENGLISH TO MORSE
        print("Not morse")
        
    else:
        print("Error")

mainMsg()