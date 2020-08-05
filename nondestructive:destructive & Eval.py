a = [1,2,3]
b = a 
a[0] = 6 
# print a, b 

import copy 
a = [1,2,3]
b = copy.copy(a)
a[0] = 6 
# print a, b 

myList = [1,2,3,4,5]    # [3,4,5,1,2] n = 2  
[2,3,4,5] + [1]
tempList = myList[2:]
firstElement = myList[0:2]
print tempList, firstElement
elements = myList[1]
print elements
tempList.append(elements)
print tempList
myList = [1,2,3,4,5]    # [3,4,5,1,2] n = 2  

firstElem = myList[0]
for i in range(0, len(myList)):
	if i == len(myList) - 1: 
		myList[i] = firstElem
	else: 
		myList[i] = myList[i + 1]
	print myList

#nondestructive 
import copy 
def nonDestructive(L,n): 
	copiedList = L.copy.copy()

#destructive
def destructive(L,n): 
	newList = L

#Eval


def getEvalSteps(equation):

	tempString = ''
	sign = equation.index('**')
	# print sign
	# print equation[sign:sign+ 2]
	if equation[sign:sign + 2] == "**":
		print equation[sign:-1], 'a'
		print int(equation[sign:1])
		temp = int(equation[sign:-1]) ** int(equation[sign:1])
		tempString = equation[:6] + int(temp) + equation[10:]
	print tempString