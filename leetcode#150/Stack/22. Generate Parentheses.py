
def generateParenthesis(n: int):
    # only add open parenthesis if open < n
    # only add a closing parenthesis if closed < open
    # valid IIF opem == closed == n

    stack = []
    res = []

    def backtrack(openN, closeN):
        if openN == closeN == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closeN)
            stack.pop()

        if closeN < openN:
            stack.append(")")
            backtrack(openN, closeN + 1)
            stack.pop()

    backtrack(0, 0)
    return res

print(generateParenthesis(3))