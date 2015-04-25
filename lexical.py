'''
Lexical analyzer based off of Eli Bendersky's lex analyzer:
http://eli.thegreenplace.net/2013/06/25/regex-based-lexical-analysis-in-python-and-javascript
'''

import re

class Token(object):
    ''' Token structure: Type, Value, Position.
    '''
    def __init__(self, type, val, pos):
        self.type = type
        self.val = val
        self.pos = pos

    def __str__(self):
        return '%s(%s) at %s' % (self.type, self.val, self.pos)

class LexerError(Exception):
    def __init__(self, pos):
        self.pos = pos

class Lexer(object):
    ''' Regex based lexer/analyzer.
    '''
    def __init__(self, rules, skip_whitespace=True):
        '''
        :param rules:
            A list of rules. Each rule is a 'regex, type' pair.
        :param skip_whitespace:
            If True, whitespace (\s+) will be skipped and not
            reported by the lexer. Otherwise you have to
            specify your rules for whitespace, or it will be
            flagged as an error.
        '''
        self.rules = []

        for regex, type in rules:
            self.rules.append((re.compile(regex), type))

        self.skip_whitespace = skip_whitespace
        self.re_ws_skip =  re.compile('\S')

    def input(self, buf):
        ''' Initialize the lexer with a buffer as input
        '''
        self.buf = buf
        self.pos = 0

    def token(self):
        ''' Return the next token (a Token object) found in the
            input buffer. None is returned if the end of the
            buffer was reached.
            In case of a lexing error (the current chunk of the
            buffer matches no rule), a LexerError is raised with
            the position of the error.
        '''
        if self.pos >= len(self.buf):
            return None
        if self.skip_whitespace:
            m = self.re_ws_skip.search(self.buf, self.pos)
            if m:
                self.pos = m.start()
            else:
                return None

        for regex, type in self.rules:
            m = regex.match(self.buf, self.pos)
            if m:
                tok = Token(type, m.group(), self.pos)
                self.pos = m.end()
                return tok

        # If we're here, no rule has been matched
        raise LexerError(self.pos)

    def tokens(self):
        ''' Returns an iterator to the tokens found in the buffer
        '''
        while 1:
            tok = self.token()
            if tok is None: break
            yield tok

def lexical(input):

    rules = [
    ('\d+',             'NUMBER'),
    ('[a-zA-Z_]\w*',    'IDENTIFIER'),
    ('\+',              'PLUS'),
    ('\-',              'MINUS'),
    ('\*',              'MULTIPLY'),
    ('\/',              'DIVIDE'),
    ('\(',              'LP'),
    ('\)',              'RP'),
    ('=',               'EQUALS'),
    ]

    lx = Lexer(rules, skip_whitespace=True)
    lx.input(input)

    output = ''

    try:
        for tok in lx.tokens():
            print(tok)
            output += str(tok) + '\n'
    except LexerError as err:
        print('LexerError at position %s' % err.pos)
        output += 'LexerError at position %s' % err.pos

    return output