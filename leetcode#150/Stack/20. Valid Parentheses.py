class Solution:
    # my solution
    def isValid(self, s: str) -> bool:
#         stack = []
#
#         d = {")": "(", "]": "[", "{": "}"}
#
#         if [*s][0] not in ["[", '{', "("]:
#             return False
#
#         for i in [*s]:
#             if i in ["[", '{', "("]:
#                 stack.append(i)
#             else:
#                 if len(stack) != 0:
# # заменил сложное условие на hash table
#                     if i == ')' and stack[-1] == '(':
#                         stack.pop()
#                     elif i == '}' and stack[-1] == '{':
#                         stack.pop()
#                     elif ']' == i and stack[-1] == '[':
#                         stack.pop()
#                     else:
#                         return False
#                 else:
#                     return False
#
#         if len(stack) == 0:
#             return True
#         else:
#             return False

        stack = []
        d = {")": "(", "]": "[", "}": "{"}

        if s[0] not in ["[", '{', "("]:
            return False

        for i in s:
            if i in ["[", '{', "("]:
                stack.append(i)
            else:
                if len(stack) != 0:
                    if d[i] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False

    # neetcode's solution
    def isValid_neetcode(self, s: str) -> bool:
        stack = []
        d = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in d:
                if stack and stack[-1] == d[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False


c = Solution()
print(c.isValid('())('))

# d = {")": "(", "]": "[", "}": "{"}
# print(")" in d)
#
# stack = []
#
# if stack:
#     print(True)
# else:
#     print(False)

