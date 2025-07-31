class PrimeFactor:
    ...

    def of(self, number)-> []:
        factors = []
        if number == 1:
            return factors
        if number == 2:
            factors.append(2)
        return factors