import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from string import Template
import base64
import os
import PIL
from PIL import Image
from resizeimage import resizeimage


def getRecipeImage(entRecipeImage):
    global imageFile

    imageFile = filedialog.askopenfilename(initialdir="/", title="Select a Image")
    entRecipeImage.set(imageFile)
    return imageFile


def createWebPage(recipeName, recipeType, recipeImage, ingredients, instructions, nutrition, notes, comments):
    global CURR_DIR
    CURR_DIR = os.getcwd()
    # previousDir = os.chdir(".")
    # previousDir2 = os.chdir("..")

    # print("CURR_DIR: " + CURR_DIR)
    #
    #
    #
    # print (os.path.abspath(os.curdir))
    #
    # os.chdir("..")
    # print (os.path.abspath(os.curdir))

    recipeNameValue = recipeName.get()
    recipeType = recipeType.get()
    recipeImagePath = recipeImage.get()
    ingredientsValue = ingredients.get("1.0", tk.END)
    instructionsValue = instructions.get("1.0", tk.END)
    nutritionValue = nutrition.get("1.0", tk.END)
    notesValue = notes.get("1.0", tk.END)
    commentsValue = comments.get("1.0", tk.END)


    # updatedImage = resizeImage(recipeImagePath, recipeNameValue)



    resizeDimension  = getResizeDimension(recipeImagePath)

    imageResized = resizeImage(recipeImagePath, resizeDimension, recipeNameValue)

    # updatedImage2 = resizeImage2(recipeImagePath, recipeNameValue)

    base64Image = convertInageToBase64(imageResized)


    formattedIngredients = formatList(ingredientsValue)
    formattedInstructions = formatList(instructionsValue)
    formattedNotes = formatList(notesValue)
    formattedComments = formatList(commentsValue)
    # ingredientsLength = calculateIngredientsLength(formattedIngredients)

    # messagebox.showinfo('Recipe Name', recipeNameValue)
    # messagebox.showinfo('Recipe Image', base64Image)
    # messagebox.showinfo('Ingredients', formattedIngredients)
    # messagebox.showinfo('Instructions', commentsValue)

    isTest = 'yes'

    if isTest == 'yes':
        testDataValues = getTestData()
        formattedIngredients = formatList(testDataValues['ingredients'])
        formattedInstructions = formatList(testDataValues['instructions'])
        formattedNotes = formatList(testDataValues['notes'])
        formattedComments = formatList(testDataValues['comments'])
        nutritionValue = testDataValues['nutrition']


    recipeHTML = htmlTemplateNEW()
    createHTML(recipeHTML, recipeNameValue, recipeType, base64Image, formattedIngredients, formattedInstructions, nutritionValue, formattedNotes, formattedComments)

    divHTML = divTemplate()
    updateIndexTemplate(divHTML, recipeType, recipeNameValue, base64Image)

    messagebox.showinfo("Recipe Name", "Recipe HTML has been successfully created: " + recipeNameValue)

    if isTest == 'yes':
        import webbrowser
        newFilePath = "file:///home/jerry/develop/html/" + recipeType + "/html/" + recipeNameValue + ".html"
        webbrowser.open_new_tab(newFilePath)



def formatList(data):
    dataFormatted = ""
    rows = data.splitlines()
    for row in rows:
        dataFormatted += "<li>" + row + "</li>\n\t\t\t\t"

    return dataFormatted

def formatWithCheckboxes(type, data):
    dataFormatted = ""
    checkboxHTML = """<input type="checkbox" name="$type" value="$value">$value<br><br>"""
    checkboxHTMLtemplate = Template(checkboxHTML)

    rows = data.splitlines()
    for row in rows:
        dataFormatted += checkboxHTMLtemplate.substitute({'type': type, 'value': row})

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
                $formattedIngredients
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
                $formattedInstructions
            </ul>
        </div>
    </body>
