def multiply_list_map(my_list=[], number=0):
    def multiply(x):
        return x * number
    result = map(multiply, my_list)
    return list(result)
