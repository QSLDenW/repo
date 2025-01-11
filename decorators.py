
def checker(*args, **kwargs):
    try:
        resoult = function(*args, **kwargs)
    except Exception as exc:
        print(f"We have problems {exc}")
    else :
        print(f"Resoult - {resoult}")


@checker  
def calculate(expresssion):
    return eval(expresssion)


@checker
def divisoin(number, div):
    return number / div

# checker(calculate, "2+2")

# calculate = checker(calculate)

calculate("2+1")
divisoin(4, 2)