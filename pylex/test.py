###################################### lex 작성 시작 ###########################################

# 생각보다 편하군... 2022
# 먼저 다음 2개 ply 와 lex를 미리 INSTALL 해야 한다.
# 중간에 좀 error가 나지만 무시하고 처리해야 한다.


from more_itertools import locate
import os
import ply.lex as lex
import csv
# import numpy as np

# List of simple token names.   항상 필요하다.
tokens = (
    'ID',
    'NUMBER',
    'DCOL',
    'DOT',
    'POINTER',
    'LBRAKET',
    'RBRAKET',
    'LPAREN',
    'RPAREN',
    'INCREASE',
    'DECREASE',
    'SEA',
    'EXCLAMATION_MARK',
    'PLUS',
    'MINUS',
    'AMPERSAND',
    'TIMES',
    'DIVIDE',
    'PERCENT',
    'LSHIFT',
    'RSHIFT',
    'LESS',
    'GTE',
    'MORETHAN',
    'LESSTHAN',
    'MEMBER_A',
    'MEMBER_B',
    'EQUALITY',
    'NOTEQ',
    'VBAR',
    'BEOR',
    'MEANTIME',
    'OROR',
    'EQUAL',
    'COMMA',
    'CONDITION',
    'ALO_MILTI',
    'ALO_DIVI',
    'MODULO',
    'ALO_PL',
    'ALO_MI',
    'ALO_LSHIFT',
    'ALO_RSHIFT',
    'BIT_AND',
    'BIT_OR',
    'BIT_EXOR',
    'COLON',
    'SEMICOL',
    'LBRACE',
    'RBRACE',
    'DOUBLE_QUOTES',
    'QUOTES',
    'DECLARE',
    'QUESTION_MARK'
)

# Regular expression rules for simple tokens
# OPERATOR
t_DCOL = r'\:\:'
t_DOT = r'\.'
t_POINTER = r'\-\>'
t_LBRAKET = r'\['
t_RBRAKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_INCREASE = r'\+\+'
t_DECREASE = r'\-\-'
t_SEA = r'\~'
t_EXCLAMATION_MARK = r"\!"
t_PLUS = r'\+'
t_MINUS = r'\-'
t_AMPERSAND = r'\&'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_PERCENT = r"\%"
t_LSHIFT = r'\<\<'
t_RSHIFT = r'\>\>'
t_LESS = r'\<'
t_GTE = r'\>'
t_MORETHAN = r'\>\='
t_LESSTHAN = r'\<\='
t_MEMBER_A = r'\.\*'
t_MEMBER_B = r'\-\>\*'
t_EQUALITY = r'\=\='
t_NOTEQ = r'\!\='
t_VBAR = r"\|"
t_BEOR = r'\^'
t_MEANTIME = r'\&\&'
t_OROR = r'\|\|'
t_EQUAL = r'\='
t_COMMA = r'\,'
t_CONDITION = r'\?\:'
t_ALO_MILTI = r'\*\='
t_ALO_DIVI = r'\/\='
t_MODULO = r"\%\="
t_ALO_PL = r'\+\='
t_ALO_MI = r'\-\='
t_ALO_LSHIFT = r'\<\<\='
t_ALO_RSHIFT = r'\>\>\='
t_BIT_AND = r'\&\='
t_BIT_OR = r'\|\='
t_BIT_EXOR = r'\^\='
t_QUESTION_MARK = r'\?'

# SEPARATOR
t_COLON = r'\:'
t_SEMICOL = r'\;'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOUBLE_QUOTES = r"\""
t_QUOTES = r"\'"
t_DECLARE = r'\#'
# t_ignore_COMMENT = r'\#.*'

operator_list = ['DCOL', 'DOT', 'POINTER', 'LBRAKET', 'RBRAKET',
                 'LPAREN', 'RPAREN', 'INCREASE', 'DECREASE', 'SEA',
                 'EXCLAMATION_MARK', 'PLUS', 'MINUS', 'AMPERSAND',
                 'TIMES', 'DIVIDE', 'PERCENT', 'LSHIFT', 'RSHIFT',
                 'LESS', 'GTE', 'MORETHAN', 'LESSTHAN', 'MEMBER_A',
                 'MEMBER_B', 'EQUALITY', 'NOTEQ', 'VBAR',
                 'BEOR', 'MEANTIME', 'OROR', 'EQUAL', 'COMMA',
                 'CONDITION', 'ALO_MILTI', 'ALO_DIVI', 'MODULO',
                 'ALO_PL', 'ALO_MI', 'ALO_LSHIFT', 'ALO_RSHIFT',
                 'BIT_AND', 'BIT_OR', 'BIT_EXOR', 'QUESTION_MARK']

separator_list = ['COLON', 'SEMICOL', 'DOUBLE_QUOTES', 'QUOTES', 'DECLARE']

