
# Contar palindromos entre dos numeros

def count_palindromes(num1, num2):
	c=0
	for i in range(num1,num2+1):
		if str(i)[::-1] == str(i):
			c+=1
	return c

