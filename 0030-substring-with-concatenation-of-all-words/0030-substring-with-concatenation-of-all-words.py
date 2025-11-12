class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def is_valid(my_str, map_temp, word_length):
            index_temp = 0
            while index_temp+word_length <= len(my_str):
                letter = my_str[index_temp: index_temp+word_length]
                if letter in map_temp:
                    map_temp[letter] -= 1
                    if map_temp[letter] == 0:
                        del map_temp[letter]
                index_temp += word_length
            return len(map_temp) == 0

        words_map = {}
        for word in words:
            words_map[word] = words_map.get(word, 0)+1
        words_length = len(words)
        word_length = len(words[0])
        total_length = words_length * word_length
        valid_comb = []

        res = []
        index = 0
        while index <= len(s) - total_length:
            mystr = s[index: index+total_length]
            if mystr in valid_comb:
                res.append(index)
                index += 1
            else:
                map_temp = words_map.copy()
                if is_valid(mystr, map_temp, word_length):
                    res.append(index)
                    valid_comb.append(mystr)
                index += 1
        return res