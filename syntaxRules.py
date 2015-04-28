from syntax import *

def nextTok():
    if (len(input) > 0):
        return input.pop()

def A():
    return B()

def B():
    node = Node(None, 'B', 0, 'NT')
    currNode.addChild(node)
    return C() and Bp()

def Bp():
    return True

def C():
    return True