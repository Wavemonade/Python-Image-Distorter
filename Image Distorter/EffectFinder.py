from tkinter import *
from tkinter import ttk
import os

#I have to do this shit because "from Effects import *" is apparently importing nothing
from Effects import DarkEdgeDefiner
from Effects import GradientCreator
from Effects import Grungeify
from Effects import Invert
from Effects import InvertBlueChannel
from Effects import InvertGreenChannel
from Effects import InvertRedChannel
from Effects import MaximiseBlueChannel
from Effects import MaximiseGreenChannel
from Effects import MaximiseRedChannel
from Effects import MeltDown
from Effects import MeltRight
from Effects import RemoveBlueChannel
from Effects import RemoveGreenChannel
from Effects import RemoveRedChannel
from Effects import ScanLinesEveryPixel
from Effects import ScanLinesHorizontal
from Effects import ScanLinesVertical
from Effects import GaussianBlurSubtract
from Effects import Sharpen
from Effects import LuminosityColorer
from Effects import Vignette
from Effects import GranularGradientCreator


def executeEffect(img,effect):
    
    global im
    im = None

    #i hate this
    match(effect):
        case "DarkEdgeDefiner.py":
            img = DarkEdgeDefiner.execute(img)
        case "GradientCreator.py":
            img = GradientCreator.execute(img)
        case "Grungeify.py":
            img = Grungeify.execute(img)
        case "Invert.py":
            img = Invert.execute(img)
        case "InvertBlueChannel.py":
            img = InvertBlueChannel.execute(img)
        case "InvertGreenChannel.py":
            img = InvertGreenChannel.execute(img)
        case "InvertRedChannel.py":
            img = InvertRedChannel.execute(img)
        case "MaximiseBlueChannel.py":
            img = MaximiseBlueChannel.execute(img)
        case "MaximiseGreenChannel.py":
            img = MaximiseGreenChannel.execute(img)
        case "MaximiseRedChannel.py":
            img = MaximiseRedChannel.execute(img)
        case "MeltDown.py":
            img = MeltDown.execute(img)
        case "MeltRight.py":
            img = MeltRight.execute(img)
        case "RemoveBlueChannel.py":
            img = RemoveBlueChannel.execute(img)
        case "RemoveGreenChannel.py":
            img = RemoveGreenChannel.execute(img)
        case "RemoveRedChannel.py":
            img = RemoveRedChannel.execute(img)
        case "ScanLinesEveryPixel.py":
            img = ScanLinesEveryPixel.execute(img)
        case "ScanLinesHorizontal.py":
            img = ScanLinesHorizontal.execute(img)
        case "ScanLinesVertical.py":
            #attr = dir(ScanLinesVertical)
            img = ScanLinesVertical.execute(img)
        case "GaussianBlurSubtract.py":
            img = GaussianBlurSubtract.execute(img)
        case "Sharpen.py":
            img = Sharpen.execute(img)
        case "LuminosityColorer.py":
            img = LuminosityColorer.execute(img)
        case "Vignette.py":
            img = Vignette.execute(img)
        case "GranularGradientCreator.py":
            img = GranularGradientCreator.execute(img) 
            
    return img
