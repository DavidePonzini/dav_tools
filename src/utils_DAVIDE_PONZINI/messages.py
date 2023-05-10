import sys

from text_color import TextFormatOption, print_colored_text, input_colored


def _message(text, icon=None, text_options=[], icon_options=[], blink=False, end='\n'):
    if icon is not None:
        print_colored_text('[', *icon_options, TextFormatOption.Style.BOLD, end='')
        
        if blink:
            print_colored_text(icon, *icon_options, TextFormatOption.Style.BOLD, TextFormatOption.Style.BLINK, end='')
        else:
            print_colored_text(icon, *icon_options, TextFormatOption.Style.BOLD, end='')
        
        print_colored_text('] ', *icon_options, TextFormatOption.Style.BOLD, end='')
    
    print_colored_text(text, *text_options, end=end)
    

# message indicating an information
def info(text: str, blink=False) -> None:
    _message(text,
             icon='*',
             icon_options=[
                 TextFormatOption.Color.BLUE
             ], 
             blink=blink)

# message indicating an error
def error(text: str, blink=False) -> None:
    _message(text, 
             icon='-', 
             blink=blink,
             icon_options=[
                 TextFormatOption.Color.RED
             ]
    )

# message indicating a warning
def warning(text: str, blink=False) -> None:
    _message(text, 
             icon='!', 
             blink=blink,
             icon_options=[
                 TextFormatOption.Color.YELLOW
             ]
    )

# message indicating a successfully completed action
def success(text: str, blink=False) -> None:
    _message(text, 
             icon='+', 
             blink=blink,
             icon_options=[
                 TextFormatOption.Color.GREEN
             ]
    )

# prints a question and returns the answer
def ask(question: str, end=': ') -> str:
    _message(f'{question}{end}',
             icon='?',
             icon_options=[
                 TextFormatOption.Color.BLUE
             ],
             end='')
    
    return input_colored(
        TextFormatOption.Style.ITALIC,
    )

# prints a question asking the user if they want to continue executing the program
# 	a positive answer makes the program continues its normal execution
# 	a negative answer terminates the program
# optionally supports a custom question
def ask_continue(text: str=None):
    if text is not None:
        message = f'{text}. Continue? (y/N)'
    else:
        message = 'Continue? (y/N)'

    while True:
        ans = ask(message, end=' ')

        if ans.lower() == 'y':
            break
        if ans.lower() == 'n':
            sys.exit()
        


if __name__ == '__main__':
    import python.utils_dav.arg_parser as arg_parser

    options = arg_parser.add_mutually_exclusive_group()
    arg_parser.add_argument('--success',
                            help='message indicating a successfully completed action',
                            action=arg_parser.ArgumentAction.STORE_TRUE,
                            argument_group=options)
    arg_parser.add_argument('--warning',
                            help='message indicating a warning',
                            action=arg_parser.ArgumentAction.STORE_TRUE,
                            argument_group=options)
    arg_parser.add_argument('--error',
                            help='message indicating an error',
                            action=arg_parser.ArgumentAction.STORE_TRUE,
                            argument_group=options)
    arg_parser.add_argument('--blink',
                            help='blinks the icon, to make the message stand out',
                            action=arg_parser.ArgumentAction.STORE_TRUE)
    
    arg_parser.add_argument('message',
                            help='message to print',
                            type=str)
    
    args = arg_parser.parse_args()
    
    if args.success:
        success(args.message, blink=args.blink)
    elif args.warning:
        warning(args.message, blink=args.blink)
    elif args.error:
        error(args.message, blink=args.blink)
    else:
        info(args.message, blink=args.blink)
 