
from fabric import task

@task
def get_hostname(c):
    print("Task is running")  # Debug print statement
    result = c.local('hostname', hide=True)
    print("The host name is:", result.stdout.strip())

@task
def install_package(c, pkg='dummy'):
    cmd = f'yum install {pkg} -y'
    result = c.local(cmd, hide=True)
    print(result.stdout)

@task
def remove_package(c, pkg=''):
    if pkg == '':
        cmd = 'yum remove dummy -y'
    else:
        cmd = f'yum remove {pkg} -y'
    result = c.local(cmd, hide=True)
    print(result.stdout)

