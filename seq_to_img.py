#!/usr/bin/env python3

from PIL import Image, ImageDraw

# this function takes in a sequence and color code for each combination
# and  makes a image using that color code dictionary and saves its with the given name
# for example: sequence -> "ATG" will follow as below
#  A T G
# A
# T
# G
# @param imageWidth {Integer} -> desired images width
# @param imageHeight {Integer} -> desired images height
# @param seqColoCode {Dictionary} -> dictionary containing possible combination and respective color code(RGB)
#                                    for example: { "AT": (255, 0, 255), "AG": (255, 0, 0) }
# @param seq {String} -> sequence as a string
# @param imgName {String} -> image name to be saved with


def Sequence_to_Image(imageWidth, imageHeight, seqColoCode, seq, imgName):

    # Create a blank image with white background
    image = Image.new("RGB", (imageWidth, imageHeight), "white")
    draw = ImageDraw.Draw(image)

    # Define the dimensions of the matrix
    matrix_size = len(sequence)
    cell_width = imageWidth // matrix_size
    cell_height = imageHeight // matrix_size

    # Draw the matrix
    for i in range(matrix_size):
        for j in range(matrix_size):
            # Define the coordinates of the current cell
            string = sequence[j]+sequence[i]
            x1 = j * cell_width
            y1 = i * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height

            if string in dic.keys():
                draw.rectangle([x1, y1, x2, y2], fill=seqColoCode[string])
            else:
                string = string[::-1]
                draw.rectangle([x1, y1, x2, y2], fill=seqColoCode[string])

    # Save the image as a file
    image.save(imgName + ".png")


# driver code
if __name__ == "__main__":

    sequence = "AGTGATGAAATGAGTATGAGTGATGAAATGAGTATGATGAGTGATGAAATGAGTATGAGTGATGATGAGTGATGAAATGAATGAAATGAGTATGAGTGATGAAATGAGTATGAGTGATGAAATGAGTATGAGTGATGAAATGAGTATGAGTGATGAAATGAGTATGAGTGATGAAATGAGT"
    dic = {
        "AA": (0, 191, 255),
        "AT": (144, 238, 144),
        "AG": (32, 178, 170),
        "TT": (255, 127, 80),
        "TG": (255, 215, 0),
        "GG": (218, 165, 32)
    }

    Sequence_to_Image(600, 600, dic, sequence, "wow")
