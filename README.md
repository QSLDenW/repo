# Python Code: Function Checker with Decorators

This script demonstrates the use of a `checker` function as a decorator to handle exceptions and print results for the wrapped functions. The script includes two functions: `calculate` and `divisoin`, each decorated with `@checker`.

## Code
```python
def checker(*args, **kwargs):
    try:
        resoult = function(*args, **kwargs)
    except Exception as exc:
        print(f"We have problems {exc}")
    else:
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
