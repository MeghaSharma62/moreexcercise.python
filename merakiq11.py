# ['NavGurukul', 'is', 'an', 'alternative', 'to', 'higher', 
# 'education', 'reducing', 'the', 'barriers', 'of', 'current', 'formal', 'education', 'system']
a=str(input("enter the sentence:"))
list=[]
str=""
for i in a:
        if i==" ":
                list.append(str)
                str=""
        else:
                str+=1
if str:
        list.append(str)
        print(list)