# C- Compiler
A second go at my compilers course project. This time done in Python.

The (slightly modified) C- language is a subset of C used as a manageable introductory language into compilers/language translators.

The conventions, syntax and semantics of this language can be found in Appendix A of Kenneth C. Louden's Compiler Construction text. I've taken liberty in making some modifications to the language (such as the ability to read floats) that were emphasized in the course.

The lexical conventions are as follows:
* KEYWORDS: int float void if else while return
* SYMBOLS: /* */ + - * / < <= > >= == != = , ; ( ) { } [ ]
* IDENTIFIER: [a-zA-Z_]\w*
* INTEGER: \d+
* FLOAT: \d+\.\d+

The syntax is as follows:
* A 	-> 	B
* B 	-> 	C B’
* B’	->	C B’ | ε
* C 	->	E id C’
* C’	->	D’ | ( G ) J
* D 	-> 	E id D’
* D’	->	; | [ num ] ;
* E	->	int | float | void
* G	->	int id I’ H’ | float id I’ H’ | void G’
* G’	->	id I’ H’ | ε
* H’	->	, I H’ | ε
* I	->	E id I’
* I’	->	[ ] | ε
* J	->	{ K L }
* K	->	D K | ε
* L	->	M L | ε
* M	->	N | J | O |P | Q
* N	->	R ; | ;
* O	->	if ( R ) M O’
* O’	->	else M | ε
* P	->	while ( R ) M
* Q	->	return N
* R	-> 	id R’ | ( R ) X’ V’ T’ | num X’ V’ T’
* R’	->	S’ RΣ | ( ß ) X’ V’ T’
* RΣ	->	= R | X’ V’ T’
* S’	->	[ R ] | ε
* T’	->	U V | ε
* U	->	<= | < | > | >= | == | !=
* V	->	X V’
* V’	->	W X V’ | ε
* W	->	+ | -
* X	->	Z X’
* X’	->	Y Z X’ | ε
* Y	->	* | /
* Z	->	( R ) | id Z’ | num
* Z’ 	->	S’ | ( ß )
* ß	->	Γ | ε
* Γ	->	R Γ’
* Γ’	->	, R Γ’ | ε

Example C- Program:

```
int gcd (int u, int v)
{
	if (v==0) return u;
	else return gcd(v,u-u/v*v);
	/* u-u/v*v == u mod v */
}

void main(void)
{
	int x; int y;
	x = input(); y = input();
	output(gcd(x,y));
}
```
