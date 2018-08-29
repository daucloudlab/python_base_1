# with open('hello.txt', 'w') as f:
#     f.write("Hello Python")
#
# f = open('hello.txt', 'w')
# try:
#     f.write('Hello Python2')
# finally:
#     f.close()
# class ManagedFile:
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         self.f = open('hello.txt', 'w')
#         return self.f
#
#     def __exit__(self, ex_type, ex_val, ex_):
#         if self.f:
#             self.f.close()
#
#
# with ManagedFile('hello.txt') as f:
#     f.write("Hello Python3!")
#     f.write("Hello again!2")
# from contextlib import contextmanager
# @contextmanager
# def managed_file(name):
#     try:
#         f = open(name, 'w')
#         yield f
#     finally:
#         f.close()
# with managed_file('hello.txt') as f:
#     f.write("Hello Python4!")
#     f.write("Hello World!")
