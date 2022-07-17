class ArithmeticPrograssion():
    def __init__(self, a, d) -> None:
        self.a = a
        self.d = d

    
    def get_n_part(self, n: int):
        n_part = self.a + n * self.d
        return n_part


    def sum_n_part(self, n: int):
        sum_n = ((self.a + self.get_n_part(n))/2) * n
        return sum_n