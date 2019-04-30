import re
from collections import deque
import operator


def postfix_evaluate(items):
    d = deque(items)
    print(d)

    for index in range(len(d)):
        # print(value)
        if re.match('[0-9]', str(d[0])):
            d.append(d.popleft())
            # print(d)
            # print(value)
        else:
            # print("Getting result")
            x = (eval_binary_expr(d[-2], d[0], d[-1]))
            # print(x)
            d.pop()
            d.pop()
            d.popleft()
            d.append(x)
            # print("Evaluated")

        # print(d)
        index += 1
    return x



def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.floordiv,
        }[op]

def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    if oper == '/' and op2 == 0:
        return 0
    return get_operator_fn(oper)(op1, op2)


print(postfix_evaluate([2, 3, '+', 4, '*'] ))
print(postfix_evaluate([1, 2, 3, 4, 5, 6, '*', '*', '*', '*', '*']))
print(postfix_evaluate([7, 3, '/']))
# -2 op -1