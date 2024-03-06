# Modify your balanced string program to check if the parentheses () and curly braces {} are balanced in the string.


def check_parentheses(a_string):
    stak = []
    for c in a_string:
        if c == "(" or c == "{":
            stak.append(c)
        if c == ")" or c == "}":
            if len(stak) == 0:
                return False
            else:
                stak.pop()
    return len(stak) == 0


# Create a maximum stack that will allow you to push through, push out,
# and track the largest number of your stack in O(1) time.


class MaxStack():
    def __init__(self):
        self.main = []
        self.max = []

    def push(self, n):
        if len(self.main) == 0:
            self.max.append(n)
        elif n >= self.max[-1]:
            self.max.append(n)
        else:
            self.max.append(self.max[-1])
        self.main.append(n)

    def pop(self):
        self.max.pop()
        return self.main.pop()

    def get_max(self):
        return self.max[-1]
