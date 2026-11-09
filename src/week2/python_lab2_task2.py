
NUMBERS=[3,8,-2,7,0,-5,10]

def squares(numbers):
    return [x**2 for x in numbers]


def positives(numbers):
    return [x for x in numbers if x>0]

def even_squares(numbers):
    return {x**2 for x in numbers if x%2==0}

def cubes(numbers):
    return {x:x**3 for x in numbers}

if __name__=="__main__":
    print("Squares:",squares(NUMBERS))
    print("Positives:", positives(NUMBERS))
    print("Even squares:", even_squares(NUMBERS))
    print("Cubes:",cubes(NUMBERS))
