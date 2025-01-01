#num=int(input("enter an number")
#if(num>0):
#    print(num, "is positive number")
#elif (num==0):
 #   print(num, "is zero")
#else:
 #   print(num, "is negative number")


 
yrs=int(input("enter an year"))
if ((yrs%4==0 and yrs%100!=0) or (yrs%400==0)):
        print(f"{yrs} is a leap year")
        
  
        
else:
    print(f"{yrs} is not a leap year")
    
