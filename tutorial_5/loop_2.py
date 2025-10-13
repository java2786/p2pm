num = 5
import time 
# for r in range(1, num+1):
#     print(r)
    
# 0 1 2 3 4 

a = 8
b = 7

# while(a>b and b>=0):
#     print(f"A: {a}, B: {b}")
#     b = b-1
#     time.sleep(1)

while(a>b):
    print(f"A: {a}, B: {b}")
    b = b-1
    time.sleep(1)
    if(b<0):
        # b = 10
        break 
