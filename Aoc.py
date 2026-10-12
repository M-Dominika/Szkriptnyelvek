def main(a):
    b=[int(n) for i,n in enumerate(a) if a[i]==a[(i+1)%len(a)]]
    print(sum(b))


if __name__ == "__main__":
    a=input()
    main(a)
