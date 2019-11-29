# Write a Python program to remove and print every third number from a list of numbers until the list becomes empty

lst = ["a","b","c","d","e","f","g","h","i"] #,"j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def remove_nums(int_list):
    position = 2 
    idx = 0
    len_list = len(int_list)
    
    while len_list>0:
        idx = (position+idx)%len_list
        print(lst)
        print("Se quito la:",int_list.pop(idx))
        len_list -= 1
    
remove_nums(lst)
    
