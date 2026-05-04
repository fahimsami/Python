class Employee:
    
    _basesalaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }
     
    def __init__(self, name, level):
        self.name = name
        self.level = level   
        self.salary = Employee._basesalaries[level]
        
    def __str__(self):
        return f"{self.name} : {self.level}"
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if not isinstance(new_salary, (int, float)):
            raise TypeError("Salary must be a number")
        if hasattr(self, '_salary') and new_salary < Employee._basesalaries[self.level]:
            raise ValueError(f"Salary must be higher than minimum salary (${Employee._basesalaries[self.level]})")
        self._salary = new_salary
        print(f"'salary' updated to {self.salary} $")
    
    @property
    def name(self):
        return self._name
    
    @name.setter   
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be of type string")
        self._name = new_name
        print(f"'name' updated to '{new_name}'")
    
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, new_level):
       
        if not isinstance(new_level, str):
            raise TypeError("level must be of type string")
        if new_level not in Employee._basesalaries:
            raise ValueError(f"Invalid value {new_level} for 'level' attribute")
        if hasattr(self, '_level') and self._level ==  new_level:
            raise ValueError(f"'level' is already set to '{new_level}'")
        if hasattr(self, '_level') and Employee._basesalaries[new_level] < Employee._basesalaries[self._level]:
            raise ValueError(f"Cannot change to lower level.")
        self._salary = Employee._basesalaries[new_level]
        self._level = new_level
        print(f"'{self.name}' promoted to '{new_level}' and 'salary' updated to {self.salary} $")
    
    def __repr__(self):
        return f"Employee('{self.name}','{self.level}')"
        
charlie_brown = Employee("Charlie Brown", "trainee")
print(charlie_brown)
print(f"Base salary: {charlie_brown.salary} $")
charlie_brown.name = "Charlie Brown Jr."
charlie_brown.level = "junior"
print(charlie_brown)

