# Write a function named format_number that takes a non-negative number as its only parameter.
# Your function should convert the number to a string and add commas as a thousand separator.
# For example, calling format_number(1000000) should return "1,000,000".

# time 29 minutes
def format_number(n):
    stringn = str(n)
    listn = [char for char in stringn]

    counter = 0
    for i in range(len(listn), 0,  -1):
        counter += 1
        if counter == 4:
            listn.insert(i, ",")
            counter = 1

    return "".join(listn)


# def format_number(n):
#     return "{:,}".format(n)

n = 999999
print(format_number(n))
