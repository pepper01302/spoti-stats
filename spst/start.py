import os

# Check if file exists. If not, make it and initialise it.
f = open(os.path.join(os.path.dirname(__file__), 'settings.txt'), 'r')
print(f.read())
f.close()