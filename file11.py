from sys import argv


def greet(name, salutations):
    sentence = f"Hi, Good Morning\n {name}\n\n {salutations}"
    return sentence


if __name__ == "__main__":
    result = greet(argv[1], argv[2])
    print(result)
