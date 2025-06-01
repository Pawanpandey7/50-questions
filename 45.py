#evaluate postfix expression 
def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # use int() for integer division
            else:
                raise ValueError(f"Unknown operator: {token}")
    return stack.pop()

# Example usage
expr = "5 1 2 + 4 * + 3 -"
result = evaluate_postfix(expr)
print("Result:", result)