# 이미 예약되어있는 문자열로서 다른 용도로 사용이 불가능한 문자열
keyword = {'for': 'FOR', 'if': 'IF', 'then': 'THEN',
           'else': 'ELSE', 'while': 'WHILE', 'do': 'DO',
           'return': "RETURN", 'range': 'RANGE', 'class': 'CLASS',
           'break': 'BREAK', 'continue': 'CONTINUE',
           'try': 'TRY',
           'alignas': 'ALIGNAS', 'alignof': 'ALIGNOF',
           'asm': 'ASM', 'auto': 'AUTO',
           'bool': 'BOOL', 'case': 'CASE',
           'catch': 'CATCH', 'char': 'CHAR', 'char8_t': 'CHAR8_T',
           'char16_t': 'CHAR16_T', 'char32_t': 'CHAR32_T',
           'concept': 'CONCEPT', 'const': 'CONST',
           'consteval': 'CONSTEVAL', 'constexpr': 'CONSTEXPR', 'constinit': 'CONSTINIT',
           'co_await': 'CO_AWAIT', 'co_return': 'CO_RETURN', 'co_yield': "CO_YIELD",
           'decltype': 'DECLTYPE', 'default': 'DEFAULT',
           'double': 'DOUBLE', 'enum': 'ENUM',
           'explicit': 'EXPLICIT', 'export': 'EXPORT', 'extern': 'EXTERN',
           'false': 'FALSE', 'float': 'FLOAT', 'friend': 'FRIEND',
           'goto': 'GOTO', 'inline': 'INLINE', 'true': 'TRUE',
           'int': 'INT', 'long': 'LONG', 'mutable': 'MUTABLE',
           'namespace': 'NAMESPACE', 'noexcept': 'NOEXCEPT',
           'nullptr': 'NULLPTR', 'operator': 'OPERATOR',
           'private': 'PRIVATE', 'protected': 'PROTECTED',
           'public': 'PUBLIC', 'register': 'REGISTER',
           'requires': 'REQUIRES', 'return': 'RETURN', 'short': 'SHORT',
           'signed': 'SIGNED', 'static': 'STATIC',
           'static_assert': 'STATIC_ASSERT', 'struct': 'STRUCT',
           'switch': 'SWITCH', 'template': 'TEMPLATE', 'this': 'THIS',
           'thread_local': 'THREAD_LOCAL', 'throw': 'THROW', 'typedef': 'TYPEDEF',
           'typename': 'TYPENAME', 'union': 'UNION',
           'unsigned': 'UNSIGNED', 'using': 'USING', 'virtual': 'VIRTUAL',
           'void': 'VOID', 'volatile': 'VOLATILE', 'wchar_t': 'WCHAR_T'}
# print("keyword.values():", keyword.values())

operator = {'sizeof': 'SIZEOF', 'typeid': 'TYPEID', 'const_cast': 'CONST_CAST',
            'dynamic_cast': 'DYNAMIC_CAST', 'reinterpret_cast': 'REINTERPRET_CAST',
            'static_cast': 'STATIC_CAST', 'compl': 'COMPL', 'not': 'NOT', "new": 'NEW',
            "delete": 'DELETE', 'not_eq': 'NOT_EQ', 'bitand': 'BITAND',
            'xor': 'XOR', 'xor_eq': 'XOR_EQ', 'bitor': 'BITOR', 'and': 'AND', 'or': 'OR',
            'and_eq': 'AND_EQ', 'or_eq': 'OR_EQ'}

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

###################################### lex 작성 완료 ###########################################

###################################### 파일 읽어오기 작성 시작 ###########################################

# f = open('/mnt/c/Users/007_0/nespa 논문/codes/algo2022/submission/201824408/02/478.cpp', 'r')


columns = [['assignment', 'submission#', 'ratio', 'token_total', 'keyword',
           'id', 'number', 'operator', 'separator', 'max_dep', 'width', 'kind']]

d = open("data.csv", "w")
writer = csv.writer(d)

writer.writerows(columns)  # 여기 주목!

sub_dir = '/mnt/c/Users/007_0/nespa 논문/codes'
sub_list = os.listdir(sub_dir)  # algo2022, ds2021

