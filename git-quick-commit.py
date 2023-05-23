from datetime import date
import sys

from dav_utils_DAVIDE_PONZINI import argument_parser, commands, messages

argument_parser.set_description('Quickly commits and uploads all changes performed on the current directory')
argument_parser.add_argument('-m', '--message', help='commit message', default=None)


if commands.get_output('git status --porcelain', return_type=str) == '':
    messages.success('Nothing to commit')
    sys.exit(0)

if argument_parser.args.message is not None:
    commit_message = argument_parser.args.message
else:
    commit_message = messages.ask('Reason')
    if len(commit_message) == 0:
        commit_message = f'Quick commit ({date.today()})'
        messages.warning(f'Using default commit message: "{commit_message}"')

commands.execute('git add .')
messages.success('Stages changes')

commands.execute(f'git commit --quiet -m "{commit_message}"')
messages.success('Committed changes')

messages.progress('Uploading commit...')
commands.execute(f'git push origin master --quiet')
messages.success('Uploaded commit')
