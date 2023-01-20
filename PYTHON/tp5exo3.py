def palindrome(s):

    s = ''.join([c for c in s if c.isalpha()])
    
    s = s.lower()
    
    return s == s[::-1] 

s = input("Entrez un mot our une phrase: ")

if palindrome(s):
    print("C'est un palindrome!")
else:
    print("Ce n'est pas palindrome...")