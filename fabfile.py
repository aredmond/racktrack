from fabric.api import local
from fabric.api import lcd

def prepare_deployment(branch_name):
    local('python manage.py test rackinfo')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)

def deploy():
    with lcd('/home/django/code/django/rack_track_1.0.0/racktrack/'):
        local('git pull /home/django/code/django/rack_track_1.0.0/racktrack_dev/')
        local('python manage.py migrate rackinfo')
        local('python manage.py test rackinfo')
        local('echo "start server"')
