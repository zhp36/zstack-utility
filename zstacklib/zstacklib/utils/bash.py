import subprocess
import functools
import threading
from zstacklib.utils import log

tl = threading.local()
tl.___BASH_DEBUG_INFO__ = []

logger = log.get_logger(__name__)

# @return: return code, stdout, stderr
def bash_full(cmd):
    p = subprocess.Popen('/bin/bash', stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = p.communicate(cmd)

    tl.___BASH_DEBUG_INFO__.append({
        'cmd': cmd,
        'return_code': p.returncode,
        'stdout': o,
        'stderr': e
    })
    return p.returncode, o, e

# @return: return code, stdout
def bash(cmd):
    ret, o, _ = bash_full(cmd)
    return ret, o

# @return: return code
def bash_ret(cmd):
    ret, _, _ = bash_full(cmd)
    return ret

# @return: stdout
def bash_errorout(cmd, code=0):
    ret, o, e = bash_full(cmd)
    if ret != code:
        raise Exception('failed to execute bash[%s], return code: %s, stdout: %s, stderr: %s' % (cmd, ret, o, e))
    return o

def in_bash(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        tl.___BASH_DEBUG_INFO__ = []

        try:
            return func(*args, **kwargs)
        finally:
            print tl.___BASH_DEBUG_INFO__

    return wrap

@in_bash
def test():
    bash('ls /tmp')
    bash('ls')
    bash('asdfasd')

threading.Thread(target=test).start()
threading.Thread(target=test).start()
