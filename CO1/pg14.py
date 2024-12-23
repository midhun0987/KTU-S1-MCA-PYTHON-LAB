#14.Accept an integer n and compute n+nn+nnn(value of n should be less than 10).

n=input("Enter an input")
s=int(n)+int(n*2)+int(n*3)
print("n+nn+nnn=",s)