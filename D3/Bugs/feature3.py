import os
import six
import sys

def _get_home():
    """Find user's home directory if possible.
    Otherwise, returns None.

    :see:
        http://mail.python.org/pipermail/python-list/2005-February/325395.html
    """
    try:
        path = os.environ.get('MATPDIR')
        if path is None:
            if six.PY2 and sys.platform == 'win32':
                path = os.path.expanduser(b"~").decode(sys.getfilesystemencoding())
            else:
                path = os.path.expanduser("~")
    except ImportError:
        # This happens on Google App Engine (pwd module is not present).
        pass
    else:
        if os.path.isdir(path):
            return path
    for evar in ('MATPDIR', 'HOME', 'USERPROFILE', 'TMP'):
        path = os.environ.get(evar)
        if path is not None and os.path.isdir(path):
            return path
    return None


