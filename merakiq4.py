# input ka use kar ke 3 alag variables mein 3 integers ka input lein. Input lene ke baad inn 3 mein se sabse bade number ko print karo

# Note: Isme aap loops ka use nahi kar sakte.

a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
if a>b and a>c:
        print(a,"is greatest")
elif b>c and b>a:
        print(b,"is greatest")
else:
        print(c,"is greatest")