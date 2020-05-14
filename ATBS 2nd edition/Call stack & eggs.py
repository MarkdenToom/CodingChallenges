# Functioning
# this is just for testing purposes to learn definition orders and the difference between global and local scopes.

eggs = "global scope eggs"
print(eggs)


def a():
    print('a() starts')
    eggs = "local scope eggs"
    b()
    print(eggs)
    d()
    print('a() returns')


def b():
    print('b() starts')
    eggs = "these eggs aren't def a()"
    print(eggs)
    c()
    print('b() returns')


def c():
    print('c() starts')
    global eggs
    eggs = "new global scope eggs"
    print('c() returns')


def d():
    print('d() starts')
    print('d() returns')


a()
print(eggs)
