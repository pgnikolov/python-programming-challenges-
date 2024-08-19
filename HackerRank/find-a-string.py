def count_substring(string, sub_string):

    counter = 0

    x = len(string) - len(sub_string)
    for i in range(x+1):
        if string[i:(i + (len(sub_string)))] == sub_string:
            counter += 1
    return counter


string = 'ABCDCDC'
sub_string = 'CDC'
print(count_substring(string, sub_string))