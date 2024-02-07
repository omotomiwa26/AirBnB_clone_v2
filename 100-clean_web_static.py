#!/usr/bin/python3
"""
This Python Fabric Script(based on the file
3-deploy_web_static.py) deletes
out-of-date archives, using the function do_clean:
"""

import os
from fabric.api import *

env.hosts = ['52.3.243.47', '100.25.165.37']


def do_clean(number=0):
    """
    This function Deletes out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for z in range(number)]
    with lcd("versions"):
        [local(F"rm ./{x}") for x in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [x for x in archives if "web_static_" in x]
        [archives.pop() for z in range(number)]
        [run(F"rm -rf ./{x}") for x in archives]
