import platform as _platform
import subprocess as _subprocess
from subprocess import CalledProcessError

class UnknownOSException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__('Could not identify OS', *args)

# runs a command, depeding on the current OS
#   the output is returned in the specified type (default: bytes)
#   if a command returns a non-zero exit code the program raises an exception (default behavior) or returns a given value (by default: None)
def execute(command_linux: str, command_windows: str, return_type=bytes,
            fail_on_os_error:bool=True,
            fail_on_command_error:bool=True, default_value=None):
    if _platform.system() == 'Linux':
        command = command_linux
    elif _platform.system() == 'Windows':
        command = command_windows
    else:
        if fail_on_os_error:
            raise UnknownOSException()
        else:
            if default_value is None:
                return None
            return return_type(default_value)

    try:
        return return_type(_subprocess.check_output(command.split()))
    except CalledProcessError as e:
        if fail_on_command_error:
            raise e
        if default_value is None:
            return None
        return return_type(default_value)
    