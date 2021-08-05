def Prefix( a):
	
	length = len(a)
	if (length == 0):
		return ""

	if (length == 1):
		return a[0]
		
	a.sort()
	
	end = min(len(a[0]), len(a[length  - 1]))
	i = 0
	while (i < end and
		a[0][i] == a[length - 1][i]):
		i += 1

	pre = a[0][0: i]
	return pre

if __name__ == "__main__":

	List=[]
	n=int(input())
	for i in range(0, n):
	    item = input(" ")
	    List.append(item)
print(Prefix(List))


