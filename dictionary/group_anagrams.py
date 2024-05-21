def group_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return anagrams


words = ["listen", "silent", "enlist", "rat", "tar", "art"]
print("Grouped anagrams:", group_anagrams(words))

'''
output:
Grouped anagrams: {'eilnst': ['listen', 'silent', 'enlist'], 'art': ['rat', 'tar', 'art']}
'''