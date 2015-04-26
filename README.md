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
