#section 1.2
import click

@click.command()
@click.argument('name')
def print_name(name):
    if not name.startswith('p'):
        click.echo(f"The name '{name}' does not begin with 'p'.")


# The @click.command() decorator defines a command-line command using the click library.
# The @click.argument('name') decorator specifies that the name argument is expected to be provided as an argument on the command line.
# The def print_name(name) function is the command's implementation. It takes the name argument as input.
# The if not name.startswith('p') condition checks if the name does not begin with the letter "p".
# If the condition is true, the click.echo() function is used to print a message indicating that the name does not begin with "p".



# To run this command-line tool, you need to call the print_name() function using the click command-line interface

if __name__ == '__main__':
    print_name()

# Save the code in a Python file (e.g., name_tool.py), and then you can execute the script from the command line, providing a name as an argument:
# the command to print on command line is" $ python name_tool.py John"
# output to this response is  "The name 'John' does not begin with 'p'."

