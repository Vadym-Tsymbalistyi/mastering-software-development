# 1. Измените свою программу сбалансированных строк, чтобы проверить, сба-
# лансированы ли в строке круглые скобки () и фигурные скобки {}.

def check_parentheses(a_string):
    stak = []
    for c in a_string:
        if c == "(" and "(":
            stak.append(c)
        if c == "}" and "}":
            if len(stak) == 0:
                return False
            else:
                stak.pop()
    return len(stak) == 0


input_string = "(){}[]"
if check_parentheses(input_string):
    print('Скобки сбалансированы ')
else:
    print('Скобки не сбалансированы')


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


max_stack = MaxStack()
max_stack.push(3)
max_stack.push(5)
max_stack.push(2)
print("Максимальное значение:", max_stack.get_max())
max_stack.pop()
print("Максимальное значение после pop:", max_stack.get_max())