# 생각보다 편하군... 2022
# 먼저 다음 2개 ply 와 lex를 미리 INSTALL 해야 한다.
# 중간에 좀 error가 나지만 무시하고 처리해야 한다.


import ply.lex as lex

# List of simple token names.   항상 필요하다.
tokens = (
    'ID',
    'NUMBER',
    'ADDITION',
    'TDIVISION',
    'FDIVISION',
    'BAND',
    'BEOR',
    'BINVERSION',
    'BOR',
    'EXPONENTIATION',
    'ASSIGNMENT',
    'LBRAKET',
    'RBRAKET',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'L_SHIFT',
    'MODULO',
    'MULTIPLI',
    'MMULTIPLI',
    'R_SHIFT',
    'SLICE',
    # 'ignore_COMMENT',
    'SUBTRACTION',
    'ORDERING_A',
    'ORDERING_B',
    'EQUALITY',
    'DIFFERENCE',
    'ORDERING_C',
    'ORDERING_D',
    'QUOTES',
    'DQUOTES',
    'DOT',
    'COMMA'
)

# Regular expression rules for simple tokens
t_ADDITION = r'\+'
t_TDIVISION = r'\/'
t_FDIVISION = r'\/\/'
t_BAND = r'\&'
t_BEOR = r'\^'
t_BINVERSION = r'\~'
t_BOR = r'\|'
t_EXPONENTIATION = r'\*\*'
t_ASSIGNMENT = r'\='
t_LBRAKET = r'\['
t_RBRAKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_L_SHIFT = r'\<\<'
t_MODULO = r'\%'
t_MULTIPLI = r'\*'
t_MMULTIPLI = r'\@'
t_R_SHIFT = r'\>\>'
t_SLICE = r'\:'
t_ignore_COMMENT = r'\#.*'
t_SUBTRACTION = r'\-'
t_ORDERING_A = r'\<'
t_ORDERING_B = r"\<\="
t_EQUALITY = r"\=\="
t_DIFFERENCE = r"\!\="
t_ORDERING_C = r"\>\="
t_ORDERING_D = r"\>"
t_QUOTES = r"\'"
t_DQUOTES = r"\""
t_DOT = r"\."
t_COMMA = r"\,"


# 파이썬 키워드 : 이미 예약되어있는 문자열로서 다른 용도로 사용이 불가능한 문자열
keyword = {'False': 'FALSE', 'None': 'NONE', 'True': 'TRUE',
           'and': 'AND', 'as': 'AS', 'assert': 'ASSERT',
           'break': 'BREAK', 'class': "CLASS", 'continue': 'CONTINUE',
           'def': 'DEF', 'elif': 'ELIF',
           'else': 'ELSE', 'except': 'EXCEPT',
           'finally': 'FINALLY', 'for': 'FOR',
           'from': 'FROM', 'global': 'GLOBAL', 'if': 'IF',
           'import': 'IMPORT', 'lambda': 'LAMBDA', 'nonlocal': 'NONLOCAL',
           'or': 'OR', 'pass': 'PASS', 'raise': 'RAISE',
           'return': 'RETURN', 'with': 'WITH', 'yield': 'YIELD',
           'try': 'TRY', 'while': 'WHILE'}
# print("keyword.values():", keyword.values())

operator = {'add': 'ADD', 'concat': 'CONCAT', 'in': 'IN', 'contains': 'CONTAINS',
            'truediv': 'TRUEDIV', 'floordiv': 'FLOORDIV', 'and_': 'AND_',
            'xor': 'XOR', 'invert': "INVERT", 'or_': 'OR_',
            'pow': 'POW', 'is_': 'IS_', 'is_not': 'IS_NOT',
            'setitem': 'SETITEM', 'delitem': 'DELITEM',
            'getitem': 'GETITEM', 'lshift': 'LSHIFT',
            'mod': 'MOD', 'mul': 'MUL', 'matmul': 'MATMUL',
            'neg': 'NEG', 'not_': 'NOT_', 'pos': 'POS',
            'rshift': 'RSHIFT', 'setitem': 'SETITEM', 'delitem': 'DELITEM',
            'getitem': 'GETITEM', 'mod': 'MOD', 'sub': 'SUB',
            'truth': 'TRUTH', 'lt': 'LT', 'le': 'LE',
            'eq': 'EQ', 'ne': 'NE', 'ge': 'GE', 'gt': 'GT',
            'is': 'IS', 'not': 'NOT', 'del': 'DEL'}

tokens = list(tokens) + list(keyword.values()) + list(operator.values())

print(tokens)

# 특정한 A regular expression과 일치한 token을 찾았을 때의 동작


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keyword.get(t.value, 'ID')
    return t

# comment 문장은 모두 pass를 이용하여


# def t_COMMENT(t):
#     r'\/\/.*'
#     pass  # ignore_ prefix 사용


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'  # A string containing ignored characters (spaces and tabs)


def t_error(t):  # Error handling rule
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# ------------ 수행을 해보자. ------------


lexer = lex.lex()  # Build the lexer

