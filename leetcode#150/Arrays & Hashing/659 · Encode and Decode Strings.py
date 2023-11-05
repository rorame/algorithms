def encode(strs):
    res = []
    for i in range(len(strs)):
        res.append(strs[i] + ":;")
    return "".join(res)

def decode (str):
    return str.split(":;")[:-1]

strs = ["we", "say", ":", "yes"]

str = encode(strs)
print(str)

res = decode(str)
print(res)

# res = []
#
# for i in range(len(strs)):
#     res.append(strs[i] + ":;")
# print("".join(res))
#
# str = "lint:;code:;love:;you:;"
#
# print(str.split(":;")[:-1])
