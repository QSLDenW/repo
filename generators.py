def raise_to_the_degrees(number, max_degree):
    i=0
    for _ in range(max_degree):
        yield number ** i
        i+=1


res = raise_to_the_degrees(123, 50)
print(res)


for _ in res:
    print(f"res , {_} \n\n\n")
