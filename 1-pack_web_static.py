#!/usr/bin/python3
"""
This python Fabric script generates a .tgz archive
from the contents of the web_static folder
AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime as d
from fabric.api import *


def do_pack():
    """
    This function generates an archive on
    web_static folder
    """

    time = d.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local(F'tar -cvzf versions/{archive} web_static')
    if create is not None:
        return archive
    else:
        return None
