
# file I/O basics 
f=open("python.txt", "r")
content= f.read()
#content=f.read(TO READ THE CONTENT)
print(content)

f.close
#Why we are closing?













''' content=f.read(324526)
print("1",content)

content=f.read(324526)
print("2",content)
f.close() '''




for line in content:
    print(line)
    
#comment the content = f.read cause content has already read the file 
for line in f:
    print(line)
    #print(line,end="")
    


# ''' f=open("py1.jpeg","rb")
# img=f.read()
# print(img)'''  ''' '''