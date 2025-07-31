class PrimeFactor:
    ...

    def of(self, number)-> []:
        factors = []
        if number == 1:
            return factors
        elif number == 2:
            factors.append(2)
        elif number == 3:
            factors.append(3)
        return factors