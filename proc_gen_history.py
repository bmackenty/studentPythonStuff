# procedural generator to write a brief history
import random

origin_1 = ["Born", "Hatched", "Invoked", "Discovered"]
origin_2 = ["in the land of", "in the wilds of", "in the forest of", "in the ocean of", "in the small village of", "in the modest hamlet of"]
origin_3 = ["Tr'lor", "Kor'mer", "Kobiyashi", "Greenest", "Mordora", "Gondor'e", "Rivendell", "Mirkwood"]

for i in range(10):
    story = random.choice (origin_1) + " " + random.choice(origin_2) + " " + random.choice(origin_3)
    print(story)
