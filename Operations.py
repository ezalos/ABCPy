import sys

print("Ope ", __name__)

def operations(a, b):
    print("Sum: ", a + b)
    print("Soustraction: ", a - b)
    print("Multiplication: ", a * b)
    if b != 0: #i b not 0:
        print("Division: ", a / b)
        print("Modulo: ", a % b)
    else:
        print("Division: ", "Error")
        print("Modulo: ", "Error")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        operations(int(sys.argv[1]), int(sys.argv[2]))

