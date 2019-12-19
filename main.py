import SnakeAI.main
import ShakespeareAI.main

def main():
    ## NOT WORKING
    print("Available projects:")
    print("SnakeAI")
    print("ShakespeareAI")

    s = input()
    if s[0] == 's' or s[0] == 'S':
        SnakeAI.main()
    else:
        ShakespeareAI.main()

if __name__ == "__main__":
    main()
