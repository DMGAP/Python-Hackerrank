import math
import os
import random
import re
import sys



n = int(input(""))
number = int(n)
number= n%2
if n ==1:
    print("Weird")
else:
    if (number==0) and (n >= 2) or ((number==0) and (n <= 5)):
        print("Not Weird")
    elif (number ==0) and (n>=6) and ((number==0) and (n<=20)):
        print ("Weird")
    elif number==0 and n>20:
        print ("Not Weird")
    else :
        print ("Weird")