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
    app.setRigCoords([[[51, 48], [80, 81], [76, 89], [30, 44], [89, 22], [57, 94], [33, 27], [20, 26], [48, 2], [32, 23], [11, 32], [22, 35], [71, 2], [30, 33], [83, 33], [17, 99], [40, 68], [69, 61], [36, 6], [41, 26], [35, 2], [95, 24], [36, 65], [63, 34], [92, 60], [80, 23], [3, 48], [53, 47], [77, 9], [76, 61]], 
                      [[90, 71], [93, 34], [46, 61], [87, 12], [49, 36], [79, 88], [52, 80], [85, 94], [73, 64], [46, 86], [36, 95], [66, 13], [74, 97], [80, 2], [43, 56], [65, 12], [1, 27], [71, 83], [51, 88], [72, 66], [91, 93], [42, 51], [35, 5], [39, 8], [66, 9], [16, 66], [52, 14], [54, 95], [58, 21], [0, 40]]])
    
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

