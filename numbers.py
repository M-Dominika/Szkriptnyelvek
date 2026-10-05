def main():
    print(sum(range(101)))
    db = 0
    for i in range(101):
        for j in list(str(i)):
            db += int(j)
    print(db)

if __name__ == '__main__':
    main()
