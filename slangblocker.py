def change(a):
    j = 0
    b = ""
    a = list(a)
    while j<len(a):
        if  a[j] == "a" or a[j] == "e" or a[j] == "i" or a[j] == "o" or a[j] == "u" or a[j] == "A" or a[j] == "E" or a[j] == "I" or a[j] == "O" or a[j] == "U":
            a[j] = "*" 
        #else:
        #    j = len(a)//2
        #    a[j] = "*"

        j = j+1
    for letter in a:
        b = b + letter 
    return b
f = open("slang.txt" , "r")
list_slang = f.read().split()
f.close()
text = input("your text: ")
text = text.split()
i = 0
while i<len(text):
    if text[i] in list_slang:
        text[i] = change(text[i])
    i = i+1
text = " ".join(text)
print(text)
cho = input("do you want to add more slang to help us?(Y/n)")

if cho == "Y" or cho == "y":
    new_slang = input("then input your slang:(only slang word, other good words can harm this)\n")
    if new_slang in list_slang:
        print("it's already imported!")
    
    else:    
        f = open("slang.txt" , "a")
        f.write(" " + new_slang)
        f.close()
elif cho == "n" or cho == "N":
    print("thanks for using us")
else:
    print("invalid choice\n thanks for using us")        
