def main():
    f1=['auto', 'villamos', 'metro']
    f1=[n.upper()+"!" for n in f1]
    print(f1)

    f2 = ['aladar', 'bela', 'cecil']
    f2 = [n.capitalize() for n in f2]
    print(f2)

    f3 = [0 for i in range(10)]
    print(f3)

    f4 = [i for i in range(1,11)]
    f4 = [i*2 for i in f4]
    print(f4)

    f5 = [str(i) for i in range(1, 11)]
    f5 = [int(i) for i in f5]
    print(f5)

    f6="1234567"
    f6=[int(i) for i in f6]
    print(f6)

    f7='The quick brown fox jumps over the lazy dog'
    f7=[len(i) for i in f7.split()]
    print(f7)

    f8 = "python is an awesome language"
    f8= [i[0] for i in f8.split()]
    print(f8)

    f9 = 'The quick brown fox jumps over the lazy dog'
    f9 = [(i, len(i)) for i in f9.split()]
    print(f9)

    f10 = [i for i in range(10) if i%2==0]
    print(f10)

    f11 = [i**2 for i in range(20) if i**2 % 2 == 0]
    print(f11)

    f12 = [i ** 2 for i in range(20) if str(i**2)[-1]=="4"]
    print(f12)

    f13 = [chr(i).upper() for i in range(ord('a'), ord('z'))]
    print(''.join(f13))

    f14 = [' apple ', ' banana ', ' kiwi']
    f14 = [n.strip() for n in f14]
    print(f14)

    f15 = [1, 0, 1, 1, 0, 1, 0, 0]
    f15 = ''.join([str(i) for i in f15])
    print(f15)

if __name__ == "__main__":
    main()
