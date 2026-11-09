
OPERATORS=['+','-','*','/','(',')']

def count_operators(expression):
    counts={op:0 for op in OPERATORS}
    for char in expression:
        if char in counts:
            counts[char]+=1
    return counts

if __name__=="__main__":
    expression=input("Enter an arithmetic expression: ")
    print("Operator counts:",count_operators(expression))
