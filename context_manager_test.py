"""
# Context Manager-дің жұмысына мысал
with open('hello.txt', 'w') as f:
    f.write("Hello Python")

# Context Manager ішінде осылай жұмыс жасайды
f = open('hello.txt', 'w')
try:
    f.write('Hello Python2')
finally:
    f.close()

# Біздің объектілеріміз де with операторымен жұмыс жасау үшін
# __enter__ және __exit__  протоколдарын қолдану қажет
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.f = open('hello.txt', 'w')
        return self.f

    def __exit__(self, ex_type, ex_val, ex_):
        if self.f:
            self.f.close()


with ManagedFile('hello.txt') as f:
    f.write("Hello Python3!")
    f.write("Hello again!2")

# contextlib модулінде contextmanager декораторы бар. Осы декораторды
# қолдану арқылы функцияны with операторымен жұмыс жасай алатындай
# етуге болады
from contextlib import contextmanager
@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()
with managed_file('hello.txt') as f:
    f.write("Hello Python4!")
    f.write("Hello World!")
"""

class Indenter:
    def __init__(self):
        self.internal_text = ""

    def printm(self, text):
        print(self.internal_text + text)

    def __enter__(self):
        self.internal_text += "\t"
        return self

    def __exit__(self, ex_type, ex_val, ex_v):
        self.internal_text = ""

with Indenter() as indent:
    indent.printm("Hello!")
    with indent:
        indent.printm("Salem")
        with indent:
            indent.printm("Привет")
    with indent:
        indent.printm("Hey!")
