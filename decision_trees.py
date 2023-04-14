import numpy as np
import matplotlib.pyplot as plt
import sys
import hashlib
from datetime import datetime

if len(sys.argv) != 4:
    print("python decision_trees.py {num of trees} {num of options} {question number Вопрос № XXX}")
    exit(0)

NUM_OF_TREES = int(sys.argv[1])
NUM_OF_OPTIONS = int(sys.argv[2])
QUESTION_NUM = int(sys.argv[3])

now = datetime.now()
current_time = now.strftime("%H:%M")

to_hash = f"DT_{NUM_OF_TREES}_{NUM_OF_OPTIONS}_{QUESTION_NUM}_{current_time}"
res_of_hash = hashlib.md5(to_hash.encode())

seed2 = int(res_of_hash.hexdigest(), 16)
seed2 %= 2**32 - 1
print(seed2, type(seed2))

letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

np.random.seed(QUESTION_NUM)
npoptions = np.random.choice(a=NUM_OF_OPTIONS, size=NUM_OF_TREES//2)

np.random.seed(seed2)
npoptions2 = np.random.choice(a=NUM_OF_OPTIONS, size=NUM_OF_TREES//2)

npoptions = np.concatenate([npoptions, npoptions2], axis=0)

options = [0 for _ in range(NUM_OF_OPTIONS)]

for value in npoptions:
    options[value] += 1

print(options)
print("Деревья решили, что ответ: ", letters[options.index(max(options))])

plt.bar([letters[i] for i in range(NUM_OF_OPTIONS)], options)
plt.show()