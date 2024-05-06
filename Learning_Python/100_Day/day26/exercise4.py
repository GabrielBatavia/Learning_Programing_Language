# convert a sentence into a list of words.

sentence = input("Input your sentence : ")

result = {word:len(word) for word in sentence.split()}

print(result)