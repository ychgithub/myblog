from fabric.api import env, run, local
from fabric.operations import sudo


GIT_REPO = "https://github.com/ychgithub/myblog.git"

env.user = 'ubuntu'
env.password = 'qwerqwer123'
env.hosts = ['182.254.137.249']

env.port = '22'


def deploy():
    source_folder = '/home/ubuntu/uwsgi-myblog/myblog'

    run('cd %s ' % source_folder)
    run('git pull')
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data')
    sudo('service nginx reload')


def test():
    local("""
        cd /home/ubuntu/uwsgi-myblog &&
        source bin/activate &&
        cd myblog &&
        python manage.py runserver
        """)
    # run('../env/bin/git clone "https://github.com/ychgithub/myblog.git"')
