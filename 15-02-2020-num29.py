# Run-length encoding and decoding

test = "AAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCDAA"

def encode(s):
    n = len(s)
    p = ""
    output = ""
    repeat_counter = 0
    for k, c in enumerate(s):

        if p == c:
            repeat_counter += 1
        if (c != p or k == n-1): # Replace with else
            if repeat_counter != 0:
                output += str(repeat_counter) + p
            repeat_counter = 1
            p = c
    return output

def decode(s):
    output = ""
    i = 0
    for k, c in enumerate(s):
        if c.isdigit():
            i = i*10 + int(c)
        else:
            output += i*c
            i = 0
    return output
## TEST
print(encode(test))
print(decode(encode(test)))
