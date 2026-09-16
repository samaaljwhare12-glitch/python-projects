has_invitation =input('Do you have an invitation?yes/no')
is_formal=input('Are wear formal?yes/no')
if has_invitation=='yes' and is_formal=='yes' :
    print('welcome')
elif has_invitation =='yes' or is_formal=='yes' :
	print('okay we will let you in')
else :
	print('sorry')
