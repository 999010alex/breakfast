# breakfast
#a functional breakfast
#purpose of the function: make code more readable, reuse the code multiple times,
#and to write shorter code
def mix_and_cook():
    print("mixing the ingredients")
    print("pouring the mixture into a frying pan")
    print("cooking the first side")
    print("flipping it")
    print("cooking the other side")
def make_omlette(ingredient):
    print("How to make an omelette:")
    mix_and_cook()
    omlette = 'a {} omelette!'.format(ingredient)
    return omlette
def make_pancake():
    print("How to make a pancake:")
    mix_and_cook()
    pancake = 'a tasty Pancake!'
    return pancake
def fancy_omlette(*ingredients):
    mix_and_cook()
    fancy_omlette = ' a fancy omelette with {} ingredients.'.format(len(ingredients))
    return fancy_omlette
'regular omelettes'
print(make_omlette('cheese'))
print(make_omlette('bacon'))
print(make_omlette('Mushroom'))
print(make_omlette('spinach'))
'fancy omelette'
print(fancy_omlette('sausage', 'onion', 'pepper', 'spinach', 'mushroom', 'tomato',))
