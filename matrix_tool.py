import numpy as np

# Function to input matrix
def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    
    print(f"Enter elements of {name} row-wise:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    return np.array(matrix)

# Display matrix nicely
def display_matrix(matrix, title="Result"):
    print(f"\n{title}:")
    print(matrix)

# Main program
def main():
    print("===== MATRIX OPERATIONS TOOL =====")
    
    while True:
        print("\nChoose Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        try:
            if choice == '1':
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")
                result = A + B
                display_matrix(result, "Addition Result")

            elif choice == '2':
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")
                result = A - B
                display_matrix(result, "Subtraction Result")

            elif choice == '3':
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")
                result = np.dot(A, B)
                display_matrix(result, "Multiplication Result")

            elif choice == '4':
                A = input_matrix("Matrix")
                result = A.T
                display_matrix(result, "Transpose Result")

            elif choice == '5':
                A = input_matrix("Matrix")
                if A.shape[0] != A.shape[1]:
                    print("Determinant only exists for square matrices!")
                else:
                    result = np.linalg.det(A)
                    print(f"\nDeterminant: {result}")

            elif choice == '6':
                print("Exiting program...")
                break

            else:
                print("Invalid choice! Try again.")

        except Exception as e:
            print("Error:", e)

# Run program
if __name__ == "__main__":
    main()