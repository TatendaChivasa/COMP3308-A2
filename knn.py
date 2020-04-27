import sys

def main():
    argc = len(sys.argv)
    if argc < 3:
        print("Program did not receive the number of parameters needed to run")
        sys.exit()

    training = sys.argv[1]
    testing = sys.argv[2]
    algorithm = sys.argv[3]

    if "NN" in algorithm:
        k = algorithm[0]
        kNN(k)

def kNN(k):
    print("in knn")



if __name__ == "__main__":
    main()