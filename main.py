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

class Node(object):
    ''' Node structure:
            Val: The name of the node (the rule for terminals or the token value for non-terminals)
            Depth: The depth of the current node (starts at 0)
            Type: Terminal (as 'T') or Non-Terminal (as 'NT')
            Token: A token object (only if the type is NT)
    '''
    c_num = 0

    def __init__(self, parent, val, depth, type, token=None):
        self.parent = parent
        self.val = val
        self.depth = depth
        self.type = type
        if token != None:
            self.token = token
        self.children = []

    def __str__(self):
        return 'NODE: %10s %10s %10s' % (self.val, self.depth, self.type)

    def addChild(self, node):
        self.children.append(node)
        self.c_num += 1

def main():
    construct()

if __name__ == '__main__':
    main()