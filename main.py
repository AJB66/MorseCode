import winsound
import time

morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-.",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": ""
}

# Input the word or phrase, the dit duration is optional.
input_phrase = input(f"Input a word or phrase: ").upper()
dit_duration = int(input('Enter the "dit" duration in milliseconds (default is 250): ').strip() or "250")

dah_duration = 3 * dit_duration
word_split_duration = 7 * dit_duration

input_chars = list(input_phrase)

for char in input_chars:
    print(f"\n{char}")
    morse_list = list(morse_code.get(char))
    time.sleep((dah_duration - dit_duration)/1000)

    for morse_char in morse_list:

        time.sleep(dit_duration/1000)

        if morse_char == '.':
            duration = dit_duration
        else:
            duration = dah_duration

        if morse_char == " ":
            time.sleep(word_split_duration/1000 - dit_duration/1000)
        else:
            print(morse_char, end="")
            winsound.Beep(frequency=2500, duration=duration)
