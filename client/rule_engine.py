# -*- coding: utf-8 -*-

class And():
    def __repr__(self): return '&&'

class Or():
    def __repr__(self): return '||'

class Not():
    def __repr__(self): return '!'

class Left():
    def __repr__(self): return '('

class Right():
    def __repr__(self): return ')'

class Index():
    def __init__(self, index): self.index = index
    def __repr__(self): return str(self.index)


def analysis(exp):
    tokens = []
    token = ''
    wait = 0
    num = 0
    exp += ' '
    for ch in exp:
        if wait and ch != ')':
            token += ch
            continue

        if ch == ' ':
            if not token:
                pass
            elif token == '_':
                tokens.append(Index(num))
                num = 0
                token = ''
            else:
                print('error token in exp:', token, ch)
                return
        elif ch == '_':
            if not token:
                pass
            else:
                print('error token in exp:', token, ch)
                return
            token = '_'
        elif ch.isdigit():
            if token != '_':
                print('error token in exp:', token, ch)
                return
            num = num * 10 + int(ch)
        elif ch == '&':
            if not token:
                token = '&'
            elif token == '&':
                tokens.append(And())
                token = ''
            elif token == '_':
                tokens.append(Index(num))
                num = 0
                token = '&'
            else:
                print('error token in exp:', token, ch)
                return
        elif ch == '|':
            if not token:
                token = '|'
            elif token == '|':
                tokens.append(Or())
                token = ''
            elif token == '_':
                tokens.append(Index(num))
                num = 0
                token = '|'
            else:
                print('error token in exp:', token, ch)
                return
        elif ch == '!':
            if not token:
                tokens.append(Not())
                token = ''
            else:
                print('error token in exp:', token, ch)
                return
        elif ch == '(':
            if not token:
                pass
            elif token == '&&':
                tokens.append(And())
            elif token == '||':
                tokens.append(Or())
            elif token == '!':
                tokens.append(Not())
            else:
                print('error token in exp:', token, ch)
                return
            wait += 1
            token += ch
        elif ch == ')':
            if not wait:
                print('error token in exp:', token, ch)
                return
            wait -= 1
            if not wait:
                tokens.extend(analysis(token[1:]))
                token = ''
            else:
                token += ch
        else:
            print('error char in exp:', ch)
            return
    return tokens


class SingleNode():
    def __init__(self, c):
        self.cond = c

    def __bool__(self):
        return self.cond

    def count(self):
        return 1

class AndNode():
    def __init__(self, ln, rn):
        self.lnode = ln
        self.rnode = rn

    def __bool__(self):
        return self.lnode and self.rnode

    def count(self):
        return self.lnode.count() + self.rnode.count()

class OrNode():
    def __init__(self, ln, rn):
        self.lnode = ln
        self.rnode = rn

    def __bool__(self):
        return self.lnode or self.rnode

    def count(self):
        return self.lnode.count() + self.rnode.count()

class NotNode():
    def __init__(self, n):
        self.node = n

    def __bool__(self):
        return not self.node

    def count(self):
        return self.node.count()

def parse(tokens):
    pass


class Cond():
    def __bool__(self): return False

class RuleEngine():
    def __init__(self, rule):
        self.node = parse(analysis(rule))
        self.count = self.node.count()

    def run(self, conds):
        pass


if __name__ == '__main__':
    rlist = [
        '_1 && _2',
        '_1 || _2 && _3',
        '_1 && _2 || _3 && _4',
        '_1 && _2 ||_3&&(_4 || _5) || !_6 && ! _7',
    ]

    for r in rlist:
        print(analysis(r))
