import random

def print_randint():
    print(random.randint(1, 100))

def print_randn():
    print(random.random())

def print_random_date():
    print(f"{random.randint(1, 2023):04d}-{random.randint(1, 12):02d}-{random.randint(1, 31):02d}")


if __name__ == '__main__':
    print_random_date()
