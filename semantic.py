import copy

class Symbol(object):
    ''' Symbol structure: Meta, Type, Name, Scope, Size, Params, Args
    '''

    def __init__(self, meta, type, name, scope, size=None, params=None, args=None):
        self.meta = meta
        self.type = type
        self.name = name
        self.scope = scope
        self.size = size
        self.params = params
        self.args = args

    def __str__(self):
        if self.meta == 'var':
            # XXX: VAR type name - size
            return '%2s: %s %s %s, SIZE: %s' % (self.scope, self.meta, self.type, self.name, self.size)
        elif self.meta == 'func':
            # XXX: FUNC type name - params
            return '%2s: %s %s %s , PARAMS: %s' % (self.scope, self.meta, self.type, self.name, self.params)

# Error messages
errors = {
'VAR_DEC': 'Variable already declared.\n',
'FUNC_DEC': 'Function already declared.\n',
'ARRAY_VAR': 'Cannot initialize array with variable length.\n',
'NULL_VAR': 'Referenced variable not found.\n',
'NULL_FUNC': 'Referenced function not found.\n',
}

# Globals
line = 0

def semantic(root):

    Symbols = {}
    sym_list = []
    error = ''
    scope = 0
    curr = None
    currTok = None
    currDepth = None
    sem_pass = True
    global line
    line = 0

    def sym_traverse(currNode):

        if currNode.type == 'T':
            if currNode.val != '@':
                sym_list.append([currNode.depth, currNode.token])

        if currNode.c_num > 0:
            currNode.children.reverse()
            copy_list = copy.deepcopy(currNode.children)
            for x in range(0, currNode.c_num):
                sym_traverse(copy_list.pop())

    def nextTok():
        if len(sym_list) > 0:
            curr = sym_list.pop()
            return curr.pop(), curr.pop()
        else:
            return None, None

    def add(sym):
        #print '\nCurrent symbols:\n %s' % str(Symbols)
        #print 'Adding symbol: %s' % sym
        if sym.scope not in Symbols:
            Symbols[sym.scope] = {sym.name: sym}
            #print 'Added new scope:\n %s\n' % str(Symbols)
            return True
        elif sym.name not in Symbols[sym.scope]:
            Symbols[sym.scope][sym.name] = sym
            #print 'Added to current scope:\n %s\n' % str(Symbols)
            return True
        else:
            #print 'Failed add:\n %s\n' % str(Symbols)
            return False

    def addOutput(msg):
        global line
        line += 1
        return '%3s: %s' % (line, msg)

    def quadhead(scope, op, arg1, arg2, res):
        return '%3s: %5s %10s %10s %10s\n' % (scope, op, arg1, arg2, res)

    def quad(op, arg1, arg2, res):
        return '%5s %10s %10s %10s\n' % (op, arg1, arg2, res)

    def varDec(type, name, _scope):
        size = 4
        sym = Symbol('var', type, name, _scope, size)
        if not add(sym):
            error = errors['VAR_DEC']
            return False, error
        else:
            return True, quad('ALLOC', size, '', name)

    def arrayDec(type, name, _scope):
        currTok, currDepth = nextTok()
        nextTok()   # RB ]

        size = int(currTok.val) * 4
        sym = Symbol('var', type, name, _scope, size)
        if not add(sym):
            error = errors['VAR_DEC']
            return False, error
        else:
            return True, quad('ALLOC', size, '', name)

    def funcDec(func):
        if not add(func):
            error = errors['FUNC_DEC']
            return False, error
        else:
            return True, quad('FUNC', func.name, func.type, func.params)

    def eval(exp_list):
        max_i = 0
        max_d = -1
        max_tok = ''
        do = False

        for i, entry in enumerate(exp_list):
            print str(entry[0]) + ' ' + str(entry[1])

            d = entry[0]
            tok = entry[1]

            if d >= max_d:
                max_i = i
                max_d = d
                max_tok = tok
            else:
                do = True

            if do or i == len(exp_list) - 1:
                one = exp_list[max_i - 2]
                two = exp_list[max_i - 1]
                three = exp_list[max_i]

                print '%s %s %s' % (str(one), str(two), str(three))
                del exp_list[max_i]
                del exp_list[max_i - 1]
                exp_list[max_i - 2] = [one[0], 'temp']

                return exp_list


    sym_traverse(root)
    output = quadhead('LNE', 'OP', 'ARG1', 'ARG2', 'RES')

    sym_list.reverse()
    while (len(sym_list) > 0 and sem_pass == True):
        currTok, currDepth = nextTok()

        # Array/Function Declaration
        if currTok.getType() == 'TYPE':

            # TYPE (int, float or void)
            type = currTok.val
            currTok, currDepth = nextTok()

            # NAME
            name = currTok.val
            currTok, currDepth = nextTok()

            # If semicolon is next, then this is a variable declaration
            if currTok.type == 'SEMICOLON':
                sem_pass, msg = varDec(type, name, scope)
                if sem_pass:
                    output += addOutput(msg)
                else:
                    error = msg

            # If a square bracket is next then this is an array declaration
            elif currTok.type == 'LB':
                sem_pass, msg = arrayDec(type, name, scope)
                nextTok()   # SEMICOLON ;
                if sem_pass:
                    output += addOutput(msg)
                else:
                    error = msg

            # If an open parenthesis then this is a function declaration
            elif currTok.type == 'LP':
                params = 0
                fname = name
                ftype = type
                var_list = []
                currTok, currDepth = nextTok()

                while (currTok.type != 'RP'):
                    # Check to see if at the start of declaration
                    if currTok.type == 'TYPE':
                        # TYPE
                        type = currTok.val
                        currTok, currDepth = nextTok()

                        # Break if end of parameters
                        if currTok.type == 'RP':
                            break

                        # NAME
                        elif currTok.type == 'IDENTIFIER':
                            params += 1
                            name = currTok.val

                            sem_pass, msg = varDec(type, name, (int(scope) + 1))
                            if sem_pass:
                                var_list.append(msg)
                            else:
                                error = msg
                                print error

                    currTok, currDepth = nextTok()


                func = Symbol('func', ftype, fname, scope, params=params)
                sem_pass, msg = funcDec(func)

                if sem_pass:
                    output += addOutput(msg)

                    if len(var_list) > 0:
                        output += addOutput(quad('PARAM', '', '', ''))
                        var_list.reverse()
                        while var_list:
                            output += addOutput(var_list.pop())

                else:
                    error = msg

        # Variable/Function reference
        elif currTok.type == 'IDENTIFIER':

            # NAME
            exp_list = []
            name = currTok.val
            currTok, currDepth = nextTok()

            # If = then var reference
            if currTok.type == 'EQUALS':

                # Expression
                currTok, currDepth = nextTok()
                while currTok.type != 'SEMICOLON':
                    if currTok.type != 'LP' and currTok.type != 'RP':
                        exp_list.append([currDepth, currTok])
                    currTok, currDepth = nextTok()

                # Evaluate
                while len(exp_list) > 1:
                    exp_list = eval(exp_list)

                print '\n'

        # Scope change
        elif currTok.getType() == 'LC':
            scope += 1
        elif currTok.getType() == 'RC':
            print 'Removing symbols from scope %s' % scope
            Symbols.pop(scope, None)
            print Symbols
            scope -= 1

    if sem_pass:
        message = 'Semantic analysis completed successfully.\n'
    else:
        message = 'ERROR: ' + error

    return message + output