# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    s1 = word
    s2 = anagram
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    if len(sorted_s1) == len(sorted_s2) :    
 
        if sorted_s1 == sorted_s2:
            return True
        else :
            return False
    else:
            return False    
 
print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))


