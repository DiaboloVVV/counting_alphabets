def opening_file(file_name):  # function to open an file and read data from it
    with open(file_name, 'r') as r:
        data = r.read()  # saving output into variable called data
    return data  # returning text


def calculating_letters(sentence):
    down = sentence.lower()  # making sentence all to lowered to make it easier to count
    alpabet = 'abcdefghijklmnouprstqwxyz'  # string containing alphabet that'll be used to count on
    string_with_calculated = ""  # empty string to save output from loop
    for i in range(25):  # loop, easy, we have 25 letters in an alphabet
        smiting = down.count(alpabet[i])
        # counting how many letters are in whole sentence
        # , checking if there is an "a" in whole sentence, then "b" etc.
        string_with_calculated += str(smiting)  # saving output from down.count into our string
    return string_with_calculated, alpabet  # returning what we got


def saving_to_file(outcome, alphabet2):
    alpha = alphabet2.upper()  # making alphabet bigger so it looks nicer, no need to do it
    with open('output.txt', 'a') as yeet:  # opening file and appending to it
        for i in range(25):  # used to loop through every single index in string
            if outcome[i] != '0':  # getting rid of letters that doesn't appear
                yeet.write(alpha[i] + ' - ' + outcome[i] + '\n')  # saving to a file
        yeet.write('---------------')  # little break so we can differ our savings in output file


if __name__ == '__main__':
    filename = input('Please specify document you want to open \n')  # specify input file
    comet = opening_file(filename)  # reading file's content and passing it into comet variable
    calculated, alphabet = calculating_letters(comet)  # calculating how many the same letters are in
    saving_to_file(calculated, alphabet)  # passing our string with results and alphabet(so we don't need to retype it)


