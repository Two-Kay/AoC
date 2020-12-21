def split_entries(data):
    '''
    Splits input data into two two-dimensional lists of ingredients and allergens.
    '''
    ingredients = []
    allergens = []
    for i in range(len(data)):
        split_data = data[i].split(" (")
        ingredients.append(split_data[0].split(" "))
        allergen = split_data[1]
        allergen = allergen[9:(len(allergen)-1)]
        allergens.append(allergen.split(", "))
    return ingredients, allergens

data = open("Day 21\input21", "r+")
data = data.read()
data = data.split("\n")
ingredients, allergens = split_entries(data)

def determine_allergen(ingredient, allergen, ingredients, allergens):
    '''
    Determines whether a given ingredient could contain an allergen.
    Returns a boolean value.
    '''
    isAllergen = False
    appearsOutside = False
    for i in range(len(ingredients)):
        isInAllergens = False
        for x in range(len(allergens[i])):
            if(allergen == allergens[i][x]):
                isInAllergens = True
        if isInAllergens:
            isAllergen = False
            for j in range(len(ingredients[i])):
                if(ingredient == ingredients[i][j]):
                    isAllergen = True
            if (isAllergen == False):
                return False
        else:
            for j in range(len(ingredients[i])):
                if(ingredient == ingredients[i][j]):
                    appearsOutside = True
    if appearsOutside:
        isAllergens = False
    return isAllergen

def list_up_allergens(allergens):
    '''
    Lists up all allergens of the input data!
    (May or may not have been used for ingredients as well)
    '''
    allergens_list = []
    for i in range(len(allergens)):
        for j in range(len(allergens[i])):
            if(allergens[i][j] not in allergens_list):
                allergens_list.append(allergens[i][j])
    return(allergens_list)

def count_not_allergen(ingredients, allergens):
    '''
    Counts the amount of ingredients which don't pose a threat of allergens.
    Counts duplicate values within the ingredients list too!
    Returns an integer of the count.
    '''
    count = 0
    checkedIngredients = []
    notAllergen = []
    allergensList = list_up_allergens(allergens)
    for i in range(len(ingredients)):
        for j in range(len(ingredients[i])):
            ingredient = ingredients[i][j]
            if(ingredient not in checkedIngredients):
                isAllergen = False
                for k in range(len(allergensList)):
                    allergen = allergensList[k]
                    if(determine_allergen(ingredient, allergen, ingredients, allergens) == True):
                        isAllergen = True
                        break
                checkedIngredients.append(ingredient)
                if(isAllergen == False):
                    notAllergen.append(ingredient)
    for x in range(len(ingredients)):
        for y in range(len(notAllergen)):
            if(notAllergen[y] in ingredients[x]):
                count += 1
    return count

def determine_most_dangerous(ingredients, allergens):
    '''
    Determines which ingredients belong to allergens.
    Returns a two dimensional list where the first column is the allergen
    and the second column the ingredient which contains the associated allergen.
    '''
    ingredientsList = list_up_allergens(ingredients)
    allergensList = list_up_allergens(allergens)
    associatedIngredients = list_up_allergens(allergens)
    output = []
    for x in range(len(associatedIngredients)):
        output.append([])
        output[x].append(associatedIngredients[x])
    for i in range(len(ingredientsList)):
        for j in range(len(allergensList)):
            if(determine_allergen(ingredientsList[i], allergensList[j], ingredients, allergens) == True):
                output[j].append(ingredientsList[i])
    isSorted = False
    sortedIngredient = []
    while(isSorted == False):
        isSorted = True
        for i in range(len(output)):
            if(len(output[i]) == 2):
                if(output[i][1] not in sortedIngredient):
                    sortedIngredient.append(output[i][1])
            else:
                isSorted = False
                for j in range(len(sortedIngredient)):
                    if(sortedIngredient[j] in output[i]):
                        output[i].remove(sortedIngredient[j])
    return(output)

puzzle1 = count_not_allergen(ingredients, allergens)
puzzle2 = determine_most_dangerous(ingredients, allergens)
print(puzzle1, puzzle2)
'''
Since writing a function to sort the list of allergens alphabetically
would take longer than just reading the output, here the actual puzzle2 result
"vpzxk,bkgmcsx,qfzv,tjtgbf,rjdqt,hbnf,jspkl,hdcj"
'''