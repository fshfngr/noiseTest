# noiseTest.py
# made by Laban Lundquist
from PIL import Image
import random, time

class cell:
    def __init__(self, color=(0)):
        self.color = color

def addTuples(arg1, arg2):
    return (arg1[0] + arg2[0], arg1[1] + arg2[1])

try:
    resolutionInput = int(input("Resolution: "))
    resolution = (resolutionInput, resolutionInput)
except:
    resolution = (64, 64)
resolution = addTuples(resolution, (40, 40))

# start timer
t1 = time.time()

cells = {}
for w in range(resolution[0]):
    for h in range(resolution[1]):
        cells[(w, h)] = cell(0)

img = Image.new("L", (resolution[0], resolution[1]), 0)

try:
    density = int(input("Density (higher numbers will result in lower densities, lowest is 1): "))
    if density == 0: density = 1
except:
    density = 0

for w in range(resolution[0]):
    for h in range(resolution[1]):
        if random.randint(0, density) == 0:
            cells[(w, h)].color = 255

offsets = (
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
)

intensity = int(input("Intensity: "))

for _ in range(intensity):
    for w in range(resolution[0]):
        for h in range(resolution[1]):
            for i in range(8):
                try:
                    if cells[addTuples((w, h), offsets[i])].color > 200:
                        cells[(w, h)].color = 199
                    else:
                        cells[(w, h)].color = int(((cells[addTuples((w, h), offsets[i])].color + cells[(w, h)].color) / 2))
                except:
                    pass

for w in range(resolution[0]):
    for h in range(resolution[1]):
        img.putpixel((w, h), cells[(w, h)].color)

img = img.crop((20, 20, resolution[0]-20, resolution[1]-20))

img.save("image.png")

# end timer
t2 = time.time()
print(f"Finished at: {round(t2-t1, 2)}")

img.show()
