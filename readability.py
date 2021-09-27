# boiler plate
import cs50

# loop
while True:
    str = cs50.get_string('Text: ')
    result = 0
    i = 0
    alphabets = 0
    digits = 0
    special = 0
    words = 1
    sentences = 0
    if (str):
        for i in range(len(str)):
            if (str[i].isalpha()):
                alphabets += 1
            elif (str[i].isnumeric()):
                digits += 1
            elif (str[i] == ' ' and str[i + 1]):
                words += 1
            elif (str[i] == '?' or str[i] == '!' or str[i] == '.'):
                sentences += 1
            else:
                special += 1

        # average number of letters per 100 words in the text
        L = float(alphabets / words * 100)

        # the average number of sentences per 100 words in the text
        S = float(sentences / words * 100)

        # Readbility, already provided to us
        result = round((float)(0.0588 * L - 0.296 * S - 15.8))

        # prints result
        if (result >= 16):
            print('Grade 16+')
        elif (result < 1):
            print('Before Grade 1')
        else:
            print(f'Grade {result}')

        break