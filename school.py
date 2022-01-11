class School:
    
    def __init__(self, name, roster ={}):
        self.name = name
        self.roster = roster
    
    def add_student(self, name, grade):
        if str(grade) not in self.roster:
            self.roster[str(grade)] = list()
            self.roster[str(grade)].append(name)
        else:
            self.roster[str(grade)].append(name)
    
    def grade(self, grade):
        return self.roster[str(grade)]
    
    def sort_roster(self):
        for key, values in self.roster.items():
            values_sorted = sorted(values, reverse= False)
            self.roster[key] = values_sorted




            

