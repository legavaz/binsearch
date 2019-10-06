

class Table(object):
    
    def __init__(self,rows, cols):
        self.field = [ [0 for _ in range(cols)] for _ in range(rows) ]
        self.rows = rows
        self.cols = cols
        
    def get_value(self, row, col):
        if  row in range(self.rows) and col in range(self.cols):
            return self.field[row][col]
        return
 
    def set_value(self, row, col,value):
        self.field[row][col] = value
    
    def n_rows(self):
        return self.rows
 
    def n_cols(self):
        return self.cols
    
    def print_value(self):
        # item_row    =   0        
        # while item_row<self.n_rows():
        #     item_cols   =   0
        #     while item_cols<self.n_cols():
        #         print(self.get_value(item_row,item_cols),end=' ')
        #         item_cols+=1
        #     print()
        #     item_row+=1 
        for i in range(self.n_rows()):
            for j in range(self.n_cols()):
                print(self.get_value(i, j), end=' ')
            print()
        
                        
            


if __name__ == "__main__":

    map = Table(3, 5)
    map.set_value(0, 1, 10)
    map.set_value(1, 2, 20)
    map.set_value(2, 3, 30)
    map.print_value()