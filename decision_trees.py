import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 4:
    print("python decision_trees.py {num of trees} {num of options} {question number Вопрос № XXX}")
    exit(0)

NUM_OF_TREES = int(sys.argv[1])
NUM_OF_OPTIONS = int(sys.argv[2])
QUESTION_NUM = int(sys.argv[3])

letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

np.random.seed(QUESTION_NUM)

npoptions = np.random.choice(a=NUM_OF_OPTIONS, size=NUM_OF_TREES)

options = [0 for _ in range(NUM_OF_OPTIONS)]

for value in npoptions:
    options[value] += 1

print(options)
print("Деревья решили, что ответ: ", letters[options.index(max(options))])

plt.bar([letters[i] for i in range(NUM_OF_OPTIONS)], options)
plt.show()