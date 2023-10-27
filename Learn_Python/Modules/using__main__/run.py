# import module1
import timing

print(f'loading run.py: __name__={__name__}')

code = '[x**2 for x in range(1000)]'
result = timing.timeit(code,100)
print(result)