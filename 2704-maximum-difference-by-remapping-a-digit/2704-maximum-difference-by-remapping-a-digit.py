class Solution:
    def minMaxDifference(self, num: int) -> int:
        # num: int

        num_str = str(num)
        
        to_map = None
        
        for i in range(len(num_str)):
            if num_str[i] != '9':
                to_map = num_str[i]
                break
        
        print("to_map", to_map)

        temp = num_str
        
        _max = num
        if to_map != None:
            _max = int(num_str.replace(to_map, '9'))
        
        print("_max", _max)
        
        first = temp[0]
        
        print('first', first)

        _min = int(temp.replace(first, '0'))
        
        print('_min', _min)

        return _max - _min