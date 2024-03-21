# 생각보다 편하군... 2022
# 먼저 다음 2개 ply 와 lex를 미리 INSTALL 해야 한다.
# 중간에 좀 error가 나지만 무시하고 처리해야 한다.


import ply.lex as lex

# List of simple token names.   항상 필요하다.
tokens = (
    'ID',
    'NUMBER',
    'LBRAKET',
    'RBRAKET',
    'LPAREN',
    'RPAREN',
    'DOT',
    'POINTER',
    'INCREASE',
    'DECREASE',
    'AMPERSAND',
    'TIMES',
    'PLUS',
    'MINUS',
    'NOT',
    'EXCLAMATION_MARK',
    'DIVIDE',
    'EQUAL',
    'PERCENT',
    'LSHIFT',
    'RSHIFT',
    'LESS',
    'GTE',
    'MORETHAN',
    'LESSTHAN',
    'EQUALITY',
    'VBAR',
    'BEOR',
    'MEANTIME',
    'OR',
    'COMMA',
    'QUESTION_MARK',
    'COLON',
    'SEMICOL',
    'LBRACE',
    'RBRACE',
    'DECLARE',
    'DOUBLE_QUOTES',
    'QUOTES'
)

# Regular expression rules for simple tokens
# OPERATOR
t_LBRAKET = r'\['
t_RBRAKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_POINTER = r'\-\>'
t_INCREASE = r'\+\+'
t_DECREASE = r'\-\-'
t_AMPERSAND = r'\&'
t_TIMES = r'\*'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_NOT = r'\~'
t_EXCLAMATION_MARK = r"\!"
t_DIVIDE = r'\/'
t_EQUAL = r'\='
t_PERCENT = r"\%"
t_LSHIFT = r'\<\<'
t_RSHIFT = r'\>\>'
t_LESS = r'\<'
t_GTE = r'\>'
t_MORETHAN = r'\>\='
t_LESSTHAN = r'\<\='
t_EQUALITY = r'\=\='
t_VBAR = r"\|"
t_BEOR = r'\^'
t_MEANTIME = r'\&\&'
t_OR = r'\|\|'
t_COMMA = r'\,'
t_QUESTION_MARK = r'\?'

# SEPARATOR
t_COLON = r'\:'
t_SEMICOL = r'\;'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DECLARE = r'\#'
t_DOUBLE_QUOTES = r"\""
t_QUOTES = r"\'"
# t_DCOL = r'\:\:'
# t_ignore_COMMENT = r'\#.*'


operator_list = ['MINUS', 'NOT', 'EXCLAMATION_MARK',
                 'DIVIDE', 'EQUAL', 'PERCENT', 'LSHIFT',
                 'RSHIFT', 'LESS', 'GTE', 'MORETHAN', 'LESSTHAN',
                 'EQUALITY', 'VBAR', 'BEOR', 'MEANTIME',
                 'OR', 'COMMA', 'QUESTION_MARK', 'SIZEOF']

# 이미 예약되어있는 문자열로서 다른 용도로 사용이 불가능한 문자열
keyword = {'auto': 'AUTO', 'break': 'BREAK', 'case': 'CASE',
           'char': 'CHAR', 'const': 'CONST', 'continue': 'CONTINUE',
           'default': "DEFAULT", 'do': 'DO', 'double': 'DOUBLE',
           'else': 'ELSE', 'enum': 'ENUM', 'extern': 'EXTERN',
           'float': 'FLOAT', 'for': 'FOR', 'goto': 'GOTO',
           'if': 'IF', 'inline': 'INLINE', 'int': 'INT',
           'long': 'LONG', 'register': 'REGISTER', 'restrict': 'RESTRICT',
           'return': 'RETURN', 'short': 'SHORT', 'signed': 'SIGNED',
           'static': 'STATIC', 'struct': 'STRUCT',
           'switch': 'SWITCH', 'typedef': 'TYPEDEF', 'union': 'UNION',
           'unsigned': 'UNSIGNED', 'void': 'VOID', 'volatile': 'VOLATILE',
           'while': 'WHILE',
           '_Alignas': '_ALIGNAS', '_Alignof': '_ALIGNOF', '_Atomic': '_ATOMIC',
           '_Bool': '_BOOL', "_Complex": '_COMPLEX', "_Generic": '_GENERIC',
           '_Imaginary': '_IMAGINARY', '_Noreturn': '_NORTURN', '_Static_assert': '_STATIC_ASSERT',
           '_Thread_local': '_THREAD_LOCAL'}

