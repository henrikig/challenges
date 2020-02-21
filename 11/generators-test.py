from itertools import permutations


def num_gen():
    yield 1
    yield 2
    yield 3


def squares(loops=5):
    num = 1

    for i in range(loops):
        yield num*num
        num += 1


def permutations_draw(draw):
    for i in range(1, 8):
        yield from list(permutations(draw, i))


demo_gen = num_gen()

try:
    while True:
        print(next(demo_gen))
except StopIteration:
    print("Iteration Done")

try:
    square_gen = squares(15)
    for num in square_gen:
        if num > 1000:
            break
        print(num)
    next(square_gen)
except StopIteration:
    print("Generator is done.")

for result in permutations_draw(["lisa", "tom", "jonas", "marcus"]):
    print(result)
