import imageio
from PIL import Image


filenames = [
    "data/Desktop_190207_1652.ppm"
    # "data/laser01/%06d.png" % (i + 1) for i in range(50)
]

Image.open('exported/test.gif').show()

# with imageio.get_writer('export/test.gif', mode='I') as writer:
#     for filename in filenames:
#         image = imageio.imread(filename)
#         writer.append_data(image)