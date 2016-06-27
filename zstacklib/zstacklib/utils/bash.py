import subprocess
import functools
import json
from jinja2 import Template
from zstacklib.utils import log
import inspect

logger = log.get_logger(__name__)

# @return: return code, stdout, stderr
def bash_roe(cmd):
    frames = []
    frame = inspect.currentframe()
    while frame:
        frames.insert(0, frame)
        frame = frame.f_back

    ctx = {}
    for f in frames:
        ctx.update(f.f_locals)

    tmpt = Template(cmd)
    cmd = tmpt.render(ctx)

    p = subprocess.Popen('/bin/bash', stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = p.communicate(cmd)

    __BASH_DEBUG_INFO__ = ctx.get('__BASH_DEBUG_INFO__')
    if __BASH_DEBUG_INFO__ is not None:
        __BASH_DEBUG_INFO__.append({
            'cmd': cmd,
            'return_code': p.returncode,
            'stdout': o,
            'stderr': e
        })

    return p.returncode, o, e

# @return: return code, stdout
def bash_ro(cmd):
    ret, o, _ = bash_roe(cmd)
    return ret, o

# @return: stdout
def bash_o(cmd):
    _, o, _ = bash_roe(cmd)
    return o

# @return: return code
def bash_r(cmd):
    ret, _, _ = bash_roe(cmd)
    return ret

# @return: stdout
def bash_errorout(cmd, code=0):
    ret, o, e = bash_roe(cmd)
    if ret != code:
        raise Exception('failed to execute bash[%s], return code: %s, stdout: %s, stderr: %s' % (cmd, ret, o, e))
    return o

def in_bash(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        __BASH_DEBUG_INFO__ = []

        try:
            return func(*args, **kwargs)
        finally:
            logger.debug('BASH COMMAND DETAILS IN %s: %s' % (func.__name__, json.dumps(__BASH_DEBUG_INFO__)))
            del __BASH_DEBUG_INFO__

    return wrap
