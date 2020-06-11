# defining the string_alternative function
def string_alternative(ip):
    return ip[::2]


# defining the main function
def main():
    word = input("Enter the word:")
    result = string_alternative(word)
    print("Result:", result)


if __name__ == "__main__":
    main()
