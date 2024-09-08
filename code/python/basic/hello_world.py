import sys
import importlib.metadata

if __name__=='__main__':
    print("Hello World!")

    # Print some info about this version of Python
    print("\n\nPython version:\n", sys.version,"\n\n")
    
    # list installed packages
    print( sorted(x.name for x in importlib.metadata.distributions()) )
