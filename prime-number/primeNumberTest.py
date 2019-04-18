from isPrime import isPrime
from pprint import pprint


def read_file_text():
    data = []
    with open("primeNumber.txt", "r") as f:
        line = f.readline()
        while line:
            line = line.strip()
            data.append(isPrime(int(line)))
            line = f.readline()
    f.close()
    return data


if __name__ == '__main__':
    data = read_file_text()
    pprint(data)
    try:
        print(data.index(False))
    except Exception as e:
        print(e)
    print("------")
    print(all(data))
