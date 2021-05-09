# Must

    - start with underscore (_) or letter (a-z, A-Z)
    - followed by any number of underscore(_), letter (a-z,A-Z) , or digit(0-9)
        - eg: var, my_var, index1, index_1, _var, __var, __it__
        - but __ have some special meaning

    - cannot be reserved words:
        - None,True,False, and , or, not, if , else, elif, for, while, break, continue, pass, def, lambda, nonlocal, return, yield, del, in, is , assert, class, try, except, finally, raise, import, from, with, as etc..

# Conventions

    - _my_var -> single underscore
        - Means this is to indicate 'internal use' or 'private' object.
        - when we import like (from module import *). the single underscore will not import.

    - __my_var -> double underscore (dunder)
        - Used to 'mangle' class attribute-useful in inheritance chains.

    - __my_var__ -> double underscore at both end
        - Used for system-defined names that have a special meaning to the interpreter.
        - Dont invent them, stick to the ones pre-defined by Python.
        - eg: x<y ---> x.__lt__(y)

# Other Naming Conventions. (PEP 8)

    * packages -> short, all-lowercase names. Preferably no underscore.
        - eg: utilities
    * module -> short, all-lower names, Can have underscores.
        - eg: db_utils, dbutils
    * Classes -> CapWords convension
        - eg: BankAccount
    * function -> lowercase, words separated by underscore(snake_case)
        - eg: open_account
    * variables -> lowercase, words separated by underscore(snake_case)
        - eg: account_id
    * Constants -> all-uppercase , words separated by underscores
        - MIN_APR

# Example

    1. abc = 123 #valid
    2. \_abc = 123 #valid
    3. ab_c = 123 #valid
    4. abc\_ = 123 #valid
    5. 1abc = 123 #in_valid
    6. $abc = 123 #in_valid
    7. ab$c = 123 #in_valid
    8. \_ = 123 #valid
    9. \_\_ = 123 #valid
    10. a1bc = 123 #valid
    11. avc1 = 123 #valid
