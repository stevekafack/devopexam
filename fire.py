
#section 1.3
import fire

class MyScript:
    def method1(self, arg1):
        print(f"Method 1 called with argument: {arg1}")

    def method2(self, arg1, arg2):
        print(f"Method 2 called with arguments: {arg1}, {arg2}")

if __name__ == '__main__':
    fire.Fire(MyScript)
# In the example above, we import the fire library and create a class MyScript with two methods: method1 and method2.
# The methods are decorated with @fire.Fire to expose them as command-line commands.
# The script is then called with fire.Fire(MyScript) to enable command-line access to the methods in MyScript.
# You can run the script from the command line and provide the method name and any required arguments to execute the desired method:

# in the command line enter the following lines 

#  python my_script.py method1 argument1

# orpython my_script.py method2 argument1 argument2