# in a list of input strings, sort the anagrams and print them in a line

from collections import defaultdict
def group_anagrams(strs):
    anagram_groups = defaultdict(list)

    for word in strs:
               
                  key = ''.join(sorted(word))
                  anagram_groups[key].append(word)


    for group in anagram_groups.values():
                  print(' '.join(group))


n = int(input())
strs = input().split()

group_anagrams(strs)
