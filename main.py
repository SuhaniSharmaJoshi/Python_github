from Operations.calculator import add, sub, mul, div
def main():
    print("1: Addition")
    print("2: Substraction")
    print("3: Multiplication")
    print("4: Divide")

    choice = int(input("enter your choice 1/2/3/4 :   "))
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))

    if choice== 1:
        print("results", add(a,b))
    elif choice==2:
        print("results", sub(a,b))
    elif choice==3:
        print("results", mul(a,b))
    elif choice==4:
        print("results", div(a,b))
    else:
        print("enter correct values")

if __name__ == "__main__":
    main()

