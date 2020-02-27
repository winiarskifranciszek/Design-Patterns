from director import Director

from big_builder import BigBuilder

def main():
    bigOne = BigBuilder()

    director = Director()

    print("Big one")
    director.setBuilder(bigOne)
    big = director.getSpeaker()
    big.show()
    print ("")

if __name__ == "__main__":
    main()