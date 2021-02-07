# Import Module
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import globalUtils
import platform

print(platform.sys.version_info)

global recipeImage

root = tk.Tk()
root.title("Create a Recipe Webpage")

rowCnt = 0
lblHeader = tk.Label(root, text='  Create Recipe Webpage  ', relief='sunken', fg='blue')
lblHeader.config(font=('helvetica', 32, 'bold'))
lblHeader.grid(row=rowCnt, sticky="n", padx=20, pady=20, columnspan=3)

rowCnt += 1

lblRecipeName = tk.Label(root, text="Recipe Name: ")
lblRecipeName.config(font=('helvetica', 16,'bold'))
lblRecipeName.grid(row=rowCnt, column=0, padx=5, pady=5)
recipeName = tk.StringVar()
entryRecipeName = tk.Entry(root, textvariable=recipeName, width=50)
entryRecipeName.grid(row=rowCnt, column=1, padx=5, pady=5, sticky="w")
rowCnt += 1

btnGetImage = tk.Button(root, text="Select Image", fg="black", command=lambda: globalUtils.getRecipeImage(recipeImage))
btnGetImage.grid(row=rowCnt, column=0, padx=5, pady=5)
recipeImage = tk.StringVar()
entRecipeImage = tk.Entry(root, textvariable=recipeImage, width=50)
entRecipeImage.grid(row=rowCnt, column=1, padx=5, pady=5, sticky="w")
rowCnt += 3

cmbIngredientsFrame = ttk.LabelFrame(root, text="Ingredients")
cmbIngredientsFrame.grid(row=rowCnt, column=0, columnspan=5, padx=5, pady=5, sticky='w')
ingredients = tk.StringVar()
entryIngredients = tk.scrolledtext.ScrolledText(cmbIngredientsFrame, height=10, width= "95" )
entryIngredients.grid(row=rowCnt, column=0, padx=5, pady=5, columnspan=5, sticky='w')
entryIngredients.focus_set()

rowCnt += 1

cmbInstructionsFrame = ttk.LabelFrame(root, text="Instructions:")
cmbInstructionsFrame.grid(row=rowCnt, column=0, columnspan=5, padx=5, pady=10, sticky='w')
instructions = tk.StringVar()
entryInstructions = tk.scrolledtext.ScrolledText(cmbInstructionsFrame, height=10, width= "95" )
entryInstructions.grid(row=rowCnt, column=0, padx=5, pady=5, columnspan=10, sticky='w')
entryInstructions.focus_set()

rowCnt += 1

cmbNutritionFrame = ttk.LabelFrame(root, text="Nutrition:")
cmbNutritionFrame.grid(row=rowCnt, column=0, columnspan=5, padx=5, pady=10, sticky='w')
nutrition = tk.StringVar()
entryNutrition = tk.scrolledtext.ScrolledText(cmbNutritionFrame, height=10, width= "95" )
entryNutrition.grid(row=rowCnt, column=0, padx=5, pady=5, columnspan=10, sticky='w')
entryNutrition.focus_set()

rowCnt += 1


btnCreate = tk.Button(root, text="Create Webpage", fg="blue",
                   command=lambda: globalUtils.createWebPage(recipeName, recipeImage, entryIngredients, entryInstructions,entryNutrition))
btnCreate.grid(row=rowCnt, column=2, padx=5, pady=5)

root.mainloop()
