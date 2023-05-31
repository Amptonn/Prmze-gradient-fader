import sys

def hex_to_rgb(hex_color):
    # Remove "#" if it's present
    if hex_color.startswith('#'):
        hex_color = hex_color[1:]

    if len(hex_color) != 6:
        print(f"Invalid Hex Colour: {hex_color}")
        sys.exit(0)

    r = int(hex_color[:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return (r, g, b)

def check_rgb(rgb, og):
    if not len(rgb) == 3:
        print(f"Invalid Colour: {og}")
        sys.exit(0)
    try:
        if 0 <= int(rgb[0]) <= 255 and 0 <= int(rgb[1]) <= 255 and 0 <= int(rgb[2]) <= 255:
            return True
        else:
            print(f"Invalid Colour: {og}")
            sys.exit(0)
    except ValueError:
        print(f"Invalid Colour: {og}")
        sys.exit(0)

def gradient(startrgb,endrgb,text, textcolor):
        changer = int((int(endrgb[0]) - int(startrgb[0]))/len(text))
        changeg = int((int(endrgb[1]) - int(startrgb[1]))/len(text))
        changeb = int((int(endrgb[2]) - int(startrgb[2]))/len(text))
        r = int(startrgb[0])
        g = int(startrgb[1])
        b = int(startrgb[2])
        for letter in text:
            if letter == '\n': pass
            with open('output.tfx', 'a', encoding='utf8') as f:
                f.write(f"\x1b[48;2;{r};{g};{b};38;2;{textcolor[0]};{textcolor[1]};{textcolor[2]}m{letter}\033[0m")
            r += changer
            g += changeg
            b += changeb

def main():
    direction = "hori"

    textcolor_hex = input("Enter text colour (#hex): ")
    textcolor = hex_to_rgb(textcolor_hex)
    check_rgb(textcolor, textcolor_hex)

    colour1 = input("Enter start colour (r,g,b or #hex): ")
    if colour1.startswith('#'):
        startcolour = hex_to_rgb(colour1)
    else:
        startcolour = tuple(colour1.split(','))
    check_rgb(startcolour, colour1)

    colour2 = input("Enter end colour (r,g,b or #hex): ")
    if colour2.startswith('#'):
        endcolour = hex_to_rgb(colour2)
    else:
        endcolour = tuple(colour2.split(','))
    check_rgb(endcolour, colour2)

    file_name = "input.txt"

    try:
        if direction == "verti" or direction == "verticle":
            banner = open(file_name, "r", encoding="utf8").read()
            output_lines = banner.split("\n")
            r = int(startcolour[0])
            g = int(startcolour[1])
            b = int(startcolour[2])
            for x in output_lines:
                changer = int((int(endcolour[0]) - int(startcolour[0]))/len(output_lines))
                changeg = int((int(endcolour[1]) - int(startcolour[1]))/len(output_lines))
                changeb = int((int(endcolour[2]) - int(startcolour[2]))/len(output_lines))
                rgb_code = f"\x1b[48;2;{r};{g};{b};38;2;{textcolor[0]};{textcolor[1]};{textcolor[2]}m"
                r += changer
                g += changeg
                b += changeb
                with open('output.tfx', 'a', encoding='utf8') as f:
                    f.write(f"{rgb_code}{x}\033[0m\n")
            print("Written to output.tfx")
        elif direction == "hori" or direction == "horizontal":
            with open(file_name, 'r', encoding='utf8') as f:
                for x in f.readlines():
                    gradient(startcolour, endcolour, x, textcolor)
            with open('output.tfx', 'a', encoding='utf8') as f:
                f.write(f"\033[0m\n")
            print("Written to output.tfx")
    except IndexError:
        print("Invalid Args!\nExpected format: vert/hori r,g,b1 r,g,b2 text_art.file")
        sys.exit(0)
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Please verify and try again.")
        sys.exit(0)

if __name__ == '__main__':
    with open('output.tfx', 'w') as f:
        f.write("")
    main()
