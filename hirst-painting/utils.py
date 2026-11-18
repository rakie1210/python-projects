import colorgram

def color_extractor():
    """ This function extracts colors from hirst-painting images using colorgram."""
    colors = colorgram.extract('damien-hirst-spot-painting.jpg', 30)

    hirst_painting_colors = list()
    for color in colors:
        rgb_color = color.rgb
        red = rgb_color[0]
        green = rgb_color[1]
        blue = rgb_color[2]
        color_tuple = (red, green, blue)
        hirst_painting_colors.append(color_tuple)

    return hirst_painting_colors