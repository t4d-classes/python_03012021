

# def do_it(msg = "awesome"):
#     print("do it " + msg)


# do_it("cooler")


# def my_sum(a, b=2, c=3):
#     print(a,b,c)

# my_sum(0,c=4)

# def my_sum(a,b,*args, **kwargs):
#     # print(a,b,args, kwargs)

#     for arg in args:
#         print(arg)

#     for key in kwargs.values():
#         print(key)


# my_sum(1,2,3,4,5,6, num1=1, num2=2, num3=3)

def outer():

    print("outer")

    def inner():
        print("inner")

    return inner

fn1 = outer()
fn1()