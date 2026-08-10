class StudentSports:
    def __init__(self, name):
        self.name = name
        self.sports = []

    def add_sport(self, sport_name):
        self.sports.append(sport_name)
        print(f"Added {sport_name} for {self.name}.")

    def show_sports(self):
        print(f"{self.name} plays these sports: {self.sports}")

    def check_sport(self, sport_name):
        if sport_name in self.sports:
            print(f"Yes, {self.name} plays {sport_name}.")
        else:
            print(f"No, {self.name} does not play {sport_name}.")

# Create a student and test the methods
student1 = StudentSports("Alex")
student1.add_sport("Cricket")
student1.add_sport("Football")
student1.show_sports()
student1.check_sport("Cricket")
