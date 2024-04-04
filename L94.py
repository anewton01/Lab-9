#the authors' names are Abby Newton and Viviana Antimo
red_velvet={"cake flour":"3 cups","baking soda":"1 teaspoon","cocoa powder":"2 tablespoons","salt":"1/2 teaspoon","unsalted butter":"1/2 cup","sugar":"2 cups","canola oil":"1 cup","eggs":"4","vanilla extract":"1 tablespoon","distilled white vinegar":"1 teaspoon","red food coloring":"3 drops","buttermilk":"1 cup"}
lemon={"flour":"1 and 1/2 cups","baking powder":"2 teaspoons","salt":"1/2 teaspoon","unsalted butter":"1/2 cup","sugar":"1 cup","eggs":"2","vanilla extract":"1 and 1/2 teaspoons","milk":"1/2 cup","lemon juice and zest":"2"}
def cake_recipe(recipe1,recipe2):
    similar_ingredients=[]
    for x in recipe1:
        if x in recipe2:
            similar_ingredients.append(x)
    return similar_ingredients
print(cake_recipe(red_velvet,lemon))
