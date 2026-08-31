import sys
def is_prime(n):
	for i in range(2, int(n**0.5)+1):
		if n%i==0:
			break
	else:
		return True	
	return False
def listprime(N):
	for i in range(2,int(N)+1):
		if is_prime(i)==True:
			print(i)
def main():
	print(is_prime(7))
	print(is_prime(12))
	print(is_prime(2))
	print(is_prime(3))
	print(is_prime(4))
	print(is_prime(5))
	print(is_prime(9))
	listprime(sys.argv[1])
	
if __name__=='__main__':
	main()