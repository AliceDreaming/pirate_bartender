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

def ask_questions():
    preferenceDict = {}
    print('Please enter y or yes to answer the following questions')
    for key in questions.keys():
        print(questions[key])
        answer = raw_input()
        answer.lower()
        if(answer =='y' or answer == 'yes'):
            preferenceDict[key] = True
        else:
            preferenceDict[key] = False
    return preferenceDict

def construct_drink(prefDict):
    drinkIngredients = []

    for key in prefDict.keys():
        ingredient=[]
        if(prefDict[key]):
            try:
                randomIngredient = random.choice(ingredients[key])
                drinkIngredients.append(randomIngredient)
            except:
                print('Error! Ingredients for your taste does not exist!')
                
    return drinkIngredients
    
    
if(__name__ == '__main__'):
    prefDict = ask_questions()
    drinkIngredients = construct_drink(prefDict)
    print('Here is your drink {}'.format(drinkIngredients))