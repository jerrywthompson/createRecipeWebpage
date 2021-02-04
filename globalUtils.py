import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from string import Template


def getRecipeImage(entRecipeImage):
    global imageFile

    imageFile = filedialog.askopenfilename(initialdir="/", title="Select a Image")
    entRecipeImage.set(imageFile)
    return imageFile


def createWebPage(recipeName, recipeImage, ingredients, instructions):
    recipeNameValue = recipeName.get()
    recipeImageValue = recipeImage.get()
    ingredientsValue = ingredients.get("1.0", tk.END)
    instructionsValue = instructions.get("1.0", tk.END)

    formatedIngredients = formatList(ingredientsValue)
    formatedInstructions = formatList(instructionsValue)

    messagebox.showinfo('Recipe Name', recipeNameValue)
    messagebox.showinfo('Recipe Image', recipeImageValue)
    messagebox.showinfo('Ingredients', formatedIngredients)
    messagebox.showinfo('Instructions', formatedInstructions)

    # html = htmlTemplate()
    # messagebox.showinfo('html', html)

    html = htmlTemplate()
    createHTML(html, recipeNameValue, recipeImage, formatedIngredients, formatedInstructions)


def formatList(data):
    dataFormatted = ""
    rows = data.splitlines()
    for row in rows:
        dataFormatted += "<li>" + row + "</li>\n\t\t\t\t"

    return dataFormatted

    # res = "You wrote" + txt.get()
    # lbl.configure(text = res)


def htmlTemplate():
    html = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>$recipeName</title>
    </head>
    <style>

    #bannerimage {
      width: 100%;
      padding: 10px;
      background: url($recipeImage) 50% / cover;
      height: 100px;
      background-position: center;
    }

    .sidenav {
      width: 400px;
      position: fixed;
      z-index: 1;
      top: 150px;
      left: 10px;
      background: #eee;
      overflow-x: hidden;
      padding: 8px 0;
    }

    .sidenav a {
      padding: 6px 8px 6px 16px;
      text-decoration: none;
      font-size: 25px;
      color: #2196F3;
      display: block;
    }

    .sidenav a:hover {
      color: #064579;
    }

    .main {
      margin-left: 425px; /* Same width as the sidebar + left position in px */
      margin-right: -350px:
      font-size: 28px; /* Increased text to enable scrolling */
      padding: 0px 10px;
    }

    @media screen and (max-height: 1450px) {
      .sidenav {padding-top: 15px;}
      .sidenav a {font-size: 18px;}
    }

    </style>
    <body>

        <div id="bannerimage">
                <p>
                    <center><font size="12" color="white"><b>$recipeImage</b></font></center>
                </p>
        </div>

        <div class="sidenav">
            <p>
                <center>
                    <font size="4" >
                        <b>
                            Ingredients
                        </b>
                    </font>
                </center>
            </p>
            <ul>
                $formatedIngredients
            </ul>
        </div>

        <div class="main">
            <h2>Instructions</h2>
            <ul>
                $formatedInstructions
            </ul>
        </div>
    </body>
</html>
"""
    return html


#    html = """<!DOCTYPE html>
# <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <title>$recipe_name</title>
#     </head>
#     <style>
#
#     #bannerimage {
#       width: 100%;
#       padding: 10px;
#       background: url(bread_pudding.jpg) 50% / cover;
#       height: 100px;
#       background-position: center;
#     }
#
#     .sidenav {
#       width: 400px;
#       position: fixed;
#       z-index: 1;
#       top: 150px;
#       left: 10px;
#       background: #eee;
#       overflow-x: hidden;
#       padding: 8px 0;
#     }
#
#     .sidenav a {
#       padding: 6px 8px 6px 16px;
#       text-decoration: none;
#       font-size: 25px;
#       color: #2196F3;
#       display: block;
#     }
#
#     .sidenav a:hover {
#       color: #064579;
#     }
#
#     .main {
#       margin-left: 425px; /* Same width as the sidebar + left position in px */
#       margin-right: -350px:
#       font-size: 28px; /* Increased text to enable scrolling */
#       padding: 0px 10px;
#     }
#
#     @media screen and (max-height: 1450px) {
#       .sidenav {padding-top: 15px;}
#       .sidenav a {font-size: 18px;}
#     }
#
#     </style>
#     <body>
#
#         <div id="bannerimage">
#                 <p>
#                     <center><font size="12" color="white"><b>$recipe_name</b></font></center>
#                 </p>
#         </div>
#
#         <div class="sidenav">
#             <p>
#                 <center>
#                     <font size="4" >
#                         <b>
#                             Ingredients
#                         </b>
#                     </font>
#                 </center>
#             </p>
#             <ul>
#                   <li>6 slices day-old bread</li>
#                   <li>2 tablespoons butter, melted</li>
#                   <li>½ cup raisins</li>
#                   <li>4 eggs, beaten</li>
#                   <li>2 cups milk</li>
#                   <li>¾ cup white sugar</li>
#                   <li>1 teaspoon ground cinnamon</li>
#                   <li>1 teaspoon vanilla extract</li>
#             </ul>
#         </div>
#
#         <div class="main">
#             <h2>Instructions</h2>
#
#             <ul>
#                 <li>Preheat oven to 350 degrees F (175 degrees C)</li>
#                 <li>Break bread into small pieces into an 8 inch square baking pan. Drizzle melted butter or margarine over bread. If desired, sprinkle with raisins</li>
#                 <li>In a medium mixing bowl, combine eggs, milk, sugar, cinnamon, and vanilla</li>
#                 <li>Beat until well mixed. Pour over bread, and lightly push down with a fork until bread is covered and soaking up the egg mixture</li>
#                 <li>Bake in the preheated oven for 45 minutes, or until the top springs back when lightly tapped</li>
#             </ul>
#         </div>
#     </body>
# </html>
# """


def createHTML(html, recipeNameValue, recipeImage, formatedIngredients, formatedInstructions):

    my_template = Template(html)

    # print(my_template.substitute(
    #     {'recipeName': recipeNameValue, 'recipeImage': recipeImage, 'formatedIngredients': formatedIngredients,
    #      'formatedInstructions': formatedInstructions}))

    data = my_template.substitute(
        {'recipeName': recipeNameValue, 'recipeImage': recipeImage, 'formatedIngredients': formatedIngredients,
         'formatedInstructions': formatedInstructions})

    writeFile(recipeNameValue, data)

def writeFile(recipeNameValue, data):
    fileName = recipeNameValue + ".html"
    file  = open(fileName, "w")
    file.write(data)