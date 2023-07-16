import argparse

def argparser():
    parser = argparse.ArgumentParser(description='give two integers.')
    parser.add_argument('inta', type=int, help='first integer')
    parser.add_argument('intb', type=int, help='second integer')
    args = parser.parse_args()
    return args
