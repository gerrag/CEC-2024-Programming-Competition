# Custom display class
from display import Display


# ---------------- TEST - DATALOAD FUNCTION ----------------
import csv
import numpy as np

def simpleGetArray(path):
    reader = csv.reader(open(path), delimiter=",")

    # data = np.array(x).astype = float
    data = np.zeros((100, 100))

    # Populate data array
    for i, row in enumerate(reader):
        if i != 0:
            # print(row)
            # y += int(row[1])
            if row[3] != "":
                data[int(row[2])][int(row[1])] = float(row[3])
            else:
                # data is empty
                data[int(row[2])][int(row[1])] = None
    return data


basepath = "../data/"
world_path = "world_array_data_day_"
algal_path = "algal_data_day_"

def main():
    app = Display()
    
    # Upload data
    data = simpleGetArray(basepath + world_path + "1.csv")
    app.UpdateCanvas(data)

    # Set preserved button changed handler
    def handler(preserving):
        # Generate new analysis to prioritize "preserving"
        pass
    
    app.set_presreve_changed_handler(handler)
    
    # list of rig1 list and rig2 list for every day
    app.setRigCoords([[(81, 14), (79, 11), (76, 13), (79, 14), (81, 18), (77, 13), (77, 8), (72, 6), (69, 6), (69, 10), (64, 8), (61, 6), (63, 6), (64, 3), (62, 2), (66, 2), (61, 1), (59, 0), (62, 5), (60, 2), (58, 3), (57, 7), (53, 2), (49, 5), (53, 9), (54, 14), (58, 12), (61, 11), (62, 8), (67, 11)], 
                      [(3, 94), (2, 98), (1, 95), (1, 93), (6, 90), (7, 93), (2, 93), (1, 88), (2, 89), (7, 84), (8, 83), (11, 80), (14, 75), (13, 79), (13, 76), (11, 73), (14, 76), (17, 71), (15, 76), (11, 79), (14, 82), (10, 79), (9, 79), (8, 75), (7, 71), (5, 66), (0, 66), (5, 64), (1, 63), (4, 62)]])
    
    # tuple list of collected by day (helium, metal, oil)
    app.setCollected([[8, 5, 8, 3, 6, 8, 16, 19, 6, 1, 0, 2, 8, 12, 8, 5, 6, 14, 14, 20, 5, 9, 7, 7, 14, 4, 15, 16, 10, 1], 
                      [10, 15, 11, 6, 14, 3, 10, 11, 19, 16, 20, 16, 1, 19, 16, 17, 15, 18, 14, 3, 20, 19, 10, 10, 20, 10, 3, 6, 11, 9], 
                      [6, 18, 8, 11, 15, 20, 13, 11, 12, 4, 3, 5, 10, 1, 2, 13, 5, 19, 8, 5, 4, 15, 15, 18, 8, 15, 0, 9, 2, 14]])


    # list of compromised by day (algal, coral, species)
    app.setCompromised([[14, 8, 18, 16, 20, 13, 8, 9, 5, 8, 8, 19, 9, 1, 18, 16, 7, 10, 19, 15, 13, 8, 10, 3, 2, 6, 20, 12, 1, 8], 
                        [20, 10, 10, 2, 20, 19, 17, 0, 17, 7, 14, 8, 17, 1, 19, 15, 19, 5, 0, 18, 17, 20, 17, 2, 5, 9, 19, 13, 5, 4], 
                        [10, 2, 13, 1, 4, 3, 6, 12, 9, 11, 17, 13, 1, 10, 13, 13, 6, 7, 11, 7, 13, 20, 9, 7, 18, 18, 6, 3, 2, 17]])

    # show app
    app.show()

main()

