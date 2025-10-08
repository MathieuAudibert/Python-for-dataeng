def modify_chaine(text):
    result = ""
    for char in text:
        if char != ' ':
            result += char + ' '
        else:
            result += '' + char
    print(result)

modify_chaine("aiehaoiehoaiheoiaheoi zaeaeaaeea")