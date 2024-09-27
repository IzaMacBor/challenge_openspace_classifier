import random
import pandas as pd
from table import Table


class Openspace:

    def __init__ (self, number_of_tables, table):
        self.number_of_tables = number_of_tables
        self.table = table
    

    def organize(self,names):
        random.shuffle(names)
        for name in names:
            assigned = False
            for table in self.number_of_tables:
                if table.assign_seat(name):
                    assigned = True
                    break
                if not assigned:
                    print(f"No more seats for {name}")

    def display(self):
        for i, table in enumerate(self.table, 1):
            print(f"Table {i}:")
            for j, seat in enumerate(table.seats, 1):
                status = seat.occupant if seat.occupant else "Free"
                print(f"Seat {j}: {status}")
            print() 

    def store(self, filename):
        data = []
        for i, table in enumerate(self.table, 1):
            for j, seat in enumerate(table.seats, 1):
                data.append({
                    "Table": i,
                    "Seat": j,
                    "Occupant": seat.occupant if seat.occupant else "Free"
                })
        
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        print(f"Classifier saved in {filename}")