from main import Node, traverse
import copy

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
            node = Node(None, tok.val, d, 'T', tok)
            currNode.addChild(node)

    def empty(currNode):
        d = currNode.depth + 1
        node = Node(None, '@', d, 'T')
        currNode.addChild(node)

    def A():
        return (B(root) and len(input) == 0)

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

        return False

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

        if isType('TYPE'):
            if D(node):
                return K(node)
            return False
        else:
            empty(node)

        return True

    def L(currNode):
        d = currNode.depth + 1
        node = Node(None, "L", d, 'NT')
        currNode.addChild(node)

        if not isVal('}'):
            if M(node):
                return L(node)
            return False
        else:
            empty(node)

        return True

    def M(currNode):
        d = currNode.depth + 1
        node = Node(None, "M", d, 'NT')
        currNode.addChild(node)


        if isVal('{'):
            return J(node)
        elif isVal('if'):
            return O(node)
        elif isVal('while'):
            return P(node)
        elif isVal('return'):
            return Q(node)
        else:
            return N(node)

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

        if isType('IDENTIFIER'):
            accept(node)
            return Rp(node)
        elif isVal('('):
            accept(node)
            if R(node):
                if isVal(')'):
                    accept(node)
                    return Xp(node)and Vp(node) and Tp(node)
        elif isType('NUM_I') or isType('NUM_F'):
            accept(node)
            return Xp(node) and Vp(node) and Tp(node)

        return False

    def Rp(currNode):
        d = currNode.depth + 1
        node = Node(None, "Rp", d, 'NT')
        currNode.addChild(node)

        if isVal('('):
            accept(node)
            if Beta(node):
                if isVal(')'):
                    accept(node)
                    return Xp(node) and Vp(node) and Tp(node)
        elif Sp(node):
            return Re(node)

        return False

    def Re(currNode):
        d = currNode.depth + 1
        node = Node(None, "Re", d, 'NT')
        currNode.addChild(node)

        if isVal('='):
            accept(node)
            return R(node)

        return Xp(node) and Vp(node) and Tp(node)

    def Sp(currNode):
        d = currNode.depth + 1
        node = Node(None, "Sp", d, 'NT')
        currNode.addChild(node)

        if isVal('['):
            accept(node)
            if R(node):
                if isVal(']'):
                    accept(node)
                    return True
            return False
        else:
            empty(node)

        return True

    def Tp(currNode):
        d = currNode.depth + 1
        node = Node(None, "Tp", d, 'NT')
        currNode.addChild(node)

        if U(node):
            return V(node)
        else:
            empty(node)

        return True

    def U(currNode):
        d = currNode.depth + 1
        node = Node(None, "U", d, 'NT')
        currNode.addChild(node)

        if isType('RELOP'):
            accept(node)
            return True

        return False

    def V(currNode):
        d = currNode.depth + 1
        node = Node(None, "V", d, 'NT')
        currNode.addChild(node)

        return X(node) and Vp(node)

    def Vp(currNode):
        d = currNode.depth + 1
        node = Node(None, "Vp", d, 'NT')
        currNode.addChild(node)

        if W(node):
            if X(node):
                return Vp(node)
            return False
        else:
            empty(node)

        return True

    def W(currNode):
        d = currNode.depth + 1
        node = Node(None, "W", d, 'NT')
        currNode.addChild(node)

        if isType('ADDOP'):
            accept(node)
            return True

        return False

    def X(currNode):
        d = currNode.depth + 1
        node = Node(None, "X", d, 'NT')
        currNode.addChild(node)

        return Z(node) and Xp(node)

    def Xp(currNode):
        d = currNode.depth + 1
        node = Node(None, "Xp", d, 'NT')
        currNode.addChild(node)

        if Y(node):
            if Z(node):
                return Xp(node)
            return False
        else:
            empty(node)

        return True

    def Y(currNode):
        d = currNode.depth + 1
        node = Node(None, "Y", d, 'NT')
        currNode.addChild(node)

        if isType('MULOP'):
            accept(node)
            return True

        return False

    def Z(currNode):
        d = currNode.depth + 1
        node = Node(None, "Z", d, 'NT')
        currNode.addChild(node)

        if isVal('('):
            accept(node)
            if R(node):
                if isVal(')'):
                    accept(node)
                    return True
        elif isType('IDENTIFIER'):
            accept(node)
            return Zp(node)
        elif isType('NUM_I') or isType('NUM_F'):
            accept(node)
            return True

        return False

    def Zp(currNode):
        d = currNode.depth + 1
        node = Node(None, "Zp", d, 'NT')
        currNode.addChild(node)

        if isVal('('):
            accept(node)
            if Beta(node):
                if isVal(')'):
                    accept(node)
                    return True
        elif Sp(node):
            return True

        return False

    def Beta(currNode):
        d = currNode.depth + 1
        node = Node(None, "BETA", d, 'NT')
        currNode.addChild(node)

        if Gamma(node):
            return True
        else:
            empty(node)

        return True

    def Gamma(currNode):
        d = currNode.depth + 1
        node = Node(None, "GAMMA", d, 'NT')
        currNode.addChild(node)

        return R(node) and Gammap(node)

    def Gammap(currNode):
        d = currNode.depth + 1
        node = Node(None, "GAMMAp", d, 'NT')
        currNode.addChild(node)

        if isVal(','):
            accept(node)
            if R(node):
                return Gammap(node)
            return False
        else:
            empty(node)

        return True
    # End rules

    if A():
        message = 'Syntax completed successfully.\n'
        syn_pass = True
    else:
        message = 'Error during syntax analysis.\n'
        syn_pass = False

    newRoot = None
    output = traverse(root)

    return message, output, root, syn_pass