# 1. Измените свою программу сбалансированных строк, чтобы проверить, сба-
# лансированы ли в строке круглые скобки () и фигурные скобки {}.

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


# 2. Создайте максимальный стек, который позволит проталкивать, выталкивать
# и отслеживать самое большое число вашего стека за время О(1).

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
