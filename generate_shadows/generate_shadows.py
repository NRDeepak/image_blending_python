import numpy as np
from PIL import Image, ImageFilter


def generate_shadow(person, position):
    """
    Generates a shadow for the person.
    """

    shadow = Image.new('RGBA', (person.width + 100, person.height + 100), (0, 0, 0, 0))
    person_alpha = person.split()[3]
    shadow_layer = Image.new('RGBA', person.size, (40, 40, 40, 150)) # Dark, semi-transparent shadow
    shadow.paste(shadow_layer, (50, 50), mask=person_alpha)


    shadow = shadow.transform(shadow.size, Image.AFFINE, (1, 0.5, -50, 0, 1, 0), resample=Image.BICUBIC)
    shadow = shadow.filter(ImageFilter.GaussianBlur(15))

    return shadow