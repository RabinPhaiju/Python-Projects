1.  Random

    - tetris random :- create tetris in python pygame
    - import random

      - random.seed() :- To generate a new random sequence, a seed must be set depending on the current system time.
      - random.getstate()
      - random.setstate()

        - import random

                random.seed(1)

                # Get the state of the generator
                state = random.getstate()

                print('Generating a random sequence of 3 integers...')
                for i in range(3):
                    print(random.randint(1, 1000))

                # Restore the state to a point before the sequence was generated
                random.setstate(state)
                print('Generating the same identical sequence of 3 integers...')
                for i in range(3):
                    print(random.randint(1, 1000))

      - random.getrandbits(100) # Get a random integer having 100 bits
      - random.randrange(1,4)
      - random.randint(100, 200) # including starting and ending numbers
      - random.random() # 0 to 1
      - random.uniform(1, 5) # 1 to 5
      - random.randint(0, i) for i in range(10) # shuffle list
      - random.choice([1,,4,7,5,8]) # randomly pick 1 value
      - random.sample([1,,4,7,5,8], 2) # pick 2 sample
