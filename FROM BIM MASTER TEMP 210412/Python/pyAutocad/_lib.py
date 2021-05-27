import json, os, sys
import numpy as np
import matplotlib

def sayHello():
    print("Hello")


class cadExtractor:
    fileName = ""
    def __init__(self):
        self.askPath()
        if len( self.fileName) > 0:
            print( self.fileName)   
    def askPath(self):
        self.fileName = input("File Name Path: ")