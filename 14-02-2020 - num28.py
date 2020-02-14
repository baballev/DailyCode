# Justify text algorithm
# Probably gonna do some euclidien division or similar:
# Repeat: take the length of the work, substract it to k, and repeat until length >= remaining k
# euclidian division of remaining_k by the (number of words - 1) already used -> q number of extra  space between each word and rest = add until done

# Dangerous cases: the word length is superior to k at the start


# TODO: Try to use string.join() more often as well as (for i, element in enumerate(list))

k =  16
te = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

def justify(text, length):
    nb_of_words = len(text)
    output = []
    current_line = ""
    remaining_k = length
    i = 0
    while (i < nb_of_words):
        print(i)
        j = len(text[i])
        if (j == remaining_k):
            remaining_k -= j
            current_line += text[i]
            i += 1
            output.append(pad(remaining_k, current_line))
            current_line = ""
            remaining_k = length # Reset count
        elif (j+1 <= remaining_k):
            remaining_k -= (j+1)
            current_line += text[i] + " "
            i += 1
        else:
            current_line = current_line[:-1]
            remaining_k += 1
            output.append(pad(remaining_k, current_line))
            current_line = ""
            remaining_k = length # Reset count
    current_line = current_line[:-1]
    remaining_k += 1
    output.append(pad(remaining_k, current_line))

    return output

def pad(remaining_k, line):
    words = line.split(" ")
    print(words)
    n = len(words)
    if n != 0: q, r = remaining_k // (n-1), remaining_k % (n-1)
    else: q, r = -1, n
    line = ""
    l = 0
    while (l<(n-1)):
        line += words[l] + (q+1)*" "
        if r > 0:
            line += " "
            r -= 1
        l += 1
    line += words[-1]
    return line



print(justify(te, k))
