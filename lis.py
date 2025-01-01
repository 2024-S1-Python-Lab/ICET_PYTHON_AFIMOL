#List1=[-2,2,3,0,-1]
#List=[i for i in List1 if(i>0)]
#print(f"positive number={List}")

#list1=[-2,2,3,0,-1]
#list2=[]
#for i in list1:
    #if(i>0):
        #list2.append(i)
#print(f" positive list={list2}")        


list=input("enter a word :")
listword=[i for i in list if i in 'aeiouAEIOU']
print(f"vowels are :{listword}")
