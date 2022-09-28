import os

def main():
    path = './myfile.txt'
    is_file = os.path.isfile(path)
    if is_file:
        f = open('myfile.txt', 'r', encoding="utf-8")
        s = f.read()
        f.close()
    else:
        s="0"

    print(f"open:{s}")
    if s == "":
        s = 1
    else:
        s = int(s)+1
    f = open('myfile.txt', 'w', encoding="utf-8")
    f.write(str(s))
    f.close()

if __name__ == '__main__':
    main()
