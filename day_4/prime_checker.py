class PrimeChecker(object):
    def __init__(self, number=''):
        if number == '':
            self.number = 0
        else:
            self.number = int(number)

    def is_prime(self):
        count = 0
        x = self.number
        if x < 2:
            return False
        elif x == 2:
            return True
        elif x == 0:
            return False
        else:
            for i in range(2, x):
                if x % i == 0:
                    count += 1
            if count >= 1:
                return False
            else:
                return True

prime = PrimeChecker('41')
prime = PrimeChecker('')
print prime.is_prime()