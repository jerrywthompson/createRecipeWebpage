# Import Module
# import matplotlib
# matplotlib.use('Agg')
import os
import tkinter as tk
from tkinter import ttk, scrolledtext
import globalUtils
import platform

print("displayjt: " + str(os.environ.get('DISPLAY','')) )

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


print(platform.sys.version_info)

global recipeImage

root = tk.Tk()
root.title("Create a Recipe Webpage")

root.columnconfigure((0, 1, 2, 3), weight=0)
root.rowconfigure(0, weight=0)

rowCnt = 0
lblHeader = tk.Label(root, text='  Create Recipe Webpage  ', fg='blue')
lblHeader.config(font=('helvetica', 32, 'bold'))
lblHeader.grid(row=rowCnt, sticky="n", padx=20, pady=20, columnspan=3)

rowCnt += 1

lblRecipeName = tk.Label(root, text="Recipe Name: ")
lblRecipeName.config(font=('helvetica', 16,'bold'))
lblRecipeName.grid(row=rowCnt, column=0, padx=5, pady=5)
recipeName = tk.StringVar()
entryRecipeName = tk.Entry(root, textvariable=recipeName, width=50)
entryRecipeName.grid(row=rowCnt, column=1, padx=5, pady=5, columnspan=3, sticky="w")
rowCnt += 1

recipeType = tk.StringVar(None, "main_course")
appetizers = tk.Radiobutton(root, text="Appitizers", variable=recipeType, value='appetizers')
appetizers.grid(row=rowCnt, column=0, sticky='w')
main_course = tk.Radiobutton(root, text="Main Course", variable=recipeType, value='main_course')
main_course.grid(row=rowCnt, column=1, sticky='w')
desserts = tk.Radiobutton(root, text="Desserts", variable=recipeType, value='desserts')
desserts.grid(row=rowCnt, column=2, sticky='w')
cocktails = tk.Radiobutton(root, text="Cocktails", variable=recipeType, value='cocktails')
cocktails.grid(row=rowCnt, column=3, sticky='w')


rowCnt += 1
btnGetImage = tk.Button(root, text="Select Image", fg="black", command=lambda: globalUtils.getRecipeImage(recipeImage))
btnGetImage.grid(row=rowCnt, column=0, padx=5, pady=5)
recipeImage = tk.StringVar()
entRecipeImage = tk.Entry(root, textvariable=recipeImage, width=50)
entRecipeImage.grid(row=rowCnt, column=1, padx=5, pady=5, sticky="w", columnspan=4)
rowCnt += 3

cmbIngredientsFrame = ttk.LabelFrame(root, text="Ingredients")
cmbIngredientsFrame.grid(row=rowCnt, column=0, columnspan=5, padx=5, pady=5, sticky='w')
ingredients = tk.StringVar()
entryIngredients = tk.scrolledtext.ScrolledText(cmbIngredientsFrame, height=5, width= "95" )
entryIngredients.grid(row=rowCnt, column=0, padx=5, pady=5, columnspan=5, sticky='w')
entryIngredients.focus_set()
rowCnt += 1

cmbInstructionsFrame = ttk.LabelFrame(root, text="Instructions:")
cmbInstructionsFrame.grid(row=rowCnt, column=0, columnspan=5, padx=5, pady=10, sticky='w')
instructions = tk.StringVar()
entryInstructions = tk.scrolledtext.ScrolledText(cmbInstructionsFrame, height=5, width= "95" )
entryInstructions.grid(row=rowCnt, column=0, padx=5, pady=5, columnspan=10, sticky='w')
entryInstructions.focus_set()
rowCnt += 1

cmbNutritionFrame = ttk.LabelFrame(root, text="Nutrition:")
cmbNutritionFrame.grid(row=rowCnt, column=0, columnspan=5, padx=5, pady=10, sticky='w')
nutrition = tk.StringVar()
entryNutrition = tk.scrolledtext.ScrolledText(cmbNutritionFrame, height=5, width= "95" )
entryNutrition.grid(row=rowCnt, column=0, padx=5, pady=5, columnspan=10, sticky='w')
entryNutrition.focus_set()
rowCnt += 1

cmbNotesFrame = ttk.LabelFrame(root, text="Notes:")
cmbNotesFrame.grid(row=rowCnt, column=0, columnspan=5, padx=5, pady=10, sticky='w')
entryNotes = tk.StringVar()
entryNotes = tk.scrolledtext.ScrolledText(cmbNotesFrame, height=5, width= "95" )
entryNotes.grid(row=rowCnt, column=0, padx=5, pady=5, columnspan=10, sticky='w')
entryNotes.focus_set()
rowCnt += 1

cmbCommentsFrame = ttk.LabelFrame(root, text="Comments:")
cmbCommentsFrame.grid(row=rowCnt, column=0, columnspan=5, padx=5, pady=10, sticky='w')
comments = tk.StringVar()
entryComments = tk.scrolledtext.ScrolledText(cmbCommentsFrame, height=5, width= "95" )
entryComments.grid(row=rowCnt, column=0, padx=5, pady=5, columnspan=10, sticky='w')
entryComments.focus_set()
rowCnt += 1


btnCreate = tk.Button(root, text="Create Webpage", fg="blue",
                      command=lambda: globalUtils.createWebPage(recipeName, recipeType, recipeImage, entryIngredients, entryInstructions, entryNutrition, entryNotes, entryComments))
btnCreate.grid(row=rowCnt, column=2, padx=5, pady=5)

root.mainloop()
