import pprint

# hello function
def hello() -> bool:
    print('Hello!')
    return True

# main function
def main():
    if not hello():
        print('ERROR!')
    return True
        
#
# Main programm
#

if __name__ == '__main__':
    main()
