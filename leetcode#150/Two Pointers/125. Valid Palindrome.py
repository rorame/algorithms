def isPalindrome(s):
    # my solution Time Limit Exceeded :(((
    s_clear = "".join(filter(str.isalnum, s)).lower()

    i = 0
    j = len(s_clear) - 1

    while i < j:
        if s_clear[i] == s_clear[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

def isPalindrome_1(s):
    # netcoode solution 1 with extra memory
    res = ""
    for c in s:
        if c.isalnum():
            res += c.lower()
    return res == res[::-1]

def isPalindrome_2(s):
    # netcoode solution 1 with O(1) memory
    l, r = 0, len(s) - 1
    while l < r:

        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

def alphaNum(c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("1") <= ord(c) <= ord("9"))


print(isPalindrome_2("A man, a plan, a canal: Panama"))

# см ASCII table
# print(ord("A"))


