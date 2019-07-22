from uwimg import *

# 1. Getting and setting pixels
im = load_image("data/dog.jpg")
for row in range(im.h):
    for col in range(im.w):
        set_pixel(im, col, row, 1, 0)
save_image(im, "figs/results_rafael/dog_no_green")

# 3. Grayscale image
im = load_image("data/colorbar.png")
graybar = rgb_to_grayscale(im)
save_image(graybar, "figs/results_rafael/graybar")

# 3. Grayscale image II
im = load_image("data/dog.jpg")
graybar = rgb_to_grayscale(im)
save_image(graybar, "figs/results_rafael/graydog")

# 4. Shift Image
im = load_image("data/dog.jpg")
shift_image(im, 0, .4)
shift_image(im, 1, .4)
shift_image(im, 2, .4)
save_image(im, "figs/results_rafael/overflow")

# 5. Clamp Image
clamp_image(im)
save_image(im, "figs/results_rafael/doglight_fixed")

# 6-7. Colorspace and saturation
im = load_image("data/dog.jpg")
rgb_to_hsv(im)
shift_image(im, 1, .2)
clamp_image(im)
hsv_to_rgb(im)
save_image(im, "figs/results_rafael/dog_saturated")

# 8. Channel scalling
im = load_image("data/dog.jpg")
rgb_to_hsv(im)
scale_image(im, 1, 2)
clamp_image(im)
hsv_to_rgb(im)
save_image(im,"figs/results_rafael/dog_scale_saturated_rafael")


