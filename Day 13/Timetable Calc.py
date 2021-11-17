import numpy
class Timetable:
    def __init__(self):
        with open("input.txt") as f:
            content = f.read()
            content_list = content.split("\n")
            
        self.earliest_time = int(content_list[0])

        self.bus_IDS_unfiltered = content_list[1].split(",")
        self.bus_IDS = (value for value in self.bus_IDS_unfiltered if value !="x")
        self.bus_IDS = list(map(int,self.bus_IDS))

        self.part_1()
        self.part_2()

    def part_1(self):
        """Gets the next arrival time of each bus after the desired time if the value != to the earliest time"""
        self.next_arrival = {}
        for item in self.bus_IDS:
            if self.earliest_time % item == 0:
                print(item)
                break
            arrival_before = (self.earliest_time//item)
            arrival = arrival_before + 1
            arrival_time =(item*arrival)
            self.next_arrival[item] = arrival_time
        lowest =(min(self.next_arrival.items(), key=lambda x: x[1]))
        print("Part 1:",lowest[0]*(lowest[1]-self.earliest_time))

    def part_2(self):
        """Gets a list of departure times such that there is a 1 difference between each bus ID unless it is x"""
        """
        Each bus departs at t + index value unless it is x,
        """
        print(self.bus_IDS_unfiltered)
        indexes = []
        values = []
        for i,val in enumerate(self.bus_IDS_unfiltered):
            if val=="x":
                continue

            indexes.append(i)
            values.append(int(val))

        print(indexes,values)
        start_value = values[0]
        i = 1
        while True:
            index_1 = indexes[0]
            for index,value in zip(indexes,values):
                if (value * i)- index != start_value:
                    break
            i +=1


        


wait_time = Timetable()

