
try:
    x = 1
    y = 0
    x += 'a'
    z = x/y
    print('Done')
except ZeroDivisionError:
        print('ZeroDiv')
except SyntaxError:
    print('Syntax')
except Exception:
    print('Except')
except:
    print('catch')