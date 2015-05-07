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
'ARRAY_VAR': 'Cannot initialize array with variable length.\n'
}

def semantic(root):
    Symbols = {}
    sym_list = []
    error = ''
    scope = 0
    curr = None
    currTok = None
    currDepth = None
    sem_pass = True

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
        if (sym.name, sym.scope) not in Symbols:
            Symbols[name, scope] = sym
            return True
        else:
            return False

    def quad(scope, op, arg1, arg2, res):
        return '%3s: %5s %10s %10s %10s\n' % (scope, op, arg1, arg2, res)

    sym_traverse(root)
    output = quad('SCP', 'OP', 'ARG1', 'ARG2', 'RES')

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
                size = 4
                sym = Symbol('var', type, name, scope, size)
                if not add(sym):
                    sem_pass = False
                    error = errors['VAR_DEC']
                else:
                    output += quad(scope, 'ALLOC', size, '', name)

            # If a square bracket is next then this is an array declaration
            elif currTok.type == 'LB':
                currTok, currDepth = nextTok()

                size = int(currTok.val) * 4
                sym = Symbol('var', type, name, scope, size)
                if not add(sym):
                    sem_pass = False
                    error = errors['VAR_DEC']
                else:
                    output += quad(scope, 'ALLOC', size, '', name)

        #
        elif currTok.getType() == 'LC':
            scope += 1
        elif currTok.getType() == 'RC':
            scope -= 1

    if sem_pass:
        message = 'Semantic analysis completed successfully.\n'
    else:
        message = 'Error during semantic analysis.\n' + error

    return message + output + str(Symbols.keys())