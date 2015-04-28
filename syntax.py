from main import Node

def syntax(input):

    input.reverse()
    root = Node(None, 'A', 0, 'NT')

    # Rules
    def isType(type_check):
        if len(input) > 0:
            return input[-1].getType() == type_check
        return False

    def isVal(val_check):
        if len(input) > 0:
            return input[-1].getVal() == val_check
        return False

    def accept(currNode):
        if len(input) > 0:
            tok = input.pop()
            d = currNode.depth + 1
            node = Node(tok, tok.val, d, 'T')
            currNode.addChild(node)

    def empty(currNode):
        d = currNode.depth + 1
        node = Node(None, u"\u03B5", d, 'T')
        currNode.addChild(node)

    def A():
        return B(root)

    def B(currNode):
        d = currNode.depth + 1
        node = Node(None, "B", d, 'NT')
        currNode.addChild(node)

        return C(node) and Bp(node)

    def Bp(currNode):
        d = currNode.depth + 1
        node = Node(None, "Bp", d, 'NT')
        currNode.addChild(node)

        empty(node)

        return True

    def C(currNode):
        d = currNode.depth + 1
        node = Node(None, "C", d, 'NT')
        currNode.addChild(node)

        if E(node):
            if isType('IDENTIFIER'):
                accept(node)
                return Dp(node)

        return False

    def Cp(currNode):
        d = currNode.depth + 1
        node = Node(None, "Cp", d, 'NT')
        currNode.addChild(node)

        if isVal('('):
            accept(node)
            if G(node):
                if isVal(')'):
                    accept(node)
                    return True
        else: return Dp(node)

    def D(currNode):
        pass

    def Dp(currNode):
        d = currNode.depth + 1
        node = Node(None, "Dp", d, 'NT')
        currNode.addChild(node)

        if isVal(';'):
            accept(node)
            return True
        elif isVal('['):
            accept(node)
            if isType('NUM_I'):
                accept(node)
                if isVal(']'):
                    accept(node)
                    if isVal(';'):
                        accept(node)
                        return True

        return False

    def E(currNode):
        d = currNode.depth + 1
        node = Node(None, "E", d, 'NT')
        currNode.addChild(node)

        if isType('TYPE'):
            accept(node)
            return True
        return False

    def G(currNode):
        d = currNode.depth + 1
        node = Node(None, "G", d, 'NT')
        currNode.addChild(node)

        if isType('TYPE'):
            accept(node)
            return True
        return False
    # End rules

    if A():
        message = 'Syntax completed successfully.\n'
    else:
        message = 'Error during syntax analysis.\n'
    output = traverse(root)

    return message, output

def traverse(currNode):
    line = ''

    if currNode.depth > 0:
        line += '|'
    for x in range (0, currNode.depth):
        line += '_'

    line += currNode.val + '\n'

    if currNode.c_num > 0:
        currNode.children.reverse()
        for x in range (0, currNode.c_num):
            line += traverse(currNode.children.pop())

    return line