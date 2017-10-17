import sys

def main():
	n = int(sys.argv[1])				#Get n
	l1 = range(1,n+1)					#Make first line
	print ' '.join(str(l) for l in l1)	#Print first line
	for j in range(2,n+1):				#For nth line, multiply first line by n
		lj = list(map(lambda x: x*j, l1))
		print ' '.join(str(l) for l in lj) #Print nth line

main()