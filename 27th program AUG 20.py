# x=20                         #global
# print("outside", x)
#
# def f():
#     print("inside", x)
# f()
#
# #local
#
# def f():
#     x=20
#     print("inside", x)
# f()
#
# print("outside", x)

#non-local / enclosed
def outer()       #nonlocal
    x=20

    def inner(): #local
        print("inside inner function",x)

    inner()
    print("inside outer function",x)

outer()