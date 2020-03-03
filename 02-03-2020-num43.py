
stack = []
max_stack = []


def push(val):
    if not(stack):
        max_stack.append(val)
    if val > max_stack[-1]:
        max_stack.append(val)
    stack.append(val)

def pop():
    if not(stack):
        return None
    else:
        if stack[-1] == max_stack[-1]:
            max_stack.pop()
        return stack.pop()

def maximum():
    if not(max_stack): return None
    else:
        return max_stack[-1]



push(1)
push(0)
push(4)
print(pop())
print(maximum())
