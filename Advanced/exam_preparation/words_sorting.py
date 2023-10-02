def words_sorting(*args):
    result = ""
    words_dict = {}
    total_sum = 0
    for word in args:
        ascii_sum = 0
        for letter in word:
            ascii_sum += ord(letter)
            total_sum += ord(letter)

        words_dict[word] = ascii_sum
    if total_sum % 2 == 0:
        sorted_dict = sorted(words_dict.items())
        for key, value in sorted_dict:
            result += f"{key} - {value}\n"
    else:
        sorted_dict = sorted(words_dict.items(), key=lambda x: -x[1])
        for key, value in sorted_dict:
            result += f"{key} - {value}\n"
    return result


print(
 words_sorting(
 'escape',
 'charm',
 'eye'
 ))




