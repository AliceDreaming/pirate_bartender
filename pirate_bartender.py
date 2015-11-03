import random


questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

ingredients_stock = {
    "glug of rum":5,
    "slug of whisky":5,
    "splash of gin":5,
    "olive on a stick":5,
    "salt-dusted rim":5,
    "rasher of bacon":5,
    "shake of bitters":5,
    "splash of tonic":5,
    "twist of lemon peel":5,
    "sugar cube":5,
    "spoonful of honey":5,
    "spash of cola":5,
    "slice of orange":5,
    "dash of cassis":5,
    "cherry on top":5
    }
    
# Ask customer questions for their taste
def ask_questions():
    preferenceDict = {}
    print('Please enter y or yes to answer the following questions')
    for key in questions.keys():
        print(questions[key])
        preferenceDict[key] = raw_input().lower() in ['y', 'yes']
    return preferenceDict

# Make a draink based on customer's preferences
def construct_drink(prefDict):
    drinkIngredients = []

    for key in prefDict.keys():
        ingredient=[]
        if(prefDict[key]):
            # Get a random ingredient from the ingredient list
            randomIngredient = random.choice(ingredients[key])
            drinkIngredients.append(randomIngredient)
                    
    return drinkIngredients
    
def main():
    customerPrefDict={}
    barOpen = True
    while barOpen:
        print("Hello, what's your name?")
        customerName = raw_input().lower()
        customerDrink=[]
        if(customerName in customerPrefDict):
            customerDrink=customerPrefDict[customerName]
        else:
            prefDict = ask_questions()
            customerDrink = construct_drink(prefDict)
            customerPrefDict[customerName]=customerDrink
            
        print('Here is your drink {}'.format(customerDrink))
            
        # Reduce the count of ingredients. If the count decreased to 0, restore the stock
        for ingredient in customerDrink:
            ingredients_stock[ingredient] -=1
            print("Current count of {} is {}".format(ingredient, ingredients_stock[ingredient]))
            
            if(ingredients_stock[ingredient] <= 0):
                print('Restore ingredients stock')
                ingredients_stock[ingredient] = 5
                
    
if(__name__ == '__main__'):
    main()
        