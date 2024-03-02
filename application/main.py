# Custom display class
from display import Display



# ---------------- TEST FUNCTION ERASE ----------------
import csv  # erase me
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



# test func only shows 4 days
def test():
    app = Display()
    
    # Set data (x,y) grid of land (1 land, 0 water)
    data = simpleGetArray(basepath + world_path + "1.csv")
    app.UpdateCanvas(data)

    # Set preserved button changed handler
    def handler(preserving):
        print("handled! type " + preserving)
    
    app.set_presreve_changed_handler(handler)
    
    # list of rig1 list and rig2 list for every day
    app.setRigCoords([[(1,1),(2,2),(3,3),(4,4)],
                      [(50,1),(50,2),(50,3),(50,4)]])
    
    # tuple list of collected by day (helium, metal, oil)
    app.setCollected([[1,2,3,4],
                      [11,12,13,14],
                      [21,22,23,24]])

    # list of compromised by day (algal, coral, species)
    app.setCompromised([[31,32,33,34],
                        [41,42,43,44],
                        [51,52,53,54]])

    # show app
    app.show()

test()

