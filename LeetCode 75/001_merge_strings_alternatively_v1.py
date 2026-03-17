'''
Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
'''
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len_word1 = len(word1)
        print(f'word1: {word1}')
        print('len_word1: ' + str(len_word1))
        len_word2 = len(word2)
        print(f'word2: {word2}')
        print('len_word2: ' + str(len_word2))
        max_len = 0
        if len_word1 >= len_word2:
            max_len = len_word1
        else:
            max_len = len_word2


        print(f'max_len: {str(max_len)}')

        word3 = ''
        for i in range(max_len):
            if i < len_word1:
                word3 = word3 + word1[i]
            if i < len_word2:
                word3 = word3 + word2[i]
            print(f'word3: {word3}')

        print(f'End: word3: {word3}')
        return word3


sol = Solution()
result = sol.mergeAlternately(word1='ab', word2='pqrs')
print(result)
