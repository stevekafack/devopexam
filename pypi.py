#section 1.5
# install first devpi using the command  "pip install devpi-server."
# Initialize a new devpi server by running devpi-server --init.
# run the cmd as an admin and grant all the aceses before doing this task 

from setuptools import setup

setup(
    name='your-package',
    version='1.0.0',
    packages=['your_package'],
    install_requires=[
        'dependency1',
        'dependency2',
    ],
)
# Build the package by running python setup.py sdist. This will create a .tar.gz file in the dist directory.
# Activate the virtual environment for your package (if applicable).
# Use the devpi command to upload the package to your local instance:



# devpi use http://localhost:port
# devpi login username --password password
# devpi upload

#Replace localhost with the appropriate hostname or IP address, port with the port number of your devpi server (default is 3141), username with your username, and password with your password.
# run the devpi with the following command 

# pip config set global.index-url http://localhost:port/user/username/simple/

# Run pip install your-package to install the package from your local devpi instance.

