def main(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    else:
        return main(s[1:-1])

if __name__ == '__main__':
    s=input()
    if main(s):
        print("Palindrom")
    else:
        print("Nem palindrom")
