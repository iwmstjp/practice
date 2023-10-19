import time

def decorator(function):
    def decoFunction():
        time.sleep(2)
        function()
    return decoFunction

@decorator
def hello():
    print("hello")

hello()