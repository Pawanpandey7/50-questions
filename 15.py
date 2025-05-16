# to check if the two strings are anagrams

def check_anagram(word1,word2):
    word1=word1.replace(" ","").lower()
    word2=word2.replace(" ","").lower()

    if sorted(word1)==sorted(word2):
        print("they are anagrams")

    else:
        print("they are nor anagrams")    


word1="listen"
word2="silent"  
check_anagram(word1,word2)    
