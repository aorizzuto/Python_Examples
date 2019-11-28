# Write a Python program to remove and print every third number from a list of numbers until the list becomes empty

lst = ["a","b","c","d","e","f","g","h","i"] #,"j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

cont=0
index=0
c=0
print("index\tcont\tc\tlen\tlst")
print("{}\t{}\t{}\t{}\t{}".format(index,cont,c,len(lst),lst))
      
while len(lst)>0:
    cont+=1
    index+=1
    
    if cont >3:
        cont=1
    
    if index > len(lst):
        index=0
        c=0
    
    if cont%3 == 0:
        c+=1
            
        lst.pop(index-c)
        print("{}\t{}\t{}\t{}\t{}".format(index,cont,c,len(lst),lst))
    
