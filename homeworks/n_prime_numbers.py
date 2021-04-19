'''
Instructions: Please write a program that print the first N prime numbers.
N should be declared as a variable at the beginning of your code.
You can hand it in as a link to your file at github or you can attach a file here in the assignment.
'''


def primes_finder(n):
    # number range to be checked
    number_range = set(range(2, n + 1))
    # empty list to apend discovered primes to
    primes_list = []

    # while loop
    while number_range:
        prime = number_range.pop()
        primes_list.append(prime)
        multiple = set(range(prime * 2, n + 1, prime))
        number_range.difference_update(multiple)

    # print list of primer
    print(primes_list)

    # number of primer that were found
    prime_count = len(primes_list)

    # largest prime

    largest_prime = max(primes_list)

    # summary

    print(f"There are {prime_count} prime number between 2 and {n}, the largest of which is {largest_prime}")

    return primes_list


### we check the function now:

primes_finder(1000)  # works!

primes_list = primes_finder(1000) # save the first 1000 prime numbers on a list
print(primes_list)