from dav_utils_DAVIDE_PONZINI import commands, messages, user

user.require_root()

try:
    commands.execute('apt update')
    messages.success('Downloaded package information')

    commands.execute('apt dist-upgrade -y')
    messages.success('Installed package upgrades')

    commands.execute('apt autoremove -y')
    messages.success('Removed unused packages')

    commands.execute('apt autoclean')
    messages.success('Cleaned up')
except commands.CalledProcessError as e:
    messages.error(e)
except KeyboardInterrupt:
    messages.warning('Interrupted')