for sub in sub_list:
    sub_dir = f'/mnt/c/Users/007_0/nespa 논문/codes/{sub}/submission'
    stu_id_list = os.listdir(sub_dir)  # 212188552, ...

    for stu_id in stu_id_list:
        id_dir = f'/mnt/c/Users/007_0/nespa 논문/codes/{sub}/submission/{stu_id}'
        assign_list = os.listdir(id_dir)  # 01 02 03
        # print(assign_list)

        for assign in assign_list:
            path_dir = f'{id_dir}/{assign}'
            # 456.cpp, 456.cres ...

            file_list = os.listdir(path_dir)

            # print(file_list)

            for i in range(len(file_list)):
                file_list[i] = file_list[i].split('.')
                # print(file_list[i])

            flat_list = []
            for l in file_list:
                for item in l:
                    flat_list.append(item)

            # print(flat_list)
            # print(flat_list.count('cpp'))

            if 'cpp' in flat_list:
                cpp_loc = list(locate(flat_list, lambda x: x == 'cpp'))
                cres_loc = list(locate(flat_list, lambda x: x == 'cres'))
                # print(cpp_loc)
                # print(flat_list[cpp_loc[-1]-1], flat_list[cpp_loc[-1]])

                try:
                    if flat_list[cpp_loc[-1]-1] == flat_list[cres_loc[-1]-1]:
                        c = open(
                            f'{path_dir}/{flat_list[cpp_loc[-1]-1]}.cres', 'r')
                        r = c.read()
                        correct = r.count('CORRECT ANSWER')
                        total = r.count(':')/2
                        c.close()
                        # print(r.count('CORRECT ANSWER'), r.count(':')/2)

                        f = open(
                            f'{path_dir}/{flat_list[cpp_loc[-1]-1]}.cpp', 'r')

                        try:
                            s = f.read()
                            data = s
                            f.close()

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
                            n_COUNTS = 0
                            d = 0
                            depth_list = []
                            kind = []
                            last_brace = [1]
                            t_depth_list = [0]
                            local_max = []
                            n_wd_counts = 0
                            width_list = [0]
                            while True:
                                tok = lexer.token()
                                # print(tok)

                                if not tok:
                                    break      # No more input

                                # print(tok.type)

                                kind.append(tok.value)

                                if tok.type in keyword.values():
                                    n_KEYWORD += 1

                                if tok.type == 'ID':
                                    n_ID += 1

                                if tok.type == 'NUMBER':
                                    n_NUMBER += 1

                                if tok.type in operator.values():
                                    n_OPERATOR += 1

                                if tok.type in operator_list:
                                    n_OPERATOR += 1

                                if tok.type in separator_list:
                                    n_SEPARATOR += 1

                                if tok.type == 'LBRACE':
                                    n_SEPARATOR += 1
                                    n_LDEPTH += 1

                                if tok.type == 'RBRACE':
                                    n_SEPARATOR += 1
                                    n_RDEPTH += 1
                                    if n_LDEPTH - n_RDEPTH == 1:
                                        n_COUNTS += 1
                                        lb = n_LDEPTH
                                        last_brace.append(lb)
                                        depth = last_brace[n_COUNTS] - \
                                            last_brace[n_COUNTS-1] + 1
                                        # print(depth)
                                        t_depth_list.append(depth)
                                        # print(t_depth_list)
                                        # d = n_RDEPTH - d
                                        # t_depth_list.append(d)

                                    if n_LDEPTH == n_RDEPTH:
                                        # t_depth_list.append('hi')
                                        # print(max(t_depth_list))
                                        if len(t_depth_list) != 0:
                                            local_max.append(max(t_depth_list))
                                            t_depth_list.clear()
                                        else:
                                            pass
                                        n_wd_counts += 1
                                        wd = n_LDEPTH - \
                                            width_list[n_wd_counts-1]
                                        width_list.append(wd)

                                        # print(width_list)

                                a += 1

                            # print('list len :', len(kind))
                            my_set = set(kind)
                            # print('set len :', len(my_set))

                            # tok.type, tok.value, tok.lineno, tok.lexpos
                            # print(tok.type)
                            # print(tok.value)

                            writer.writerows([[sub[:2]+assign, flat_list.count('cres'), correct/total, n_KEYWORD + n_ID +
                                               n_NUMBER + n_OPERATOR + n_SEPARATOR, n_KEYWORD, n_ID, n_NUMBER, n_OPERATOR,
                                               n_SEPARATOR, sum(local_max, 0.0)/len(local_max), sum(width_list, 0.0)/(len(width_list)-1), len(my_set)]])
                            # print('assignment :', assign)
                            # print('submission# :', flat_list.count('cres'))
                            # print('ratio :', correct/total)
                            # print('while total :', a)
                            # print("sum :", n_KEYWORD + n_ID +
                            #       n_NUMBER + n_OPERATOR + n_SEPARATOR)
                            # print("n_KEYWORD :", n_KEYWORD)
                            # print("n_ID :", n_ID)
                            # print("n_NUMBER :", n_NUMBER)
                            # print("n_OPERATOR :", n_OPERATOR)
                            # print("n_SEPARATOR :", n_SEPARATOR)
                            # print("depth_list :", depth_list)
                            # print("max DEPTH :", max(depth_list))
                            # print("DEPTH frequency :", n_COUNTS)
                        except UnicodeDecodeError as u:
                            print(u)

                except IndexError as e:
                    print(e, flat_list, cpp_loc, cres_loc)

                else:
                    pass

            else:
                pass