</html>
"""
    return html


def htmlTemplateNEW():
    html = """<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
    <style>
        .header { grid-area: header; 
            width: 100%;
            padding: 10px;
            background: url(" data:image/jpg;base64,$recipeImage");
            height: 100px;
            background-position: center;
            background-size: cover;
        }
        .ingredients { 
            grid-area: ingredients; 
            background: #eee;
            width: 400px;
            overflow: hidden
        }
        .instructions { 
            grid-area: instructions;
            overflow: hidden;
        }
        .notes { 
            grid-area: notes;
            background: #eee;
            width: 400px;
            overflow: hidden
        }
        .nutrition { 
            grid-area: nutrition;
            background: #eee;
            width: 400px;
            overflow: hidden;
        }
        .comments { 
            grid-area: comments;
        }
        
        .grid-container {
          display: grid;
          grid-template-areas:
            'header header header header header header'
            'ingredients instructions instructions instructions instructions instructions'
            'notes comments comments comments comments comments'
            'nutrition comments comments comments comments comments';
          grid-gap: 10px;
          /*background-color: #2196F3;*/
          padding: 10px;
        }
        
        .grid-container > div {
         /* background-color: rgba(255, 255, 255, 0.8);*/
          padding: 20px 0;
          font-size: 30px;
        }
        
        input[type='checkbox'] {
            -webkit-appearance:none;
            width:30px;
            height:30px;
            background:white;
            border-radius:5px;
            border:2px solid #555;
            float: left;
        }
        
        input[type='checkbox']:checked {
            background: blue;
        }
        
        label {
            display: block;
            margin-left: 24px;
        }
    </style>
    <script data-dapp-detection="">
        !function(){let e=!1;function n(){if(!e){const n=document.createElement("meta");n.name="dapp-detected",document.head.appendChild(n),e=!0}}if(window.hasOwnProperty("ethereum")){if(window.__disableDappDetectionInsertion=!0,void 0===window.ethereum)return;n()}else{var t=window.ethereum;Object.defineProperty(window,"ethereum",{configurable:!0,enumerable:!1,set:function(e){window.__disableDappDetectionInsertion||n(),t=e},get:function(){if(!window.__disableDappDetectionInsertion){const e=arguments.callee;e&&e.caller&&e.caller.toString&&-1!==e.caller.toString().indexOf("getOwnPropertyNames")||n()}return t}})}}();
    </script>
</head>

<body>
    <div class="grid-container">
        <div class="header">
            <h1>
                <center>
                    <font color="white">
                        <b>$recipeNameValue</b>
                    </font>
                </center>
            </h1>
        </div>
        <div class="ingredients">
            <h2>
                <center>
                    <b>Ingredients</b>
                </center>
            </h2>   
            <ul>
                $formattedIngredients
            </ul>
        </div>
        <div class="instructions">
            <h2>
                <b>Instructions</b>
            </h2>
            <ul>
                $formattedInstructions
             </ul>
        </div>
        <div class="notes">
            <h2>
            <center>
                <b>Notes</b>
            </center>
        </h2>
            <ul>
                $formattedNotes
             </ul>
        </div>
        <div class="nutrition">
            <h2>
                <center>
                    <b>Nutrition</b>
                </center>
            </h2>
            <p>
                $nutrition
            </p>
        </div>
        <div class="comments">
            <h2>
                <b>Comments</b>
            </h2>
            <p>
                $formattedComments
            </p>
        </div>
    </div>
</body>

</html>"""

    return html


def divTemplate():
    indexDiv = """            <div class="inner-grid">
                <p><font size="5" color="black"><b>${recipeName}</b></font></p>
                <a href="html/${recipeName}.html" alt="${recipeName}">
                    <img src="data:image/png;base64,${recipeImage}"?auto=compress&cs=tinysrgb&dpr=1&w=500/>
                </a>
            </div>"""
    return indexDiv


def getTestData():
    testData = {}

    testData['type'] = 'main_course'

    testData['ingredients'] = """2 cups shredded cheese mozzarella or cheddar * See notes
1/4 cup cream cheese softened
1 1/2 cups almond flour
3 large eggs Divided ** See notes
1 tsp baking powder optional2 cups shredded chjasdfjkfdaskjdfs kjfasdkjfdaskjlfdsaklfdsakjfdsa jkafkaldflkadlfkjadkfjadk flafalklajfkaljfklaeese mozzarella or cheddar * See notes
1/4 cup cream cheese softened
1 1/2 cups almond flour
3 large eggs Divided ** See notes
1 tsp baking powder optional2 cups shredded cheese mozzarella or cheddar * See notes
1/4 cup cream cheese softened
1 1/2 cups almond flour
3 large eggs Divided ** See notes
1 tsp baking powder optional2 cups shredded cheese mozzarella or cheddar * See notes
1/4 cup cream cheese softened
1 1/2 cups almond flour
3 large eggs Divided ** See notes
"""

    testData['instructions'] = """Preheat the oven to 180C/350F. Line a large baking tray with parchment paper and set aside.
