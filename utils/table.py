class Seat:     
               
    def __init__(self):
        self.free = True
        self.occupant = ""

    def set_occupant(self, name):
        self.free = False
        self.occupant = name

    def remove_occupant(self):
            self.free = True
            self.occupant = ""


class Table:
           
    def __init__(self, capacity = 4):
        self.capacity = capacity
        self.seats = [] 

    def has_free_spot(self, free):
        self.free = True
        return any(seat.free for seat in self.seats)
    
    def assign_seat(self, name):
        for seat in self.seats:
         if seat.free:
              seat.set_occupant(name)
              return (f"Seats if for {name}")

    def left_capacity(self):
         return sum(1 for seat in self.seats if seat.free) 
        
