def isPalindrome(phrase):
    reverse = phrase[::-1]
    reverse = reverse.lower()
    reverse = reverse.replace(' ', '')
    phrase = phrase.replace(' ', '')
    print("Phrase=",phrase.lower())
    print("reverse=", reverse)

    if (phrase.lower() == reverse):
        return True
    else:
        return False


print(isPalindrome("Taco cat."))