# Write a Python program to count frequency of each character in a given string using user defined function.
def cnt():
    mystr=input("Enter your String:")
    mychar=input("Enter character for counting:")
    cnt=0
    for c in mystr:
        if c==mychar:
            cnt+=1
    print(cnt)
cnt()