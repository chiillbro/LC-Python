class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = defaultdict(list)
        self.rows = rows

        for i in range(26):
            self.spreadsheet[chr(65 + i)] = [0] * (rows + 1)


    def setCell(self, cell: str, value: int) -> None:
        char = cell[0]
        val = int(cell[1:])

        self.spreadsheet[char][val] = value

    def resetCell(self, cell: str) -> None:
        char = cell[0]
        val = int(cell[1:])

        self.spreadsheet[char][val] = 0

    def getValue(self, formula: str) -> int:
        i = 1
        val1 = val2 = ""
        plus_crossed = False
        while i < len(formula):
            if formula[i] == '+':
                plus_crossed = True
                i += 1
                continue
            
            if plus_crossed:
                val2 += formula[i]
            else:
                val1 += formula[i]
            
            i += 1
        

        if not val1.isdigit():
            char = val1[0]
            val = int(val1[1:])
            val1 = self.spreadsheet[char][val]
        
        if not val2.isdigit():
            char = val2[0]
            val = int(val2[1:])
            val2 = self.spreadsheet[char][val]
        
        return int(val1) + int(val2)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)