
def text_to_morse():
    alphanumerical = {"A" : ".-",
                  "B" : "-...",
                  "C" : "-.-.",
                  "D" : "-..",
                  "E" : ".",
                  "F" : "..-.",
                  "G" : "--.",
                  "H" : "....",
                  "I" : "..",
                  "J" : ".---",
                  "K" : "-.-",
                  "L" : ".-..",
                  "M" : "--",
                  "N" : "-.",
                  "O" : "---",
                  "P" : ".--.",
                  "Q" : "--.-",
                  "R" : ".-.",
                  "S" : "...",
                  "T" : "-",
                  "U" : "..-",
                  "V" : "...-",
                  "W" : ".--",
                  "X" : "-..-",
                  "Y" : "-.--",
                  "Z" : "--..",
                  "1" : ".----",
                  "2" : "..---",
                  "3" : "...--",
                  "4" : "....-",
                  "5" : ".....",
                  "6" : "-....",
                  "7" : "--...",
                  "8" : "---..",
                  "9" : "----.",
                  "0" : "-----", }
    user_input = input("Please enter your message: ").upper()
    morse = ''
    for symbol in user_input:
        if symbol == " ":
            morse = morse + " "
        else:
            morse = morse + alphanumerical[symbol]
    
    return morse


converted_string = text_to_morse()

print(converted_string)




