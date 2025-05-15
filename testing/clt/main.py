from time import sleep

# object creation

class Coffee():
    def __init__(self):
        self.isfull = True
        self.ml = 200

    def is_mug_full(self):
        if self.ml == 0:
            self.isfull = False
            return False
        return True

    def refill(self):
        print("Refilling coffee mug...")
        self.ml = 200
        sleep(2)
        self.isfull = True

# init #
coffee = Coffee()
def work():
    print("Working...")
    sleep(2)
    coffee.ml -= 50
    print(f"Remaining coffee {coffee.ml}")

def main():
    print("=========================================")
    print("=             WORKING AS CLT            =")
    print("=========================================")
    while True:
        work()
        if coffee.is_mug_full():
            continue
        else:
            coffee.refill()

# main initialization
if __name__ == "__main__":
    main()