#section 1.1
import sys

if __name__ == '__main__':
    if len(sys.argv) > 0:
        print("This script is being run from the command line.")
    else:
        print("This script is not being run from the command line.")
# Explanation:
# The sys.argv variable holds the command-line arguments passed to the script.
# sys.argv[0] is the name of the script itself.
# The condition __name__ == '__main__' ensures that the code inside the if block is executed only if the script is run directly and not imported as a module.
# If sys.argv has a length greater than zero, it means that at least one argument (the script name) was passed, indicating that the script is being run from the command line.





