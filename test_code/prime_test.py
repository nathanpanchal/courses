def is_prime(n):
    if n == 0 or n == 1:
        print "Not Prime"
        return
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print "Not Prime"
            return
        else:
            print "Prime"
            return

n = int(raw_input("Please enter a number: "))
is_prime(n)