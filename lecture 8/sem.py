from nltk.sem import Valuation, Model,Assignment
from nltk.sem import Expression
from nltk.sem import evaluate
from nltk.inference import tableau

dom = set(['u1', 'u2', 'u3', 'u4'])
g3 = Assignment(dom, [('x', 'u1'), ('y', 'u2')])
print g3 == {'x': 'u1', 'y': 'u2'}

read_expr = Expression.fromstring
p1 = read_expr('man(socrates)')
p2 = read_expr('all x.(man(x) -> mortal(x))')
c  = read_expr('mortal(socrates)')
print tableau.TableauProver().prove(c, [p1,p2])