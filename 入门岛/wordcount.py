import string ,re
text="""Hello world!  
This is an example.  
Word count is fun.  
Is it fun to count words?  
Yes, it is fun!"""
trans = str.maketrans('', '', string.punctuation)
text=text.translate(trans)
text = text.lower()
ws = text.split()
w_dict = {}
for word in ws:
    if word in w_dict:
        w_dict[word]+=1
    else:
        w_dict[word] = 1
print(w_dict)