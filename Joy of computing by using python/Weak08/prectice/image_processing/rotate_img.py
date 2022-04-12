# in this segment will rotate the image for four times and will see the result.
from PIL import Image
import pandas

img = Image.open("aman_img.jpg")  # will open img and store it in img var as in matrix form.
# img.show()  # will open the above image in default image viewer of you pc

# now will transpose the above img i.e will change all the row into col.
# transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT) # flipping the img from left right
# transposed_img.save("fst_lr_tran.png")
#
#  # will gate original image.
# transposed_img1 = transposed_img.transpose(Image.FLIP_LEFT_RIGHT) # again flipped left right.
# transposed_img1.save("snd_lr_tran.png")
# transposed_img.show()


# tr_img = img.transpose(Image.TRANSPOSE) # fst 90degree flip
# tr_img.save("fst_nty_dr_flip.png")

# t_img = img.transpose(Image.ADAPTIVE) # 180 degree flip
# t_img.save("fst_180_deg_flip.png")
# t_img.show()


new_img = img.transpose(Image.AFFINE)
new_img.show()