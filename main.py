# Define the Morse code dictionary with corresponding characters and Morse symbols
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': ' ', '': '',
}

# Create a reverse dictionary for Morse to English translation
eng_dict = {value: key for key, value in morse_dict.items()}

# Display the start of the program
print("\nMORSE CODE MACHINE")


# Function to handle goodbye message
def goodbye():
    print("\nGOODBYE")


# Function to handle invalid input message
def invalid():
    print("\nInvalid.\nExiting...")


# Function to translate English text to Morse code
def eng_to_morse():
    # Get input from user for English text
    eng_string = input("What would you like to translate: \n\nText: ")

    def morse_translation(eng_string):
        try:
            # Translate each character in the input string to Morse code, ignoring empty strings
            morse_code_list = [morse_dict[string.upper()] for string in eng_string if string != '']
        except KeyError as char:
            # Handle characters that are not in the Morse code dictionary
            print(f"\nInvalid Input\n{char} not translatable.")
            return eng_to_morse()

        # Join Morse code symbols with two spaces to indicate word separation
        morse_code_string = '  '.join(morse_code_list)
        print(f"\nMorse Code Translation:\n{morse_code_string}")

        # Ask user if they want to make another translation
        answer = input("\nWould you like to make another translation? Input [Y] Yes or [N] No: ")
        if answer.upper() == "Y":
            eng_to_morse()
        elif answer.upper() == "N":
            # Ask if user wants to return to the menu or exit
            answer_two = input("\nReturn to Menu? [Y] Yes or [N] No\nInput: ")
            if answer_two.upper() == "Y":
                menu()
            elif answer_two.upper() == "N":
                goodbye()
            else:
                invalid()
        else:
            invalid()

    morse_translation(eng_string)


# Function to translate Morse code to English text
def morse_to_eng():
    # Get input from user for Morse code
    morse_string = input("\nGUIDE:\nONE space to indicate character separation\n"
                         "TWO spaces to indicate one space between words\n\n"
                         "What would you like to translate:\n\n"
                         "Text: ")

    def eng(morse_string):
        # Split the Morse code string into words using two spaces
        words = morse_string.split('  ')

        # Split each word into Morse symbols using single spaces
        morse_symbols = [word.split(' ') for word in words]

        try:
            # Translate Morse symbols to English letters, ignoring empty words
            translated_words = [''.join(eng_dict[symbol] for symbol in word) for word in morse_symbols if word != '']

            # Combine the translated words into a full English sentence
            english_translation_string = ' '.join(translated_words)
            print(f"\nEnglish Text Translation:\n{english_translation_string.title()}")

        except KeyError as invalid_symbol:
            # Handle symbols that are not in the Morse code dictionary
            print(f"\nInvalid Input\n{invalid_symbol} is not a valid Morse code symbol.")
            return morse_to_eng()  # Restart the function if an invalid symbol is found

        # Ask user if they want to make another translation
        answer = input("\nWould you like to make another translation? Input [Y] Yes or [N] No: ")
        if answer.upper() == "Y":
            morse_to_eng()
        elif answer.upper() == "N":
            # Ask if user wants to return to the menu or exit
            answer_two = input("\nReturn to Menu? [Y] Yes or [N] No\nInput: ")
            if answer_two.upper() == "Y":
                menu()
            elif answer_two.upper() == "N":
                goodbye()
            else:
                invalid()
        else:
            invalid()

    eng(morse_string)


# Dictionary to map menu options to functions
OPTIONS = {1: eng_to_morse,
           2: morse_to_eng,
           3: goodbye}


# Function to display the menu and handle user input
def menu():
    try:
        # Get user choice for the menu option
        option = int(input("\nSELECT OPTION\n[1] Translate English Text to Morse Code\n"
                           "[2] Translate Morse Code to English Text\n[3] End Program\n\nInput: "))
    except ValueError:
        # Handle non-integer input
        print("\nInvalid Input: Please select a number")
        return menu()
    try:
        # Execute the chosen option
        return OPTIONS[option]()
    except KeyError:
        # Handle invalid menu option
        print("\nInvalid Input: Not a valid option.")
        return menu()


# Start the program by displaying the menu
menu()
