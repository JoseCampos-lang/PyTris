import random
class Shapes:
    J = [[0, 1], [0, 1], [1, 1]]
    L = [[1, 0], [1, 0], [1, 1]]
    O = [[1, 1], [1, 1]]
    S = [[0, 1, 1], [1, 1, 0]]
    Z = [[1, 1, 0], [0, 1, 1]]
    I = [[1], [1], [1], [1]]
    def random_shape:
        all_shapes = [J, L, O, S, Z, I]
        return random.choice(all_shapes)
