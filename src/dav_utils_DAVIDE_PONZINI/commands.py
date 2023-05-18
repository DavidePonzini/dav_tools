import platform as _platform
import subprocess as _subprocess
from subprocess import CalledProcessError


class UnknownOSException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__('Could not identify OS', *args)

# runs a command, depeding on the current OS
#   returns True if the program exits with return code zero, False otherwise
def execute(command: str) -> bool:
    exit_status = _subprocess.check_call(command.split())
    return exit_status == 0

# runs a command, depeding on the current OS
#   the output is returned in the specified type (default: bytes)
#   if a command returns a non-zero exit code the program raises an exception (default behavior) or returns a given value (by default: None)
def get_output(command_linux: str, command_windows: str, return_type = bytes, on_error = None):
    if _platform.system() == 'Linux':
        command = command_linux
    elif _platform.system() == 'Windows':
        command = command_windows
    else:
        if on_error is None:
            raise UnknownOSException()
        else:
            return return_type(on_error())
        
    try:
        return return_type(_subprocess.check_output(command.split()))
    except CalledProcessError as e:
        if on_error is None:
            raise e
        return return_type(on_error())
    