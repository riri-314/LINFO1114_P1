import numpy as np
import csv
from algorithms.dijkstra import Dijkstra
from algorithms.bellman_ford import Bellman_Ford
from algorithms.floyd_warshall import Floyd_Warshall


def csv_to_matrix(filename):
    csv_file = open(filename, 'r')
    data = csv.reader(csv_file)

    # Create empty list to store the data
    data_matrix = []

    # Loop through the rows in the csv and append them to the list
    for row in data:
        data_matrix.append(row)

    # Convert the list to a numpy array
    data_matrix = np.array(data_matrix)

    # Convert each element of the array to a numpy float
    data_matrix = data_matrix.astype(float)

    # Return the resulting matrix
    return data_matrix



#funtion that help in the process of manually translating the .jpg source graph to the numpy matrix
def is_symmetric(matrix, N):
  for i in range(N):
    for j in range(N):
      if (matrix[i][j] != matrix[j][i]):
        #print("i j")
        #print(i)
        #print(j)
        #print(mat[i][j])
        #print(mat[j][j])
        return False
  return True

def check_matrix_equality(matrix_list):
    # initialize the flag
    flag_equal = True
    # check the equality of each matrix in the list
    for i in range(len(matrix_list)-1):
        if not np.array_equal(matrix_list[i], matrix_list[i+1]):
            flag_equal = False
            break
    # return the flag
    return flag_equal


def main(input_file):
    try:
        # Test converting csv to matrix 
        matrix = csv_to_matrix(input_file)
        # Testing symmetry of the matrix
        if (is_symmetric(matrix, 10) != True):
            print("Error: Matrix is not symmetric")
            return -1
        else:
            print("Input Matrix:")
            print(matrix)
            
            print("Dijkstra output: ")
            dijkstra = Dijkstra(matrix)
            print(dijkstra)
            
            print("Belleman Ford output: ")
            bellman_ford = Bellman_Ford(matrix)
            print(bellman_ford)
            
            print("Floyd Warshall output: ")
            floyd_warshall = Floyd_Warshall(matrix)
            print(floyd_warshall)
            
            matrix_list=[dijkstra, bellman_ford, floyd_warshall]
            flag = check_matrix_equality(matrix_list)
            print("Output matrix are the same: ", flag)

            return 0
            
    except:
        # Return error message if converting to matrix failed
        # May be caused by a non square matrix, common error
        print("Error: converting csv to matrix")
        return -1


# Run 
main("graph28.csv")