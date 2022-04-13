#this python program is to create a function to generate any random number and print it.
import matplotlib.pyplot as plt


#parameterizing seed as initial value.
def seedLCG(initval):
    global seed
    seed = initval

#Using linear congruential generator to generate pseudo-random Numbers.
def LinearCongGenerator():
    global seed
    
    #defining module
    mod = (2**31)-1
    
    #defining multiplier
    mult = 2
    
    #defining increment value
    inc = 5
    
    #applying LCG algorithm
    '''
    x[i] = m.x[i-1] + p
    u = x[i] % p
    
    x[i] = seed
    m = multiplier
    p = module
    u = random output
    '''
    seed = ((mult * seed) + inc) % mod
    
    return seed

#calling global seed function
seedLCG(1)

#printing output in a certain range.
for i in range(5):
    print(LinearCongGenerator())
    plt.hist(seed, bins = 1, alpha = 1)
    
    continue
plt.show()

