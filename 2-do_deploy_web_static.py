#!/usr/bin/python3
"""
This Python Fabric script(based on the file
1-pack_web_static.py) that distributes
an archive to your web servers,
using the function do_deploy
"""

from fabric.api import put, run, env
from os.path import exists as e
env.hosts = ['52.3.243.47', '100.25.165.37']


def do_deploy(archive_path):
    """
    This function distributes an archive
    to the web servers
    """
    if e(archive_path) is False:
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
        run(F'rm -rf {path}{no-ext}/web_static')
        run('rm -rf /data/web_static/current')
        run(F'ln -s {path}{no_ext}/ /data/web_static/')
        return True
    except Exception:
        return False
