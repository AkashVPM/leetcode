'''
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 
Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]
'''

from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        left = 0 
        search = len(words[0]) *len(words) 
        right = left + search 
        length = len(words[0])
        out = []
        target = Counter(words)
        

        while right <=  len(s):

            seen = []
            check = s[left:right:]

            start = 0
            end = length

            while end <= len(check):
                seen.append(check[start:end])
                start += length
                end += length

            if Counter(seen) == target: 
                out.append(left)

            left += 1
            right = (left + search)
        
        return out