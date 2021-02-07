import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from string import Template
import base64
import PIL
from PIL import Image
from resizeimage import resizeimage


def getRecipeImage(entRecipeImage):
    global imageFile

    imageFile = filedialog.askopenfilename(initialdir="/", title="Select a Image")
    entRecipeImage.set(imageFile)
    return imageFile


def createWebPage(recipeName, recipeImage, ingredients, instructions, nutrition):
    recipeNameValue = recipeName.get()
    recipeImageValue = recipeImage.get()
    ingredientsValue = ingredients.get("1.0", tk.END)
    instructionsValue = instructions.get("1.0", tk.END)
    nutritionValue = nutrition.get("1.0", tk.END)


    updatedImage = resizeImage(recipeImageValue, recipeName)

    updatedImage2 = resizeImage2(recipeImageValue, recipeName)

    base64Image = convertInageToBase64(updatedImage)


    formatedIngredients = formatList(ingredientsValue)
    formatedInstructions = formatList(instructionsValue)

    ingredientsLength = calculateIngredientsLength(formatedIngredients)

    # messagebox.showinfo('Recipe Name', recipeNameValue)
    # messagebox.showinfo('Recipe Image', base64Image)
    # messagebox.showinfo('Ingredients', formatedIngredients)
    # messagebox.showinfo('Instructions', formatedInstructions)


    recipeHTML = htmlTemplate()
    createHTML(recipeHTML, recipeNameValue, base64Image, formatedIngredients, formatedInstructions, nutritionValue, ingredientsLength)

    divHTML = divTemplate()
    updateIndexTemplate(divHTML, recipeNameValue, base64Image)


def formatList(data):
    dataFormatted = ""
    rows = data.splitlines()
    for row in rows:
        dataFormatted += "<li>" + row + "</li>\n\t\t\t\t"

    return dataFormatted


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
      background: url(" data:image/jpg;base64,$recipeImage") 50% / cover;
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
    
    .sidenav2 {
      width: 400px;
      position: fixed;
      z-index: 1;
      top: ${ingredientsLength}px;
      left: 10px;
      background: #eee;
      overflow-x: hidden;
      padding: 8px 0;
    }

    .sidenav2 a {
      padding: 6px 8px 6px 16px;
      text-decoration: none;
      font-size: 25px;
      color: #2196F3;
      display: block;
    }

    .sidenav2 a:hover {
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
                    <center><font size="12" color="white"><b>$recipeName</b></font></center>
                </p>
        </div>
        <div class="sidenav">
            <p>
                <center>
                    <h1>
                        <b>
                            Ingredients
                        </b>
                    </h1>
                </center>
            </p>
            <ul>
                $formatedIngredients
            </ul>
        </div>
        <div class="sidenav2">
            <p>
                <center>
                    <h1>
                        <b>
                            Nutrition
                        </b>
                    </h1>
                </center>
            </p>
            <p>
                $nutrition
            </p>
        </div>
        <div class="main">
            <h1><b>Instructions</b></h1>
            <ul>
                $formatedInstructions
            </ul>
        </div>
    </body>
</html>
"""
    return html

def divTemplate():
    indexDiv = """            <div class="inner-grid">
                <p><font size="5" color="black"><b>${recipeName}</b></font></p>
                <a href="html/${recipeName}.html" alt="${recipeName}">
                    <img src="data:image/png;base64,${recipeImage}"?auto=compress&cs=tinysrgb&dpr=1&w=500/>
                </a>
            </div>"""
    return indexDiv

def createHTML(html, recipeNameValue, recipeImage, formatedIngredients, formatedInstructions, nutrition, ingredientsLength):

    recipeHTMLtemplate = Template(html)

    data = recipeHTMLtemplate.substitute(
        {'recipeName': recipeNameValue, 'recipeImage': recipeImage, 'formatedIngredients': formatedIngredients,
         'formatedInstructions': formatedInstructions,'nutrition': nutrition, 'ingredientsLength': ingredientsLength})

    writeRecipeFile(recipeNameValue, data)

def writeRecipeFile(recipeNameValue, data):
    # import os
    # CURR_DIR = os.getcwd()
    # print("CURR_DIR: " + CURR_DIR)
    fileName = "./html/" + recipeNameValue + ".html"
    file  = open(fileName, "w")
    file.write(data)
    # print (data)


def convertInageToBase64(image_path):

    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')



def calculateIngredientsLength(data):
    rows = len(data.splitlines())

    ingredientsLength = (rows * 50) + 150

    return ingredientsLength

def updateIndexTemplate(html, recipeNameValue, recipeImage):

    divHTMLtemplate = Template(html)

    data = divHTMLtemplate.substitute(
        {'recipeName': recipeNameValue, 'recipeImage': recipeImage})

    findIndexFile(data)

def findIndexFile(data):
    fileName = "index.html"
    # fileName2 = "index2.html"

    searchTxt = """        </div>
    </body>
</html>"""

    newText = data + "\n" +searchTxt

    with open(fileName, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(searchTxt, newText)

    # Write the file out again
    with open(fileName, 'w') as file:
        file.write(filedata)

    print(filedata)

def resizeImage(recipeImage, recipeName):
    base_width = 800
    imagePath = "./images/" + str(recipeName) + ".jpg"
    image = Image.open(recipeImage)
    width_percent = (base_width / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(width_percent)))
    image = image.resize((base_width, hsize), PIL.Image.ANTIALIAS)
    image.save(imagePath)
    return imagePath


def resizeImage2(recipeImage, recipeName):

    fd_img = open(recipeImage, 'r')
    img = Image.open(fd_img)
    img = resizeimage.resize_thumbnail(img, [800, 800])
    img.save('test-image-thumbnail.jpeg', img.format)
    fd_img.close()