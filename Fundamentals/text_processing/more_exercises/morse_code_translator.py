def decrypt(message):
    message += " "
    decipher = ""
    citext = ""

    for letter in message:
        if letter != " ":
            i = 0
            citext += letter
        else:
            i += 1

            if i == 2:
                decipher += " "
            else:
                for key, value in morse_code_dict.items():
                    if citext == value:
                        decipher += key

                citext = ""

    return decipher


message = '  '.join(input().split(" | "))
morse_code_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

result = decrypt(message)
print(result)