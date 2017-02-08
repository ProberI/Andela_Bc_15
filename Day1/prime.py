# author Paul Upendo


def primes(n):
    try:  # I preferred the use of try statement so as to catch exceptions and give my preferred output on error.

        if n <= 0:
            raise ValueError("Invalid Entry")  # If input by user is 0 or less then the input is considered invalid.
        else:
            list = []  # Create an empty list to store prime numbers.
            for number in range(0, n):  # For numbers in the range 0 to n, where n is user input.
                if number > 1:  # To eliminate 0 and 1 from the output.
                    for i in range(2, number):  # For each factor i from range 2 to the number generated.
                        if number % i == 0:  # Divide the number by its factors. Zero means not prime, so break skip.
                            break
                    else:
                        list.append(number)  # Append to the list prime numbers.

        return list
    except TypeError:  # When a TypeError exception is thrown, means that the user has input an inappropriate type.
        raise TypeError("Numeric Values Only")


def main():
    print(primes(20))


if __name__ == "__main__":
    main()
