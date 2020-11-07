print('This is the string {}'.format('Inserted'))

print(f"This is the string {'Inserted'}")

print('The {0} {0} {0} '.format('fox', 'brown', 'quick'))

print('The {} {} {} '.format('fox', 'brown', 'quick'))

print('The {q} {b} {f} '.format(f = 'fox', b = 'brown', q= 'quick'))

# float formating -----------------------
result  = 100/777
print('the result was {r:0.3f}'.format(r = result))