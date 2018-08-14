x = 10
def globallyChange():
      global x
      x = "didn't work"
globallyChange() #You've to call the function for changes.
print x
