"""
This code give an image of how programmer brains works
"""

# Parameter
egg_at_shop = 60
milk_at_shop = 5
cart = { 'egg' : 0,'milk' : 0 }
report = ''

print('Mommy shout : Budi, please buy me 1 bottle of milk at shop, and if they have an egg buy 6')
print('Budi says: Okay Mom')
print('Budi goes to the shop')
print('Budi finds a milk')


if milk_at_shop > 0:
    print('there are {} bottle of milk at the shop'.format(milk_at_shop))
    print('Budi finds an egg')
    if egg_at_shop > 0:
        print('there are {} eggs at the shop'.format(egg_at_shop))
        if milk_at_shop > 6:
            print('There are more than 6 bottle of milk')
            cart['milk'] = 6
        else:
            print('There are less than 6 bottle of milk')
            cart['milk'] = milk_at_shop
        report = 'Budi says : Mom here is your order, {} eggs and {} bottle of milk'.format(cart['egg'], cart['milk'])
    else:
        print('there are {} eggs at the shop'.format(egg_at_shop))
        cart['milk'] = 1
        report = 'Budi says : Mom here is your order, {} eggs and {} bottle of milk'.format(cart['egg'], cart['milk'])
else:
    report = 'there are no milk at the shop'
print('Budi pays for {} eggs and {} bottles of milk'.format(cart['egg'], cart['milk']))
print('Budi back to home')
print(report)
if report == 'Budi says : Mom here is your order, 0 eggs and 1 bottle of milk':
    print('Thank you honey')
else:
    print('What!!! !%!@%@!#^@')