In a large, microwave safe bowl, add your shredded cheese and cream cheese. Microwave for 30 seconds, or until the cheeses have mostly melted. Remove from the microwave and whisk together, until smooth. Let the cheese cool for several minutes.
When the cheese has cooled slightly, add in the almond flour and two of the eggs, and mix well, until a smooth dough remains.
Using your hands, form 10 balls of dough. Place them on the lined tray. Whisk the remaining egg and using a pastry brush, brush the exterior of each of the rolls.
Bake the rolls for 25 minutes, or until golden on the outside. Serve warm.
Preheat the oven to 180C/350F. Line a large baking tray with parchment paper and set aside.
In a large, microwave safe bowl, add your shredded cheese and cream chem,cvx,.vmz.c,v.z,c,.zmxcv.zml;vakf;lvk;lzmc,.z/mv,.zmcv,.mzckv.mzklmcvz.,mvc,.zcmv,.cx.,ese. Microwave for 30 seconds, or until the cheeses have mostly melted. Remove from the microwave and whisk together, until smooth. Let the cheese cool for several minutes.
When the cheese has cooled slightly, add in the almond flour and two of the eggs, and mix well, until a smooth dough remains.
Using your hands, form 10 balls of dough. Place them on the lined tray. Whisk the remaining egg and using a pastry brush, brush the exterior of each of the rolls.
Bake the rolls for 25 minutes, or until golden on the outside. Serve warm.Preheat the oven to 180C/350F. Line a large baking tray with parchment paper and set aside.
In a large, microwave safe bowl, add your shredded cheese and cream cheese. Microwave for 30 seconds, or until the cheeses have mostly melted. Remove from the microwave and whisk together, until smooth. Let the cheese cool for several minutes.
When the cheese has cooled slightly, add in the almond flour and two of the eggs, and mix well, until a smooth dough remains.
Using your hands, form 10 balls of dough. Place them on the lined tray. Whisk the remaining egg and using a pastry brush, brush the exterior of each of the rolls.
Bake the rolls for 25 minutes, or until golden on the outside. Serve warm.Preheat the oven to 180C/350F. Line a large baking tray with parchment paper and set aside.
In a large, microwave safe bowl, add your shredded cheese and cream cheese. Microwave for 30 seconds, or until the cheeses have mostly melted. Remove from the microwave and whisk together, until smooth. Let the cheese cool for several minutes.
When the cheese has cooled slightly, add in the almond flour and two of the eggs, and mix well, until a smooth dough remains.
Using your hands, form 10 balls of dough. Place them on the lined tray. Whisk the remaining egg and using a pastry brush, brush the exterior of each of the rolls.
Bake the rolls for 25 minutes, or until golden on the outside. Serve warm."""

    testData['notes']= """* Low moisture mozzarella cheese is best, as it has minimal flavor. 
** 2 eggs will be used for the dough, 1 egg for the egg wash on top. 
TO STORE: Leftover rolls can be stored in the refrigerator, covered, for up to 1 week. 
TO FREEZE: Place the cooled rolls in a ziplock bag and store them in the freezer for up to 6 months. Thaw completely before reheating. 
TO REHEAT: You must reheat the rolls, as they are too dense at room temperature/cooled. Either microwave for 30 seconds or place them in a preheated oven until warm."""

    testData['comments'] = """The Big Man’s World ® Arman Liew owns the copyright on all images and text and does not allow for its original recipes, pictures and content to be reproduced anywhere other than this site unless authorization is given. If you enjoyed this recipe and would like to publish it on your own website, please re-write it, in your own words and link back to my site and recipe page. Copying and/or pasting full recipes and pictures to social media or personal blogs is strictly prohibited. Read my disclosure and copyright policy. This post may contain affiliate links.

