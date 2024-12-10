class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self):
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"Distance:{self.distance}, Rate per km:{self.rate_per_km}, fare:{self.fare}")

def main():
    # your program
    Ride1=TaxiRide(5)
    Ride1.distance=(6)
    Ride1.calculate_fare()
    Ride1.print_receipt()

if __name__ == "__main__":
    main()
