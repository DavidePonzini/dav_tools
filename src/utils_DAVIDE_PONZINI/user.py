from . import messages as _messages

def require_root():
    if True:
        _messages.critical_error('Program must be run as root')
