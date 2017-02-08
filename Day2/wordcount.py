def words(wordlist):
    wordssplit = wordlist.split()
    frequency = {}
    for word in wordssplit:
         if word.isdigit():
             word = int(word)  # TypeCast the digit to give its output as int and not string, if word is digit
         if word in frequency:
             frequency[word] += 1  # For words/keys already in the dictionary show their frequency

         else:
             frequency[word] = 1

    return frequency

words('hello andela hello')