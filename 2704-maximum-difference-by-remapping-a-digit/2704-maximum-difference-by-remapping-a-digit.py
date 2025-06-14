class Solution:
    def minMaxDifference(self, num: int) -> int:
        # num: int

        digit_to_arr = [int(digit) for digit in str(num)]
        print(digit_to_arr)
        
        to_map = None
        
        for i in range(len(digit_to_arr)):
            if digit_to_arr[i] < 9:
                to_map = digit_to_arr[i]
                break
        
        print("to_map", to_map)
        
        _max = num
        if to_map != None:
            _max = int(''.join([str(num) if num != to_map else '9' for num in digit_to_arr]))
        
        print("_max", _max)
        
        first = digit_to_arr[0]
        
        print('first', first)

        _min = int(''.join([str(num) if num != first else '0' for num in digit_to_arr]))
        
        print('_min', _min)

        return _max - _min