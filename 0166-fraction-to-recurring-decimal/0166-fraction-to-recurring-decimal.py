class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        fraction = []

        if (numerator < 0) ^ (denominator < 0):
            fraction.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)

        fraction.append(str(numerator // denominator))
        rem = numerator % denominator

        if rem == 0:
            return ''.join(fraction)
        
        fraction.append('.')

        seen = {}

        while rem != 0:
            if rem in seen:
                fraction.insert(seen[rem], "(")
                fraction.append(")")
                break
            
            seen[rem] = len(fraction)
            rem *= 10
            fraction.append(str(rem // denominator))
            rem %= denominator
        
        return ''.join(fraction)