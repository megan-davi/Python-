"""
Prompt: use a binary tree to decode a string of morse code
"""

import re
import itertools
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


# build the tree
tree = BinaryTree("")
tree.insertLeft("E")
tree.insertRight("T")
tree.getLeftChild().insertLeft("I")
tree.getLeftChild().insertRight("A")
tree.getLeftChild().getLeftChild().insertLeft("S")
tree.getLeftChild().getLeftChild().insertRight("U")
tree.getLeftChild().getLeftChild().getLeftChild().insertLeft("H")
tree.getLeftChild().getLeftChild().getLeftChild().insertRight("V")
tree.getLeftChild().getLeftChild().getRightChild().insertLeft("F")
tree.getLeftChild().getRightChild().insertLeft("R")
tree.getLeftChild().getRightChild().insertRight("W")
tree.getLeftChild().getRightChild().getLeftChild().insertLeft("L")
tree.getLeftChild().getRightChild().getRightChild().insertLeft("P")
tree.getLeftChild().getRightChild().getRightChild().insertRight("J")
tree.getRightChild().insertLeft("N")
tree.getRightChild().insertRight("M")
tree.getRightChild().getLeftChild().insertLeft("D")
tree.getRightChild().getLeftChild().insertRight("K")
tree.getRightChild().getLeftChild().getLeftChild().insertLeft("B")
tree.getRightChild().getLeftChild().getLeftChild().insertRight("X")
tree.getRightChild().getLeftChild().getRightChild().insertLeft("C")
tree.getRightChild().getLeftChild().getRightChild().insertRight("Y")
tree.getRightChild().getRightChild().insertLeft("G")
tree.getRightChild().getRightChild().insertRight("O")
tree.getRightChild().getRightChild().getLeftChild().insertLeft("Z")
tree.getRightChild().getRightChild().getLeftChild().insertRight("Q")

decoded = " "
fileobj = open("in.txt", 'r')

lines = fileobj.readlines()
letters = [elem.rstrip('\n').split(" ") for elem in lines]
letters = sum(word, [])

print(word)
#print(string)

for letter in letters:
# decode(letter)

    
    if character == ".":
        decoded += tree.getLeftChild().getRootVal()
    elif character == "..":
        decoded += tree.getLeftChild().getLeftChild().getRootVal()
    elif character == "...":
        decoded += tree.getLeftChild().getLeftChild().getLeftChild().getRootVal()
    elif character == "....":
        decoded += tree.getLeftChild().getLeftChild().getLeftChild().getLeftChild().getRootVal()
    elif character == "...-":
        decoded += tree.getLeftChild().getLeftChild().getLeftChild().getRightChild().getRootVal()
    elif character == "..-.":
        decoded += tree.getLeftChild().getLeftChild().getRightChild().getLeftChild().getRootVal()
    elif character == "..-":
        decoded += tree.getLeftChild().getLeftChild().getRightChild().getRootVal()
    elif character == ".-":
        decoded += tree.getLeftChild().getRightChild().getRootVal()
    elif character == ".-.":
        decoded += tree.getLeftChild().getRightChild().getLeftChild().getRootVal()
    elif character == ".-..":
        decoded += tree.getLeftChild().getRightChild().getLeftChild().getLeftChild().getRootVal()
    elif character == ".--":
        decoded += tree.getLeftChild().getRightChild().getRightChild().getRootVal()
    elif character == ".--.":
        decoded += tree.getLeftChild().getRightChild().getRightChild().getLeftChild().getRootVal()
    elif character == ".---":
        decoded += tree.getLeftChild().getRightChild().getRightChild().getRightChild().getRootVal()
    elif character == "-":
        decoded += tree.getRightChild().getRootVal()
    elif character == "-.":
        decoded += tree.getRightChild().getLeftChild().getRootVal()
    elif character == "-..":
        decoded += tree.getRightChild().getLeftChild().getLeftChild().getRootVal()
    elif character == "-...":
        decoded += tree.getRightChild().getLeftChild().getLeftChild().getLeftChild().getRootVal()
    elif character == "-..-":
        decoded += tree.getRightChild().getLeftChild().getLeftChild().getRightChild().getRootVal()
    elif character == "-.-":
        decoded += tree.getRightChild().getLeftChild().getRightChild().getRootVal()
    elif character == "-.-.":
        decoded += tree.getRightChild().getLeftChild().getRightChild().getLeftChild().getRootVal()        
    elif character == "-.--":
        decoded += tree.getRightChild().getLeftChild().getRightChild().getRightChild().getRootVal()
    elif character == "--":
        decoded += tree.getRightChild().getRightChild().getRootVal() 
    elif character == "--.":
        decoded += tree.getRightChild().getRightChild().getLeftChild().getRootVal()
    elif character == "---":
        decoded += tree.getRightChild().getRightChild().getRightChild().getRootVal()
    elif character == "--..":
        decoded += tree.getRightChild().getRightChild().getLeftChild().getLeftChild().getRootVal()
    elif character == "--.-":
        decoded += tree.getRightChild().getRightChild().getLeftChild().getRightChild().getRootVal()
    elif character == "":
        decoded += " "
    elif character == "\n":
        decoded += "\n"


print()
print (re.sub(' +', ' ',decoded))



