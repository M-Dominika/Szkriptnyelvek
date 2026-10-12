def main():
    """Visszaadjuk az 1000-nél kisebb számok összegét, melyek 3-nak vagy 5-nek többszörösei"""
    l=[i for i in range(1000) if i%3==0 or i%5==0]
    print(sum(l))

if __name__ == "__main__":
    main()
