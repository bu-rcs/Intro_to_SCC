import sys
import pkg_resources

if __name__=='__main__':
    print("Hello World!")

    # Print some info about this version of Python
    print("\n\nPython version:\n", sys.version,"\n\n")
    
    # list installed packages
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages]) 
    print(installed_packages_list)
