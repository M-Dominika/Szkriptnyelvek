def main():
    n=int(input("Magasság: "))
    if n % 2 == 0:
        print("Hiba! A szám páros!")
    else:
        for i in range(1, n + 1, 2):
            print(("*" * i).center(n))
        for i in range(n - 2, 0, -2):
            print(("*" * i).center(n))

if __name__ == '__main__':
    main()
