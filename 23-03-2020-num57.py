# Given a string and an integer k, breaks up the string
# into lines of length <= k and such that no words is broken
# up by passing from one line to another.

def breaker(s, k):
    count = k
    output = [""]
    tmp = ""
    for c in s:
        if count > 0 and c != " ":
            tmp += c
            count -= 1
        elif c == " ":
            if len(output[-1]) != 0:
                if count != 0:
                    output[-1] += " "
                    count -= 1
                else:
                    count = k - len(temp)
                    if count < 0: return None
                    output.append("")
            output[-1] += tmp
            tmp = ""
        if count == 0:
            count = k-len(tmp)
            if count < 0: return None
            output.append("")
    output[-1] += tmp            
    return output


test1 = "The quick brown fox jumps over the lazy dog"

print(breaker(test1, 10))

