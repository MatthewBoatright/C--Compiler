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

        if isType('TYPE'):
            if C(node):
                Bp(node)
            else:
                return False
        else:
            empty(node)

        return True

    def C(currNode):
        d = currNode.depth + 1
        node = Node(None, "C", d, 'NT')
        currNode.addChild(node)

        if E(node):
            if isType('IDENTIFIER'):
                accept(node)
                return Cp(node)

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
                    return J(node)
        else:
            return Dp(node)

    def D(currNode):
        d = currNode.depth + 1
        node = Node(None, "D", d, 'NT')
        currNode.addChild(node)

        if E(node):
            if isType('IDENTIFIER'):
                accept(node)
                return Dp(node)

        return False

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

        if isVal('void'):
            accept(node)
            return Gp(node)
        elif isVal('int') or isVal('float'):
            accept(node)
            if isType('IDENTIFIER'):
                accept(node)
                return Ip(node) and Hp(node)

    def Gp(currNode):
        d = currNode.depth + 1
        node = Node(None, "Gp", d, 'NT')
        currNode.addChild(node)

        if isType('IDENTIFIER'):
            return Ip(node) and Hp(node)
        else:
            empty(node)

        return True

    def Hp(currNode):
        d = currNode.depth + 1
        node = Node(None, "Hp", d, 'NT')
        currNode.addChild(node)

        if isVal(','):
            accept(node)
            return I(node) and Hp(node)
        else:
            empty(node)

        return True

    def I(currNode):
        d = currNode.depth + 1
        node = Node(None, "I", d, 'NT')
        currNode.addChild(node)

        if E(node):
            if isType('IDENTIFIER'):
                accept(node)
                return Ip(node)

        return False

    def Ip(currNode):
        d = currNode.depth + 1
        node = Node(None, "Ip", d, 'NT')
        currNode.addChild(node)

        if isVal('['):
            accept(node)
            if isVal(']'):
                accept(node)
                return True
            else:
                return False
        else:
            empty(node)

        return True

    def J(currNode):
        d = currNode.depth + 1
        node = Node(None, "J", d, 'NT')
        currNode.addChild(node)

        if isVal('{'):
            accept(node)
            if K(node) and L(node):
                if isVal('}'):
                    accept(node)
                    return True

        return False

    def K(currNode):
        d = currNode.depth + 1
        node = Node(None, "K", d, 'NT')
        currNode.addChild(node)

        if D(node):
            return K(node)
        else:
            empty(node)

        return True

    def L(currNode):
        d = currNode.depth + 1
        node = Node(None, "L", d, 'NT')
        currNode.addChild(node)

        if M(node):
            return L(node)
        else:
            empty(node)

        return True

    def M(currNode):
        d = currNode.depth + 1
        node = Node(None, "M", d, 'NT')
        currNode.addChild(node)

        if N(node) or J(node) or O(node) or P(node) or Q(node):
            return True

        return False

    def N(currNode):
        d = currNode.depth + 1
        node = Node(None, "N", d, 'NT')
        currNode.addChild(node)

        if isVal(';'):
            accept(node)
            return True
        elif R(node):
            if isVal(';'):
                accept(node)
                return True

        return False

    def O(currNode):
        d = currNode.depth + 1
        node = Node(None, "O", d, 'NT')
        currNode.addChild(node)

        if isVal('if'):
            accept(node)
            if isVal('('):
                accept(node)
                if R(node):
                    if isVal(')'):
                        accept(node)
                        return M(node) and Op(node)

        return False

    def Op(currNode):
        d = currNode.depth + 1
        node = Node(None, "Op", d, 'NT')
        currNode.addChild(node)

        if isVal('else'):
            accept(node)
            return M(node)
        else:
            empty(node)

        return True

    def P(currNode):
        d = currNode.depth + 1
        node = Node(None, "P", d, 'NT')
        currNode.addChild(node)

        if isVal('while'):
            accept(node)
            if isVal('('):
                accept(node)
                if R(node):
                    if isVal(')'):
                        accept(node)
                        return M(node)

        return False

    def Q(currNode):
        d = currNode.depth + 1
        node = Node(None, "Q", d, 'NT')
        currNode.addChild(node)

        if isVal('return'):
            accept(node)
            return Qp(node)

        return False

    def Qp(currNode):
        d = currNode.depth + 1
        node = Node(None, "Qp", d, 'NT')
        currNode.addChild(node)

        if isVal(';'):
            accept(node)
            return True
        elif R(node):
            if isVal(';'):
                accept(node)
                return True

        return False

    def R(currNode):
        d = currNode.depth + 1
        node = Node(None, "R", d, 'NT')
        currNode.addChild(node)

    def Rp(currNode):
        pass

    def Re(currNode):
        pass

    def Sp(currNode):
        pass

    def Tp(currNode):
        pass

    def U(currNode):
        pass

    def V(currNode):
        pass

    def Vp(currNode):
        pass

    def W(currNode):
        pass

    def X(currNode):
        pass

    def Xp(currNode):
        pass

    def Y(currNode):
        pass

    def Z(currNode):
        pass

    def Zp(currNode):
        pass

    def Beta(currNode):
        pass

    def Gamma(currNode):
        pass

    def Gammap(currNode):
        pass
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