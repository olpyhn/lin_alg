# coding=utf-8


class Permutation:
    def __init__(self, values):
        self.n = len(values)
        self.permutation = values

    # в качестве has нужно передавать список элементов,
    # все перестановки которых мы хотим получить, например, (0, 1, 2, 3, 4, 5)
    @staticmethod
    def get_permutations(n, has):
        if n == 0:
            return [[]]
        result = []
        for v in range(n):
            permutations = Permutation.get_permutations(n - 1, has[:v] + has[v + 1:])
            for permutation in permutations:
                result.append([has[v]] + permutation)
        return result

    @staticmethod
    def get_all_subsets(arr, new_size):
        if new_size == 0:
            return [[]]
        if new_size > len(arr):
            return []
        if new_size == len(arr):
            return [arr]
        res = []
        ss = Permutation.get_all_subsets(arr[1:], new_size - 1)
        if len(ss) > 0:
            for el in ss:
                res.append([arr[0]] + el)
        res += Permutation.get_all_subsets(arr[1:], new_size)
        return res

    def get_permutation_sign(self):
        cnt = 0
        for i in range(len(self.permutation)):
            for j in range(i + 1, len(self.permutation)):
                if self.permutation[i] > self.permutation[j]:
                    cnt += 1
        if cnt % 2 == 1:
            return -1
        return 1

    def __mul__(self, other):
        if len(self.permutation) != len(other.permutation):
            raise Exception("Перестановки не могут быть разного размера")
        values = [0] * self.n
        for i in range(self.n):
            values[i] = self.permutation[other.permutation[i]]
        return Permutation(values)

    def get_inverse_permutation(self):
        values = [0] * self.n
        for i in range(self.n):
            values[self.permutation[i]] = i
        return Permutation(values)

    def __pow__(self, power, modulo=None):
        result = Permutation(list(range(self.n)))
        for _ in range(abs(power)):
            result = result * self
        if power < 0:
            return result.get_inverse_permutation()
        else:
            return result