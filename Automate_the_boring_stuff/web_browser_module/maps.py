import webbrowser, sys, pyperclip

# webbrowser.open('https://www.facebook.com') # default broswer opens facebook
address = ''
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
elif len(pyperclip.paste()) > 1:
    address = pyperclip.paste()

if len(address) > 1:
    webbrowser.open(f'https://www.google.com/maps/place/{address}')