The Big Man’s World ® Arman Liew owns the copyright on all images and text and does not allow for its original recipes, pictures and content to be reproduced anywhere other than this site unless authorization is given. If you enjoyed this recipe and would like to publish it on your own website, please re-write it, in your own words and link back to my site and recipe page. Copying and/or pasting full recipes and pictures to social media or personal blogs is strictly prohibited. Read my disclosure and copyright policy. This post may contain affiliate links.

ish it on your own website, please re-write it, in your own words and link back to my site and recipe page. Copying and/or pasting full recipes and pictures to social media or personal blogs is strictly prohibited. Read my disclosure and copyright policy. This post may contain affiliate links.

"""
    testData['nutrition'] = """Serving: 1serving | Calories: 203kcal | Carbohydrates: 5g | Protein: 11g | Fat: 17g | Sodium: 222mg | Potassium: 46mg | Fiber: 2g | Vitamin A: 309IU | Calcium: 186mg | Iron: 1mg | NET CARBS: 3g"""

    return testData


def createHTML(html, recipeNameValue, recipeType, recipeImage, formattedIngredients, formattedInstructions, nutrition, formattedNotes, formattedComments):

    recipeHTMLtemplate = Template(html)

    data = recipeHTMLtemplate.substitute(
        {'recipeNameValue': recipeNameValue, 'recipeImage': recipeImage, 'formattedIngredients': formattedIngredients,
         'formattedInstructions': formattedInstructions,'nutrition': nutrition, 'formattedNotes': formattedNotes, 'formattedComments': formattedComments})

    writeRecipeFile(recipeNameValue, recipeType, data)

def writeRecipeFile(recipeNameValue, recipeType, data):
    # import os
    # CURR_DIR = os.getcwd()
    # print("CURR_DIR: " + CURR_DIR)
    # print("CURR_DIR: " + CURR_DIR)
    #
    #
    #
    # print (os.path.abspath(os.curdir))
    #
    # os.chdir("..")
    # print (os.path.abspath(os.curdir))

    fileName = "../html/" + recipeType + "/html/" + recipeNameValue + ".html"
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


def updateIndexTemplate(html, recipeType, recipeNameValue, recipeImage):

    divHTMLtemplate = Template(html)

    data = divHTMLtemplate.substitute(
        {'recipeName': recipeNameValue, 'recipeImage': recipeImage})

    findIndexFile(recipeType,  data)

def findIndexFile(recipeType, data):
    fileName = "../html/" + recipeType + "/" + "index.html"
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

    # print(filedata)

# def resizeImage(recipeImagePath, recipeName):
#     base_width = 800
#     newImagePath = "./images/" + str(recipeName) + ".jpg"
#     image = Image.open(recipeImagePath)
#     width_percent = (base_width / float(image.size[0]))
#     hsize = int((float(image.size[1]) * float(width_percent)))
#     image = image.resize((base_width, hsize), PIL.Image.ANTIALIAS)
#     image.save(newImagePath)
#     return newImagePath

def getResizeDimension(recipeImagePath):

    img = Image.open(recipeImagePath)

    #image size
    width = img.size[0]
    height = img.size[1]

    resizeDimension = {}

    if width == height:
        resizeDimension["top"] = 0
        resizeDimension["bottom"] = height
        resizeDimension['left'] = 0
        resizeDimension['right'] = width
        return resizeDimension

    if width > height:
        cropAmount = (width - height)/2
        resizeDimension["top"] = 0
        resizeDimension["bottom"] = height
        resizeDimension['left'] = cropAmount
        resizeDimension['right'] = width - cropAmount
        return resizeDimension

    if height > width:
        cropAmount = (height - width) / 2
        resizeDimension["top"] = cropAmount
        resizeDimension["bottom"] = height - cropAmount
        resizeDimension['left'] = 0
        resizeDimension['right'] = width
        return resizeDimension


def resizeImage(recipeImagePath, resizeDimension, recipeName):
    newImagePath = "../images/" + str(recipeName) + ".jpg"
    img = Image.open(recipeImagePath)

    left = resizeDimension['left']
    top = resizeDimension['top']
    right = resizeDimension['right']
    bottom = resizeDimension['bottom']

    imgResized = img.crop((left, top, right, bottom))

    imgResized.show()

    # imgResized.save('test-crop-image-' + recipeName + '.jpeg', img.format)
    imgResized.save(newImagePath, img.format)
    return newImagePath