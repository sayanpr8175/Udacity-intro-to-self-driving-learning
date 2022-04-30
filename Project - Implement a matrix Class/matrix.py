import math
from math import sqrt
import numbers
import copy

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        if (self.h==1):
            return self.g
        
        if(self.h==2):
            return ((self.g[0][0]*self.g[1][1]) - (self.g[0][1]*self.g[1][0]))
        

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
            
        
        # TODO - your code here
        total_sum = 0
        for i in range(self.h):
            total_sum = total_sum + self.g[i][i]
        
        return total_sum
        

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        
        new_ar = copy.deepcopy(self.g)
        if (len(self.g)==1):
            new_obj = Matrix([[ 1.0/new_ar[0][0] ]])
            return new_obj
        
        
        elif (len(self.g) == 2):
            
            multifactor = 1.0 / (float(self.g[0][0]*self.g[1][1]) - float(self.g[0][1]*self.g[1][0]))
            new_matrix = [[ self.g[1][1], -self.g[0][1] ],
                      [ -self.g[1][0], self.g[0][0]] ]
            
            for i in range(self.h):
                for j in range(self.w):
                    new_matrix[i][j] = multifactor*new_matrix[i][j]
            new_mat_obj = Matrix(new_matrix)
            
            return new_mat_obj
        
        
        

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        def get_column(matrix, column_num):
            column = []
            for i in range(len(matrix)):
                column.append(matrix[i][column_num])
            return column
        matrix_transpose = []
        for i in range(self.w):
            matrix_transpose.append(get_column(self.g, i))
            
        new_mat_obj = Matrix(matrix_transpose)
        
        return new_mat_obj
            
        

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        
        print("it is pos  " ,self.g)
        print("it is negative  " ,other.g)
        matrixSum = []
        row = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j]+other.g[i][j])
            matrixSum.append(row)
        
        newMatObj = Matrix(matrixSum)
        print(newMatObj.g)
        
        return newMatObj

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        
        newMatObj = Matrix(copy.deepcopy(self.g))
        new_array = []
        print("positive ",self.g)
        
        for i in range(newMatObj.h):
            #temp = []
            for j in range(newMatObj.w):
                #temp.append(-1 * newMatObj.g[i][j])
                newMatObj.g[i][j] = -1*(newMatObj.g[i][j])
            #new_array.append(temp)
        print("negative ",newMatObj.g)
        print("sub repeat positive ",self.g)
        return newMatObj
        
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        
        matrixSum = []
        row = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j]-other.g[i][j])
            matrixSum.append(row)
        
        newMatObj = Matrix(matrixSum)
        
        return newMatObj
        
        

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        def get_row(matrix, row):
            return matrix[row]
        
        def get_column(matrix, column_num):
            column = []
            for i in range(len(matrix)):
                column.append(matrix[i][column_num])
            return column
        
        def dot_product(vector_one, vector_two):
            dotSum = 0
            if(len(vector_one) == len(vector_two)):
                for i in range(len(vector_one)):
                    dotSum += vector_one[i]*vector_two[i]
            return dotSum
        
        m_rows = self.h
        p_cols = other.w
        
        matrixA = copy.deepcopy(self.g)
        matrixB = copy.deepcopy(other.g)
        
        result = []
        
        for i in range(m_rows):
            nw_row = get_row(matrixA, i)
            nw_storage = []
            for j in range(p_cols):
                nw_col = get_column(matrixB, j)
                
                nw_storage.append(dot_product(nw_row, nw_col))
                
            result.append(nw_storage)
            
        
        new_mat_obj = Matrix(result)
        
        return new_mat_obj
        
        
        

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        
        newMatObj = Matrix(self.g)
        doubled = []
        
        if isinstance(other, numbers.Number):
            
            #   
            # TODO - your code here
            #
            
            for i in range(self.h):
                temp = []
                for j in range(self.w):
                    temp.append(other * self.g[i][j])
                    
                doubled.append(temp)
                    
        return doubled
            
            
            
            