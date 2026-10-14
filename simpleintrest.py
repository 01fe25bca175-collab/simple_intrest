import sys

def ssimple_intrest(principal, interest, time):
    return (principal)*intrest*time)/100

if __name__ == "__main__":
    p = int(input("Enter princiopal amt"))
    i = float(input("Enter intrest"))
    t = int(input("Enter the time in months"))

    print("simple intrest is:", simple_intrest(p, i, t))