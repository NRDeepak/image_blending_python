import numpy as np
from PIL import Image



def color_correct(person, background, position):
    """
    Performs basic color correction by matching the mean color of the person
    to the area they will be placed on in the background.
    """
    # Get the region of the background where the person will be placed
    x, y = position
    w, h = person.size
    bg_region = background.crop((x, y, x + w, y + h))

    # Convert to numpy arrays for easier calculation
    bg_data = np.array(bg_region).astype(float)
    person_data = np.array(person).astype(float)

    # Calculate the mean color for both (ignoring transparent pixels in person)
    person_mask = person_data[:, :, 3] > 0
    bg_mean = np.mean(bg_data[:, :, :3], axis=(0, 1))
    person_mean = np.mean(person_data[person_mask, :3], axis=0)

    # Calculate the color difference and apply it
    color_correction = bg_mean - person_mean
    corrected_person_data = person_data.copy()
    corrected_person_data[person_mask, :3] += color_correction
    corrected_person_data = np.clip(corrected_person_data, 0, 255)

    return Image.fromarray(corrected_person_data.astype('uint8'), 'RGBA')