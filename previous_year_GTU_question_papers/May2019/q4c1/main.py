from string import ascii_letters


def encrypt(input_string: str, key: int, alphabet=None) -> str:
    alpha = alphabet or ascii_letters
    result = ""

    for character in input_string:
        if character not in alpha:
            result += character
        else:
            new_key = (alpha.index(character)+key) % len(alpha)
            result += alpha[new_key]
    return result


def decrypt(input_string: str, key: int, alphabet=None) -> str:
    key += -1
    return encrypt(input_string, key, alphabet)


def main():
    while True:
        print(f'\n{"-" * 10}\n Menu\n{"-" * 10}')
        print(*["1.Encrpyt", "2.Decrypt", "3.Quit"], sep="\n")

        # get user input
        choice = input("\nWhat would you like to do?: ").strip() or "3"

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice, please enter a valid choice")
        elif choice == "1":
            input_string = input("Please enter the string to be encrypted: ")
            key = int(input("Please enter off-set: ").strip())

            print(encrypt(input_string, key))
        elif choice == "2":
            input_string = input("Please enter the string to be decrypted: ")
            key = int(input("Please enter off-set: ").strip())

            print(decrypt(input_string, key))

        elif choice == "3":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
