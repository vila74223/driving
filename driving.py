country = input ('Where do you come from: ')
age = input('Please enter your age: ')
age = int(age)
if country == 'China':
	if age >= 18:
		print('You can apply for driving license.')
	else:
		print('You have not reached the age.')
