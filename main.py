from PIL import Image
from color_correct import color_correct
from generate_shadows import generate_shadow

try:
    person_img = Image.open('images/person.png').convert('RGBA')
    background_img = Image.open('images/backgrouund_img.jpeg').convert('RGBA')
except FileNotFoundError as e:
    print(f"Error: {e}. Make sure the image files are in the same directory.")
    exit(0)


scale = 0.4
new_size = (int(person_img.width * scale), int(person_img.height * scale))
person_img = person_img.resize(new_size, Image.LANCZOS)


position = (70, background_img.height - person_img.height + 30)


corrected_person = color_correct(person_img, background_img, position)
# corrected_person.convert('RGB').save('output/color_corrected_debug.png', 'PNG')

shadow_img = generate_shadow(corrected_person, position)
# shadow_img.convert('RGB').save('output/shadow_debug.png', 'PNG')


final_img = background_img.copy()

final_img.paste(shadow_img, (position[0] - 70, position[1] - 30), shadow_img)

final_img.paste(corrected_person, position, corrected_person)


final_img.convert('RGB').save('output/final_composite_image9.jpeg', 'JPEG')



