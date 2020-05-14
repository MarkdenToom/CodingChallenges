# learn traceback for errors

def spam():
    bacon()


def bacon():
    raise Exception('This is the error message.')


spam()  # This would call an error on the raise Exception, but also Traceback bacon() and spam() respectively
