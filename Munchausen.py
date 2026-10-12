def main():
    for i in range(440000000+1):
        osszeg = 0
        for j in str(i):
            if j=="0":
                osszeg=osszeg
            else:
                osszeg+=int(j)**int(j)
        if osszeg==i:
            print(osszeg)

if __name__ == "__main__":
    main()
