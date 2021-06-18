Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> def func(a,b):
	c=a+b
	d=a-b
	e=a/b
	f=a*b
	#ADDITION
	print('Additon is :', +c)
	#SUBTRACTION
	print('Subtraction  is :', +d)
	#DIVISION
	print('Division is :', +e)
	#MULTIPLICATION
	print('Multiplication is :', +f)

	
>>> func(73,15)
Additon is : 88
Subtraction  is : 58
Division is : 4.866666666666666
Multiplication is : 1095
>>> 
>>> 
>>> def covid(patientname, bodytemp=98):
	 print("Patient name is "+patientname,
          " and Body temperature is", bodytemp, 'degree')

	 
>>> covid('Alex')
Patient name is Alex  and Body temperature is 98 degree
>>> 
>>> covid('Alex',108)
Patient name is Alex  and Body temperature is 108 degree
>>> 