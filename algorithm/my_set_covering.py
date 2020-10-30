stations={}
stations["kone"]=set(["id","nv","ut"])
stations["ktwo"]=set(["wa","id","mt"])
stations["kthree"]=set(["or","nv","ca"])
stations["kfour"]=set(["nv","ut"])
stations["kfive"]=set(["ca","az"])




def least_stations():
    # the least needed station set
    least_station_needed = set()
    states = set(["id", "nv", "ut", "wa", "id", "mt", "or", "ca", "az"])
    while states:
        # station which can cover the most states in states set
        max_cover_station=None
        # the number of the most states
        max_cover_states={}

        # go through all stations to find the station which can cover the most states
        for station in stations.keys():
            # the intersection between current station and all needed states
            cover_states=stations[station]&states
            if len(cover_states)>len(max_cover_states):
                max_cover_station=station
                max_cover_states=cover_states
        states-=max_cover_states
        # add the qualified station to the least_station_needed set
        least_station_needed.add(max_cover_station)
    return least_station_needed

print(least_stations())
