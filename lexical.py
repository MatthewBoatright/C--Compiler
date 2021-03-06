'''
Lexical analyzer based off of Eli Bendersky's lex analyzer:
http://eli.thegreenplace.net/2013/06/25/regex-based-lexical-analysis-in-python-and-javascript
'''

import re
from main import Token

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
        # All the regexes are concatenated into a single one
        # with named groups. Since the group names must be valid
        # Python identifiers, but the token types used by the
        # user are arbitrary strings, we auto-generate the group
        # names and map them to token types.
        #
        idx = 1
        regex_parts = []
        self.group_type = {}

        for regex, type in rules:
            groupname = 'GROUP%s' % idx
            regex_parts.append('(?P<%s>%s)' % (groupname, regex))
            self.group_type[groupname] = type
            idx += 1

        self.regex = re.compile('|'.join(regex_parts), re.DOTALL)
        self.skip_whitespace = skip_whitespace
        self.re_ws_skip = re.compile('\S')

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
        else:
            if self.skip_whitespace:
                m = self.re_ws_skip.search(self.buf, self.pos)

                if m:
                    self.pos = m.start()
                else:
                    return None

            m = self.regex.match(self.buf, self.pos)
            if m:
                groupname = m.lastgroup
                tok_type = self.group_type[groupname]
                tok = Token(tok_type, m.group(groupname).strip(), self.pos)
                self.pos = m.end()
                return tok

            # if we're here, no rule matched
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
    ('\d+\.\d+',                                        'NUM_F'),
    ('\d+',                                             'NUM_I'),
    ('int\s|float\s|void\s',                            'TYPE'),
    ('if\s|else\s|while\s|return\s',                    'KEYWORD'),
    ('[a-zA-Z_]\w*',                                    'IDENTIFIER'),
    ('\/\*(.*)\*\/',                                    'COMMENT'),
    ('\+|\-',                                           'ADDOP'),
    ('\*|\/',                                           'MULOP'),
    ('\!\=|\<\=|\>\=|\<|\>|\=\=',                       'RELOP'),
    ('\(',                                              'LP'),
    ('\)',                                              'RP'),
    ('\{',                                              'LC'),
    ('\}',                                              'RC'),
    ('\[',                                              'LB'),
    ('\]',                                              'RB'),
    ('\=',                                              'EQUALS'),
    ('\;',                                              'SEMICOLON'),
    ('\,',                                              'COMMA'),
    ]

    lx = Lexer(rules, skip_whitespace=True)
    lx.input(input)

    message = 'Lexical analysis completed successfully.\n'
    output = ''
    tokens = []

    try:
        for tok in lx.tokens():
            if tok.type != 'COMMENT':
                tokens.append(tok)
                output += str(tok) + '\n'
    except LexerError as err:
        message = 'Error during lexical analysis.\n'
        output += 'LexerError at position %s' % err.pos

    return (message, output, tokens)