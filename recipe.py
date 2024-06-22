import requests

def get_recipes(api_key, ingredients):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        'apiKey': api_key,
        'ingredients': ','.join(ingredients),
        'number': 5,  
        'ranking': 1 
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    
    api_key = 'aff346b8f1ef4bc5b15e0a42deb64dde'

 
    user_input = input("Enter your available ingredients (comma separated): ")
    available_ingredients = [ingredient.strip().lower() for ingredient in user_input.split(",")]


    recipes = get_recipes(api_key, available_ingredients)

    if recipes:
        print("You can make the following recipes:")
        for recipe in recipes:
            print(f"- {recipe['title']}")
            print(f"  Used ingredients: {', '.join([ingredient['name'] for ingredient in recipe['usedIngredients']])}")
            print(f"  Missing ingredients: {', '.join([ingredient['name'] for ingredient in recipe['missedIngredients']])}")
            print(f"  Recipe link: https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-')}-{recipe['id']}")
    else:
        print("No recipes found with the given ingredients.")

if __name__ == "__main__":
    main()

