from dav_tools import commands
import platform

def test_is_installed_existing():
    if platform == 'Windows':
        assert commands.is_installed('cmd')
    elif platform == 'Linux':
        assert commands.is_installed('ls')

def test_is_installed_non_existing():
    assert not commands.is_installed('non_existing_command')

    