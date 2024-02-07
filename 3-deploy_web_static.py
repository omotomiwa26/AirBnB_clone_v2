#!/usr/bin/python3
"""
This python Fabric script(based on the file
2-do_deploy_web_static.py) that creates
and distributes an archive to your
web servers, using the function deploy
"""

from fabric.api import env, local, put, run
from datetime import datetime as d
from os.path import exists, isdir
env.hosts = ['52.3.243.47', '100.25.165.37']


def do_pack():
    """
    This function generates
    a tgz archive
    """
    try:
        date = d.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = F"versions/web_static_{date}.tgz"
        local(F"tar -cvzf {file_name} web_static")
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """
    This function distributes an archive
    to the web servers
    """
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run(F'mkdir -p {path}{no_ext}/')
        run(F'tar -xzf /tmp/{file_n} -C {path}{no_ext}/')
        run(F'rm /tmp/{file_n}')
        run(F'mv {path}{no_ext}/web_static/* {path}{no_ext}/')
        run(F'rm -rf {path}{no_ext}/web_static')
        run('rm -rf /data/web_static/current')
        run(F'ln -s {path}{no_ext}/ /data/web_static/current')
        return True
    except Exception:
        return False


def deploy():
    """
    This function creates and distributes
    an archive to the web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
