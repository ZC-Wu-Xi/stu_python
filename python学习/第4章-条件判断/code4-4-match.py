x = 4;
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3 | 4:
        print("x is 3 or 4")
    case _:
        print("x is something else")

x = 'hello'
match x:
    case 'hello':
        print("x is hello")
    case 'world':
        print("x is world")
    case _:
        print("x is something else")