# print("keyword.values():", keyword.values())

operator = {'sizeof': 'SIZEOF'}

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


def t_COMMENT(t):
    r'\/\/.*'
    pass  # ignore_ prefix 사용


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
#include "timebomb.h"
#include <stdlib.h>

typedef struct Tree{
    int self;
    struct Tree *left;
    struct Tree *right;
} Tree;

int main(){
    box_ready();

    int N, result, this;
    N = box_size();

    int N2 = 0;
    int double_box[20] = {1};
    while (double_box[N2] < N){
        double_box[N2 + 1] = double_box[N2] * 2;
        N2++;
    }
    N2++;

    Tree ***First = (Tree ***)malloc(sizeof(Tree **) * N2);
    First[0] = (Tree **)malloc(sizeof(Tree *) * N);
    for (int i = 0; i < N; i++){
        First[0][i] = (Tree *)malloc(sizeof(Tree));
        First[0][i]->left = First[0][i]->right = NULL;
        First[0][i]->self = i+1;
    }

    int N3 = N;
    for (int i = 1; i < N2; i++){
        int Nend = (N3 + 1) / 2;
        First[i] = (Tree **)malloc(sizeof(Tree) * Nend);

        for (int j = 0; j < Nend; j++){
            First[i][j] = (Tree *)malloc(sizeof(Tree));
            
            First[i][j]->left = First[i - 1][j * 2];
            if (j*2+1 >= N3){
                First[i][j]->right = NULL;
                First[i][j]->self = First[i - 1][j * 2]->self;
            }else{
                First[i][j]->right = First[i - 1][j * 2 + 1];
                int left_idx = First[i - 1][j * 2]->self;
                int right_idx = First[i - 1][j * 2 + 1]->self;

                First[i][j]->self = (box_comp(left_idx, right_idx) == 1) ? left_idx : right_idx;
            }
        }

        N3 = (N3 + 1) / 2;
    }

    Tree *now = First[N2 - 1][0];
    Tree *next;
    int second_max;

    if (now->self == now->left->self){
        next = now->left;
        second_max = now->right->self;
    }
    else{
        next = now->right;
        second_max = now->left->self;
    }

    while(now->left != NULL || now->right != NULL){
        next = now->left;
        if (now->right != NULL){
            int check_val;
            if (now->self == now->left->self){
                next = now->left;
                check_val = now->right->self;
            }
            else{
                next = now->right;
                check_val = now->left->self;
            }
            second_max = (box_comp(second_max, check_val) == 1) ? second_max : check_val;
        }
        now = next;
    }

    box_report(second_max);
    return 0;
}

'''

data = data.lower()


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
d = 0
depth_list = []
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

    if tok.type == 'LBRAKET':
        n_OPERATOR += 1

    if tok.type == 'RBRAKET':
        n_OPERATOR += 1

    if tok.type == 'LPAREN':
        n_OPERATOR += 1

    if tok.type == 'RPAREN':
        n_OPERATOR += 1

    if tok.type == 'DOT':
        n_OPERATOR += 1

    if tok.type == 'POINTER':
        n_OPERATOR += 1

    if tok.type == 'INCREASE':
        n_OPERATOR += 1

    if tok.type == 'DECREASE':
        n_OPERATOR += 1

    if tok.type == 'AMPERSAND':
        n_OPERATOR += 1

    if tok.type == 'TIMES':
        n_OPERATOR += 1

    if tok.type == 'PLUS':
        n_OPERATOR += 1

    if tok.type in operator_list:
        n_OPERATOR += 1

    if tok.type == 'COLON':
        n_SEPARATOR += 1

    if tok.type == 'SEMICOL':
        n_SEPARATOR += 1

    if tok.type == 'DECLARE':
        n_SEPARATOR += 1

    if tok.type == 'LBRACE':
        n_SEPARATOR += 1
        n_LDEPTH += 1

    if tok.type == 'RBRACE':
        n_SEPARATOR += 1
        n_RDEPTH += 1
        if n_LDEPTH == n_RDEPTH:
            n_DEPTH_COUNTS += 1
            d = n_RDEPTH - d
            depth_list.append(d)

    if tok.type == 'DOUBLE_QUOTES':
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
print("depth_list :", depth_list)
print("max DEPTH :", max(depth_list))
print("average DEPTH :", average_DEPTH)
