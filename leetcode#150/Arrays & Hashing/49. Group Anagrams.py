class Solution:
    # my solution
    # создаем словарь, где ключ - анаграмм (в виде строки), а значение - это лист с
    def groupAnagrams(self, strs):
        anagrams = {}

        for s in strs:
            if "".join(sorted(s)) not in anagrams:
                anagrams["".join(sorted(s))] = [s]
            else:
                anagrams["".join(sorted(s))] = anagrams.get("".join(sorted(s)), []) + [s]

        return [*anagrams.values()]

strs = ["a"]



c = Solution()
print(c.groupAnagrams(strs))


