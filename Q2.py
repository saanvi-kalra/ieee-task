import sys
def process_list(N):
	numbers=[]
	for i in range(int(N)):
  		numi = int(input(f"Enter number {i}:"))
  		numbers.append(numi)
	removal=[]
	duplicate=numbers.copy()
	for item in duplicate:
		if item<0:
			removal.append(item)
	duplicate= list(set(duplicate)-set(removal))
	duplicate.append(0)
	duplicate.sort()
	print(duplicate)
def main():
  process_list(sys.argv[1])
if __name__=='__main__':
  main()