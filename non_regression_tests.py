from gestion_jdr3_tests import *

assert not image_will_be_out_of_screen(105, 5, 6, 800)
assert image_will_be_out_of_screen(105, 5, 7, 800)


assert first_image_on_x(0)
assert not first_image_on_x(1)