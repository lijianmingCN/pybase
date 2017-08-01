#Decotator
def identity(f):
    print 'preaction'
    return f

@identity
def main():
    print 'main function'


main()