data = '''
num = int(input())
i=0

def is2(line,L,R):
    front = True
    rear = True
    L1 = L+1
    R1 = R-1
    while (L1 < R):
        if (line[L1] == line[R]):
            L1 = L1+1
            R = R-1
        else:
            front = False
            break
    while (L<R1):
        if(line[L] == line[R1]):
            L = L+1
            R1 = R1-1
        else:
            rear = False
            break
    return front or rear

while i<num:
    line= input().rstrip("\n")
    line = ''.join(filter(str.isalnum, line))
    L = 0
    R = len(line)-1
    while (L < R):
        if (line[L] == line[R]):
            L = L+1
            R = R-1
        else:
            if(is2(line,L,R)):
                print(2)
                break
            else:
                print(3)
                break
    if(L>=R):
        print(1)
    i = i+1


'''

# data = data.lower()


# data = '''          # Test it out
# template<typename T>
# std::vector<T> slice(std::vector<T> const &v, int m, int n) {
#     auto first = v.cbegin() + m;
#     auto last = v.cbegin() + n + 1;

#     // comment example

#     std::vector<T> vec(first, last);
#     return vec;
# }

# '''

# Give the lexer some input
lexer.input(data)

a = 0
n_KEYWORD = 0
n_ID = 0
n_NUMBER = 0
n_OPERATOR = 0
n_SEPARATOR = 0
n_LDEPTH = 0
n_RDEPTH = 0
n_DEPTH_COUNTS = 0
while True:
    tok = lexer.token()
    # print(tok)

    if not tok:
        break      # No more input

    # print(tok.type)

    if tok.type in keyword.values():
        n_KEYWORD += 1

    if tok.type == 'ID':
        n_ID += 1

    if tok.type == 'NUMBER':
        n_NUMBER += 1

    if tok.type in operator.values():
        n_OPERATOR += 1

    if tok.type == 'ADDITION':
        n_OPERATOR += 1

    if tok.type == 'TDIVISION':
        n_OPERATOR += 1

    if tok.type == 'FDIVISION':
        n_OPERATOR += 1

    if tok.type == 'BAND':
        n_OPERATOR += 1

    if tok.type == 'BEOR':
        n_OPERATOR += 1

    if tok.type == 'BINVERSION':
        n_OPERATOR += 1

    if tok.type == 'BOR':
        n_OPERATOR += 1

    if tok.type == 'EXPONENTIATION':
        n_OPERATOR += 1

    if tok.type == 'ASSIGNMENT':
        n_OPERATOR += 1

    if tok.type == 'LBRAKET':
        n_OPERATOR += 1

    if tok.type == 'RBRAKET':
        n_OPERATOR += 1

    if tok.type == 'L_SHIFT ':
        n_OPERATOR += 1

    if tok.type == 'MODULO':
        n_OPERATOR += 1

    if tok.type == 'MULTIPLI':
        n_OPERATOR += 1

    if tok.type == 'MMULTIPLI':
        n_OPERATOR += 1

    if tok.type == 'R_SHIFT':
        n_OPERATOR += 1

    # if tok.type == 'ignore_COMMENT':
    #     n_OPERATOR += 1

    if tok.type == 'SUBTRACTION':
        n_OPERATOR += 1

    if tok.type == 'ORDERING_A':
        n_OPERATOR += 1

    if tok.type == 'ORDERING_B':
        n_OPERATOR += 1

    if tok.type == 'EQUALITY':
        n_OPERATOR += 1

    if tok.type == 'DIFFERENCE':
        n_OPERATOR += 1

    if tok.type == 'ORDERING_C':
        n_OPERATOR += 1

    if tok.type == 'ORDERING_D':
        n_OPERATOR += 1

    if tok.type == 'LPAREN':
        n_OPERATOR += 1

    if tok.type == 'RPAREN':
        n_OPERATOR += 1

    if tok.type == 'SLICE':
        n_SEPARATOR += 1

    if tok.type == 'LBRACE':
        n_SEPARATOR += 1
        n_LDEPTH += 1

    if tok.type == 'RBRACE':
        n_SEPARATOR += 1
        n_RDEPTH += 1
        if n_LDEPTH == n_RDEPTH:
            n_DEPTH_COUNTS += 1

    if tok.type == 'DOT':
        n_SEPARATOR += 1

    if tok.type == 'COMMA':
        n_SEPARATOR += 1

    if tok.type == 'DQUOTES':
        n_SEPARATOR += 1

    if tok.type == 'QUOTES':
        n_SEPARATOR += 1

    a += 1

if n_DEPTH_COUNTS != 0:
    average_DEPTH = n_LDEPTH/n_DEPTH_COUNTS
else:
    average_DEPTH = 0

    # tok.type, tok.value, tok.lineno, tok.lexpos
    # print(tok.type)
    # print(tok.value)

print('while total :', a)
print("sum :", n_KEYWORD + n_ID + n_NUMBER + n_OPERATOR + n_SEPARATOR)
print("n_KEYWORD :", n_KEYWORD)
print("n_ID :", n_ID)
print("n_NUMBER :", n_NUMBER)
print("n_OPERATOR :", n_OPERATOR)
print("n_SEPARATOR :", n_SEPARATOR)
print("average DEPTH :", average_DEPTH)
