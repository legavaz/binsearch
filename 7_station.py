# пересечения множеств

import os
os.system('CLS')

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}

stations["Kone"]     =   set(['id','nv','ut'])
stations["Ktwo"]     =   set(['wa','id','mt'])
stations["Kthree"]   =   set(['or','nv','ca'])
stations["Kfour"]    =   set(['nv','ut'])
stations["Kfive"]    =   set(['ca','az'])

final_station       =   set()


while states_needed:
    best_station        =   None
    states_covered      =   set()
    for station, states_for_station in stations.items():
        # print(station,states_for_station)        
        covered     =   states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station    =   station
            states_covered  =   covered
    
    final_station.add(best_station)
    states_needed-=states_covered
print(final_station)




