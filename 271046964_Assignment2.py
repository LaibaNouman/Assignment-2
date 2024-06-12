import pickle

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def display_info(self):
        print(f"Username: {self.username}\nPassword: {self.password}")

def signup_user():
    print("\nWELCOME TO CINEMA!\n")
    username = input("Enter your  Username: ")
    password = input("Enter your  Password: ")
    print("Sign Up completed!")
    return User(username, password)

def save_user_data(user_data):
    with open('user_data.pkl', 'wb') as file:
        pickle.dump(user_data, file)

def load_user_data():
    with open('user_data.pkl', 'rb') as file:
        return pickle.load(file)

user_data = signup_user()
save_user_data(user_data)

class AdminMovie:

    def __init__(self, movie_id, title, duration, seats):
        self.movie_id = movie_id
        self.title = title
        self.duration = duration
        self.seats = seats
        
    def display_movie_info(self):
        print(f"\nMovie ID: {self.movie_id}\nTitle: {self.title}\nDuration: {self.duration}\nAvailable seats: {self.seats}")

def list_movies():
    movie1 = AdminMovie(1, "The Omen", "2 hours", 100)
    movie2 = AdminMovie(2, "Annabelle Creation", "2.5 hours", 120)
    movie3 = AdminMovie(3, "Conjuring", "2.5 hours", 80)
    movie4 = AdminMovie(4, "Sabrina", "3 hours", 110)
    movies_list = [movie1, movie2, movie3, movie4]
    for movie in movies_list:
        movie.display_movie_info()

class Screen:
    def __init__(self, screen_id):
        self.screen_id = screen_id

    def display_screen_info(self):
        print(f"The number of screens available for this Title are: {self.screen_id}\n")

class TimeSlot:
    def __init__(self, t, timeslots):
        self.timeslots = timeslots
        self.t = t

    def display_timeslot_info(self):
        print(f"{self.t}. {self.timeslots}")

class Ticket:
    def __init__(self, seats, price):
        self.seats = seats
        self.price = price

    def display_ticket_info(self, movie_title, time_slot):
        self.movie_title = movie_title
        self.time_slot = time_slot
        total_price = self.seats * self.price
        print(f"\nDETAILS SHOWN BELOW:\nMovie: {self.movie_title}\nTime Slot: {self.time_slot}\nNumber of Seats: {self.seats}\nPrice per Seat: ${self.price}\nTotal Price: ${total_price}")

def user_selection():
    while True:
        user_input = int(input("\nEnter the movie number you want tickets for: "))

        if user_input == 4:
            screen = Screen(2)
            screen.display_screen_info()
            print("Available Time slots are:")
            timeslot1 = TimeSlot("1", "6:00 PM - 9:00 PM")
            timeslot2 = TimeSlot("2", "9:30 PM - 12:30 AM")
            movie_title = "Sabrina"
            timeslot1.display_timeslot_info()
            timeslot2.display_timeslot_info()
            confirmation = input("\nAre you sure you want to continue? (y/n): ")
            if confirmation == "y":
                    user_selection2 = int(input("\nEnter the desired time slot: "))    
                    seats_no = int(input("\nEnter the number of seats you want to book (5$ each): "))
                    details = Ticket(seats_no, 5)
                    if user_selection2 == 1:
                        details.display_ticket_info(movie_title, "6:00 AM - 9:00 AM")
                    elif user_selection2 == 2:
                        details.display_ticket_info(movie_title, "9:30 AM - 12:30 AM")
                    break
            else:
                    list_movies()
        elif user_input == 3:
            screen = Screen(1)
            screen.display_screen_info()
            print("Available Time slots are:")
            timeslot1 = TimeSlot("1", "6:00 AM - 9:00 AM")
            movie_title = "Conjuring"
            timeslot1.display_timeslot_info()
            confirmation = input("\nAre you sure you want to continue? (y/n): ")
            if confirmation == "y":
                    user_selection2 = int(input("\nEnter the desired time slot: "))
                    seats_no = int(input("\nEnter the number of seats you want to book (5$ each): "))
                    details = Ticket(seats_no, 5)
                    if user_selection2 == 1:
                        details.display_ticket_info(movie_title, "6:00 AM - 9:00 AM")
                    break
            else:
                    list_movies()
        elif user_input == 2:
            screen = Screen(4)
            screen.display_screen_info()
            print("Available Time slots are:")
            timeslot1 = TimeSlot("1", "6:00 PM - 9:00 PM")
            timeslot2 = TimeSlot("2", "9:30 PM - 12:30 AM")
            timeslot3 = TimeSlot("3", "1:00 AM - 3:00 AM")
            timeslot4 = TimeSlot("4", "3:30 AM - 6:30 AM")
            movie_title = "Annabelle Creation"
            timeslot1.display_timeslot_info()
            timeslot2.display_timeslot_info()
            timeslot3.display_timeslot_info()
            timeslot4.display_timeslot_info()
            confirmation = input("\nAre you sure you want to continue? (y/n): ")
            if confirmation == "y":
                    user_selection2 = int(input("\nEnter the desired time slot: "))
                    seats_no = int(input("\nEnter the number of seats you want to book (5$ each): "))
                    details = Ticket(seats_no, 5)  
                    if user_selection2 == 1:
                        details.display_ticket_info(movie_title, "6:00 PM - 9:00 PM")
                    elif user_selection2 == 2:
                        details.display_ticket_info(movie_title, "9:30 PM - 12:30 AM")
                    elif user_selection2 == 3:
                        details.display_ticket_info(movie_title, "1:00 AM - 3:00 AM")
                    elif user_selection2 == 4:
                        details.display_ticket_info(movie_title, "3:30 AM - 6:30 AM")
                    break
            else:
                    list_movies()
        elif user_input == 1:
            screen = Screen(3)
            screen.display_screen_info()
            print("Available Time slots are:")
            timeslot1 = TimeSlot("1", "6:00 PM - 9:00 PM")
            timeslot2 = TimeSlot("2", "9:30 PM - 12:30 AM")
            timeslot3 = TimeSlot("3", "1:00 AM - 3:00 AM")
            movie_title = "The Omen"
            timeslot1.display_timeslot_info()
            timeslot2.display_timeslot_info()
            timeslot3.display_timeslot_info()
            confirmation = input("\nAre you sure you want to continue? (y/n): ")
            if confirmation == "y":
                    user_selection2 = int(input("\nEnter the desired time slot: "))
                    seats_no = int(input("\nEnter the number of seats you want to book (5$ each): "))
                    details = Ticket(seats_no, 5)
                    if user_selection2 == 1:
                        details.display_ticket_info(movie_title, "6:00 PM - 9:00 PM")
                    elif user_selection2 == 2:
                        details.display_ticket_info(movie_title, "9:30 PM - 12:30 AM")
                    elif user_selection2 == 3:
                        details.display_ticket_info(movie_title, "1:00 AM - 3:00 AM") 
                    elif user_selection2 >= 4:
                        print("Invalid choice was made. Please try again later..")
                    break
            else:
                    list_movies()
        if user_input >= 4:
            print("Invalid choice was made.")
    
def login_page():
    
    print("\nWelcome, please enter your username and password to access the movie lists.\n")
    
    count = 0
    
    while count < 3:
        username = input("Please Enter the username: ")
        password = input("Please enter the password: ")

        if username == user_data.username and password == user_data.password:
            print("\nLogged in Successful!\n")
            list_movies()
            user_selection()
            break
        else:
            count += 1
            print (f"Incorrect password/username! ({count}/3)")

        if count >= 3:
            return ("Out of tries, please try again later!")

login_page()