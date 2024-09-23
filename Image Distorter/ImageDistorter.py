import os
import pathlib
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

import EffectFinder

#gets path where this file is (and the result path)
path = pathlib.Path(__file__).parent.resolve()
resultpath = os.path.join(path, "Exports/")
effectsPath = os.path.join(path, "Effects/")

previewImage = ImageTk
global editImage

#Main Window
root = Tk()
root.geometry('500x850')# Size of the window
#root.resizable(0, 0) # makes the window adjustable with its features
root.title('Image Distorter')

windowTitle = Label(root, text="Image Distorter",font=("bold",30))
windowTitle.grid(column=1,row=0)

previewImageLabel = Label()
previewImageLabel.grid(column=1,row=1)

hintLabel = Label(root,text="(Image is not to scale and may look different)")
hintLabel.grid(column=1,row=2)

imageSelectButton = Button(root, text="Change Directory", command= lambda:SelectPhoto())
imageSelectButton.grid(column=1,row=3)

effectLabel = Label(root,text="Effects: ")
effectLabel.grid(column=0,row=3)

optionsLabel = Label(root,text="Options: ")
optionsLabel.grid(column=2,row=3)

effectButtons = []
effectCounter = 0

#Generate Effect Buttons
for file in os.listdir(effectsPath):
    if os.path.isfile(effectsPath+file) and file.endswith(".py"):
        effectButtons.append(Button(root, text=(os.path.splitext(file)[0]),command= lambda file=file:AddEffect(file)))
        effectButtons[effectCounter]["state"] = "disabled"
        effectButtons[effectCounter].grid(column=0,row=4+effectCounter)
        effectCounter += 1

exportButton = Button(root, text="Export Image", command= lambda:ExportPhoto())
exportButton["state"] = "disabled"
exportButton.grid(column=2,row=4)

#-----Functions-----
def AddEffect(effect):
    global editImage

    imageSelectButton["state"] = "disabled"
    exportButton["state"] = "disabled"
    for eb in effectButtons:
        eb["state"] = "disabled"
    
    editImage = EffectFinder.executeEffect(editImage,effect)

    imageSelectButton["state"] = "normal"
    exportButton["state"] = "normal"
    for eb in effectButtons:
        eb["state"] = "normal"
        
    CreatePreviewImage()


#Maintenance Functions
def SelectPhoto():
    load = filedialog.askopenfilename()
    global editImage 
    editImage = Image.open(load)
    
    CreatePreviewImage()

    if exportButton["state"] == "disabled":
        exportButton["state"] = "normal"
        for eb in effectButtons:
            eb["state"] = "normal"

def ExportPhoto():
    filename = os.path.basename(editImage.filename)
    editImage.save(resultpath + filename)
    print("exported "+filename)

def CreatePreviewImage():
    previewImage = editImage
    previewImage = previewImage.resize((200,200))
    
    previewImage = ImageTk.PhotoImage(previewImage)
    
    previewImageLabel.configure(image=previewImage)
    previewImageLabel.image = previewImage

root.mainloop()