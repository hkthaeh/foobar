def gcd(a, b):
    """
    Use the Euclidean algorithm to find the greatest common divisor
    
    :param a: the first integer
    :type a: int
    :param b: the second integer
    :type b: int
    :return the greatest common divisor between the two numbers
    :rtype: int
    """
    while b:                                         # Time: O(log(min(a,b))
        temp = a
        a = b
        b = temp % b
        
    return a

def factorial(n):
    """
    Calculate the factorial of a number
    
    :param n: the number we need to calculate the factorial of
    :type n: int
    :return: the factorial of said number
    :rtype: int
    """
    result = 1
    for i in range(1, n + 1):                                   # Time: O(n)
        result *= i
    return result

def conjugacy_size(partition):
    """
    Calculate the conjugacy size from a partition
    
    :param partition: the partition we need to calcualte the conjugacy size
    :type partition: tuple
    :return: the conjugacy size
    :rtype: int
    """
    n = sum(partition)                                          
    denominator = 1
    for length in set(partition):                   # Time: O(n), Space: O(n)
        count = partition.count(length)                          # Time: O(n)
        denominator *= factorial(count) * (length ** count)

    return factorial(n) // denominator

def integer_partitions(n, I=1):
    """
    Generate all the partitions of an integer
    
    :param n: the integer we need to grab all partitions of
    :type n: int
    :return: the integer partitions
    :rtype: tuples
    """
    yield (n,)
    for i in range(I, n // 2 + 1):                             # Time: O(n/2)
        for p in integer_partitions(n - i, i):                 # Time: O(2^n)
            yield (i,) + p

def exponent_sum(row_partition, column_partition):
    """
    Calculate the sum of gcd for all combinations of two
    given partitions
    
    :param row_partition: the partitions for the row
    :type row_partition: tuples
    :param column_partition: the partitions for the column
    :type column_partition: tuples
    :return: the sum of the two partitions
    :rtype: int
    """
    sum = 0
    for a in row_partition:                                     # Time: O(n)
        for b in column_partition:                              # Time: O(n)
            sum += gcd(a, b)
    return sum

def solution(w, h, s):
    """
    To escape Cammander Lambdas' elite starfighters that have flanked our ship,
    we need to determine the configuration of the celestial bodies in the 
    quadrant in order to jump into hyperspace and escape the clutches of
    Commander Lambdas once and for all!!!!!
    
    :param w: width of the star grid
    :type w: int
    :param h: height of the star grid
    :type h: int
    :param s: each celestial body's possible states
    :type s: int
    :return: the total number of distinct celestial body configurations
    :rtype: int
    """
    
    # Scott, the day has finally arrived. We've completed our month long 
    # mission and freed the bunnies!! It was a hard and difficult journey
    # but the story does not end here. We still have to make our final escape,
    # and only then can we finally relax! Now, let's calculate some 
    # celestial configurations. 

    
    # it would seems like this is a type of Group Theory problem, figuring out
    # all the ways things can be symmetric. 
    
    # Using Burnside's Lemma method, G = {e,a,b,c,p,q,r,s}
    
    # we'll first grab the number of celestrial permutations 
    # of this quadrant
    g = factorial(w) * factorial(h)
    # next we'll gather all integer partitions 
    row_permutations = list(integer_partitions(h))              # Space: O(n)
    column_permutations = list(integer_partitions(w))           # Space: O(n)
    # let's start counting the number of ways the celestial
    # bodies in this quadrant can be arranged
    configutations = 0
    
    # we'll go through all the row permutations
    for r in row_permutations:                                  # Time: O(n) 
        # along with the column permutations
        for c in column_permutations:                           # Time: O(n)
            # calculate the sum of gcd for the current row 
            # and column permutation
            exp = exponent_sum(r, c)
            # grab the product of the conjugacy size for
            # the current row and column
            C = conjugacy_size(r) * conjugacy_size(c)
            # now we add all of this to our final tally
            configutations += C * (s ** exp)
    
    # Finally! with the determination and resilience of
    # saving the bunnies and destroying Commander Lambda's
    # Doomsday device, we can jump into hyperspace and escape
    # this quasar quantum flux field and Commander Lambda!!
    home = str(configutations // g)
    
    # My friends, let's go home. 
    return home
    
    
    # Overall Time Complexity: O(2^n)
    # Overall Space Complexity: O(n)
    
    # Future Improvements:
        # 1) We can try to use Polya’s Enumeration Theorem
        # 2) for the integer_partitions function, we can switch to a more
        #    efficient iterative algorithm to reduce the time complexity
        