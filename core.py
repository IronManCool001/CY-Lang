def println(msg):
    print(msg)

def find_variable(content):
    #string = list("str")
    if "str" in content:
        println("Found String!")
    if "int" in content:
        println("Found Integer!")
    if "float" in content:
        println("Founf Decimal Value!")
