import math   
#this is the search for prime numbers
## make this codde better by introducing a flag that will stop the dividing loop 
##if the divisor count > 0 bc if divisor count > 0 then number is not prime :)


def  main():
    #user input bounds
    print('Enter a range. This program will search and print ')
    print('the primes within the given range.')
    print()
    LB = int(input('Enter lower bound: '))
    UB = int(input('Enter upper bound: '))
    print()

    #make emptry number list
    num_list = []

    #populate number list
    #with user's range
    for i in range (LB, UB):
        num_list.append(i)

    #make a copy of num_list
    prime_list = num_list[:]

    #sieve of primes
    for div in range (2, int(math.sqrt(UB))):
        for num in prime_list:
            if num%div == 0 and div != num:
                prime_list.remove(num)
    
    #this prints the resulting list of primes
    print(prime_list, '\n')
    
    ##find amount of primes
    index_p = 0
    for i in prime_list:
        index_p += 1
    print('There are ', index_p,' prime numbers in the given range.')
    print()

    #ENDing number alanlyzing
    print('Notice primes only end with 1, 3, 7, 9.')
    print('We will analyze how often these numbers occur at the end of primes.')
    print()

    ##accumulators for endings
    index_1 = 0
    index_3 = 0
    index_7 = 0
    index_9 = 0
    
    ##test primes for ending
    for num in prime_list:
        end = str(num)
        #primes that end with 1
        if end.endswith('1'):
            index_1 += 1

        #primes that end with 3
        if end.endswith('3'):
            index_3 += 1

        #primes that end with 7
        if end.endswith('7'):
            index_7 += 1
            
        #primes that rnd with 9
        if end.endswith('9'):
            index_9 += 1
    #prime percentages
    per_1 = format(float((index_1/index_p)*100), '.2f')
    per_3 = format(float((index_3/index_p)*100), '.2f')
    per_7 = format(float((index_7/index_p)*100), '.2f')
    per_9 = format(float((index_9/index_p)*100), '.2f')
    print('There are', index_1,'primes that end with 1 in your list.')
    print('That is', per_1, '% of primes end with 1')
    print()
    print('There are', index_3,'primes that end with 3 in your list.')
    print('That is', per_3, '% of primes end with 3')
    print()
    print('There are', index_7,'primes that end with 7 in your list.')
    print('That is', per_7, '% of primes end with 7')
    print()
    print('There are', index_9,'primes that end with 9 in your list.')
    print('That is', per_9, '% of primes end with 9')
    print()

main()


#time table
#100000 ~ 37-40s