#Recursion function for array addition
def list_add(u):
    if u==[]:
        return 0
    else:
        return u[0]+list_add(u[1:])     #recursive call
a=[]                                    #array initialization
s=int(input("Enter the size:"))
for i in range(s):                      #loop for inputs
    a.append(int(input("Enter a number:")))
print(a)
print(list_add(a))
