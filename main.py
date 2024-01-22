# We first create a dictionnary to store each letter in ASCII art

ascii_art_dict = {
    'A': ['  A  ', ' A A ', 'AAAAA', 'A   A', 'A   A'],
    'B': ['BBBB ', 'B   B', 'BBBB ', 'B   B', 'BBBB '],
    'C': [' CCC ', 'C   C', 'C    ', 'C   C', ' CCC '],
    'D': ['DDDD ', 'D   D', 'D   D', 'D   D', 'DDDD '],
    'E': ['EEEEE', 'E    ', 'EEE  ', 'E    ', 'EEEEE'],
    'F': ['FFFFF', 'F    ', 'FFF  ', 'F    ', 'F    '],
    'G': [' GGG ', 'G    ', 'G  GG', 'G   G', ' GGG '],
    'H': ['H   H', 'H   H', 'HHHHH', 'H   H', 'H   H'],
    'I': [' III ', '  I  ', '  I  ', '  I  ', ' III '],
    'J': ['  JJJ', '   J ', '   J ', 'J  J ', ' JJ  '],
    'K': ['K   K', 'K  K ', 'KK   ', 'K  K ', 'K   K'],
    'L': ['L    ', 'L    ', 'L    ', 'L    ', 'LLLLL'],
    'M': ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M'],
    'N': ['N   N', 'NN  N', 'N N N', 'N  NN', 'N   N'],
    'O': [' OOO ', 'O   O', 'O   O', 'O   O', ' OOO '],
    'P': ['PPPP ', 'P   P', 'PPPP ', 'P    ', 'P    '],
    'Q': [' QQQ ', 'Q   Q', 'Q   Q', 'Q  Q ', ' QQ Q'],
    'R': ['RRRR ', 'R   R', 'RRRR ', 'R R  ', 'R  RR'],
    'S': [' SSS ', 'S    ', ' SSS ', '    S', 'SSSS '],
    'T': ['TTTTT', '  T  ', '  T  ', '  T  ', '  T  '],
    'U': ['U   U', 'U   U', 'U   U', 'U   U', ' UUU '],
    'V': ['V   V', 'V   V', 'V   V', ' V V ', '  V  '],
    'W': ['W   W', 'W   W', 'W W W', 'WW WW', 'W   W'],
    'X': ['X   X', ' X X ', '  X  ', ' X X ', 'X   X'],
    'Y': ['Y   Y', ' Y Y ', '  Y  ', '  Y  ', '  Y  '],
    'Z': ['ZZZZZ', '   Z ', '  Z  ', ' Z   ', 'ZZZZZ']
}

# Then we can define a function that store the art for a text entered by the user

def text_to_art(text):
    art_text=[' ' for i in range(5)]
    for letter in text:
        if letter in ascii_art_dict.keys():
            for index, line in enumerate(ascii_art_dict[letter]):
                art_text[index]+=(line)+' '
    return art_text

# We create a function that will display the art in the console
def from_art_to_console(art_text):
    # We know that each letter is of length 5. So we will take in account to display the figure
    for i in range(5):
        print(art_text[i])


#second option of ASCII art, with the Pyfiglet python library
import pyfiglet
def list_fonts():
    return pyfiglet.FigletFont.getFonts()

def text_to_art_pyfiglet(text, font="standard"):
    pyfiglet_obj = pyfiglet.Figlet(font=font)
    return pyfiglet_obj.renderText(text)

def from_art_to_console_pyfiglet(art_text):
    print(art_text)


print("Welcome to ASCII art!")
choice=input("Do you want the version dictionary (1) or PyFiglet (2)?")
if (choice=="2"): 
    print("Choose the font you want to use, in this list:")
    fonts = list_fonts()
    for font in fonts:
        print(font)
    font_user=input("Your choice:")

    user=input("Give a string to transform in ASCII art: ")
    text=user.upper()
    print("\n\n")
    ascii_art = text_to_art_pyfiglet(text, font=font_user)
    from_art_to_console_pyfiglet(ascii_art)
    print("\n\n")
elif (choice=="1"):
    user=input("Give a string to transform in ASCII art: ")
    text=user.upper()
    print("\n\n")
    from_art_to_console(text_to_art(text))
    print("\n\n")
else:
    print("Select a valid option.")