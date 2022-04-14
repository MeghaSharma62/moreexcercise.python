# Ek function likho is_harshad_number jo ek number parameter ki tarah le aur fir agar woh number
# harshad number hai toh ek boolean (True agar harshad number hai, False agar nahi hai toh) return kare.
# def har(i):
#         # i=int(input("enter the number"))
#         n=i
#         sum=0
#         while i>0:
#                 sum=sum+i%10
#                 i//=10
#         print(sum)
#         if n%sum==0:
#                 print("true")
#         else:
#                 print("false")
# har(156)


n=int(input("enter the number"))
# if n%2==0 and n>20:
#         print("not weird")
# else:
#         print("weird")


#     n = int(raw_input().strip())
if n%2==0 and n>20:
        print("Not Weird")
elif n<2 and n>5 and n%2==0:
        print("Not Weird")
elif n<6 and n>20 and n%2==0:
        print("Weird")
else:
        print("Weird")