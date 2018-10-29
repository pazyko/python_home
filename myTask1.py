print('Hello,stranger!')
while True:
	print('Enter your name')
	name=input()
	if name!='Svetik':
		continue
	print('Welcome,Svetik.Enter your password')
	password=input()
	if password=='123':
		break
print('Access granted')
