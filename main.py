'''
Author: Matthew Boatright
Project: C- Compiler
'''

from graphics import *

class Token(object):
    ''' Token structure: Type, Value, Position.
    '''
    def __init__(self, type, val, pos):
        self.type = type
        self.val = val
        self.pos = pos

    def __str__(self):
        return '%4s: %s(%s)' % (self.pos, self.type, self.val)

    def getType(self):
        return self.type

    def getVal(self):
        return self.val

    def getPos(self):
        return self.pos

class Tree(object):
    ''' Tree structure: Parent, Children
    '''
    def __init__(self):
        print 'New tree'
        self.root = Node()

    def addChild(self, node):
        pass

class Node(object):
    ''' Node structure:
    '''
    def __init__(self, tok=None):
        if tok != None:
            self.type = tok.getType()
            self.val = tok.getVal()
            self.pos = tok.getPos()
        self.children = []

    def __str__(self):
        return 'NODE: %10s %10s %10s' % (self.type, self.val, self.pos)

def main():
    construct()

if __name__ == '__main__':
    main()