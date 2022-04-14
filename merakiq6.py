string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
i=0
b=[]
while i<len(string_list):
        if string_list[i] not in b:
                b.append(string_list[i])
        i+=1
print(b)