import pytest
from testinfra import get_host


# Connect to the remote server
@pytest.fixture(scope="module")
def host(request):
    host = get_host("ssh://user@your-remote-host")
    yield host


def test_nginx_installed(host):
    # Check if Nginx is installed
    nginx_package = host.package("nginx")
    assert nginx_package.is_installed


def test_nginx_running(host):
    # Check if Nginx is running with the system
    nginx_service = host.service("nginx")
    assert nginx_service.is_running
    assert nginx_service.is_enabled


def test_nginx_binding_port(host):
    # Check if Nginx is binding to port 80
    nginx_process = host.process.filter(comm="nginx")
    assert any(":80" in proc.cmdline() for proc in nginx_process)


def test_nginx_listen_port(host):
    # Configure Nginx to listen on a different port
    nginx_config_file = host.file("/etc/nginx/sites-available/default")
    nginx_config_file.replace("listen 80", "listen 8080")

    # Check if Nginx fails to listen on port 80 after the configuration change
    nginx_service = host.service("nginx")
    assert not nginx_service.is_running
    assert not nginx_service.is_enabled


# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])
# The test module defines multiple test functions prefixed with test_.
# The host fixture is used to connect to the remote server.
# The test_nginx_installed function checks if Nginx is installed on the remote server.
# The test_nginx_running function verifies if Nginx is running with the system.
# The test_nginx_binding_port function ensures that Nginx is binding to port 80.
# Finally, the test_nginx_listen_port function modifies the Nginx configuration file to listen on a different port (8080) and then checks if Nginx fails to listen on port 80.
# The tests can be executed by running the test module using python test_module.py.


# nb please install the module testinfra with the command 
# (pip install testinfra)