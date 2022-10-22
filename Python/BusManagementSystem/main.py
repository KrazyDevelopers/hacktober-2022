import os
if not os.path.exists("Seats.txt"):
    with open("Seats.txt", "w+") as f:
      for i in range(1, 29):
        f.write("0 ")

class Bus:
  def __init__(self):
    self.seats = []
    with open("Seats.txt", "r") as f:
      for line in f:
        for seat in line.split():
          self.seats.append(int(seat))
  def displayAvailableSeats(self):
    availableSeats = 0
    for seat in self.seats:
      if seat == 0:
        availableSeats += 1
    print("Number of available seats = \033[1;32m ", availableSeats, "\033[0;0m")
    print("Number of non available seats = \033[1;32m", len(self.seats) - availableSeats, "\033[0;0m")
  def displaySeats(self):
    for i in range(0, len(self.seats), 4):
      for j in range(i+1, i + 5):
        if self.seats[j-1] == 0:
          print("{    ", "\033[1;32m{0:>2} \033[0;0m".format(j), end="     } ")
        else:
          print("{  ", "\033[1;31m{0:>0} \033[0;0m".format("Reserved"), end=" } ")
      print("")
  def reserveSeat(self):
    if self.seats.count(0) == 0:
      print("No available seats")
    numberOfSeats = int(input("How many seats do you want to reserve? "))
    for i in range(numberOfSeats):
      seatNum = int(input("Please select the seat you want to reserve: "))
      if seatNum > self.seats.count(0):
        print("\033[1;31m Error: Insufficient seats \033[0;0m")
        break
      elif seatNum < 0:
        print("\033[1;31mError: Invalid numbers of seats\033[0;0m")
        break
      if self.seats[seatNum-1] == 0:
        self.seats[seatNum-1] = 1
        with open("Seats.txt", "w") as f:
          for seat in self.seats:
            f.write(str(seat) + " ")
        print("\033[1;32mSeat reserved\033[0;0m")
      else:
        print("\033[1;31mSeat already reserved \033[0;0m")
        break
  def deleteSeat(self):
    process = True
    self.displaySeats()
    if self.seats.count(1) == 0:
      print("\033[1;31mNo seats reserved \033[0;0m")
      process = False
    while process:
      numberOfSeats = int(input("enter the number of reservations to delete: "))
      if numberOfSeats > self.seats.count(1):
        print("\033[1;31mError: Insufficient seats\033[0;0m")
        break
      elif numberOfSeats < 0:
        print("\033[1;31mError: Invalid numbers of seats\033[0;0m")
        break
      for i in range(numberOfSeats):
        seatNum = int(input("Please select the seat you want to delete: "))
        if self.seats[seatNum-1] == 0:
          print("\033[1;31mError: Seat not reserved\033[0;0m")
          
          break
        elif self.seats[seatNum-1] == 1:
          self.seats[seatNum-1] = 0
          with open("Seats.txt", "w") as f:
            for seat in self.seats:
              f.write(str(seat) + " ")
        else:
          print("\033[1;31mSeat already reserved\033[0;0m")
          break
      break
  def menu(self):
    print("1. Display number of availabe seats")
    print("2. Display status of all seats")
    print("3. Reserve seats")
    print("4. Delete reservation.")
    print("5. Exit")
    choice = int(input("Please select your choice [1, 2, 3, 4, or 5]: "))
    if choice == 1:
      self.displayAvailableSeats()
    elif choice == 2:
      self.displaySeats()
    elif choice == 3:
      self.reserveSeat()
    elif choice == 4:
      self.deleteSeat()
    elif choice == 5:
      exit()
    else:
      print("Please enter a number according to the given list")
    self.menu()
bus = Bus()
bus.menu()