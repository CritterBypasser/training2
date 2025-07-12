from collections import defaultdict
def group_anagrams(strs):
    anagram_groups = defaultdict(list)

    for word in strs:
                  # Sort the word to get the key                  
                  key = ''.join(sorted(word))
                  anagram_groups[key].append(word)

# Print each group in a new line 

    for group in anagram_groups.values():
                  print(' '.join(group))


# Input
n = int(input())
strs = input().split()

# Call function

group_anagrams(strs)