class Numerology:
    def __init__(self):
        self.numbers = {}
        self.names = {}
        self.birthdate = None
        self.date = None
        self.month = 0
        self.year = 0
        self.name_ = ''
        self.lucky_numbers_ = []
        self.summary_info = {}

    def set_birthdate(self, birthdate):
        self.birthdate  = birthdate
        day, month, year = birthdate.split('-')
        self.date, self.month, self.year = int(day), int(month), int(year)

    def set_name(self, name):
        self.name_ = name
        
    def get_bhagyanak(self):
        total = sum([self.date, self.month, self.year])
        while total > 9:
            total = sum(map(int, str(total)))
        return total

    def get_mulank(self):
        mulank = sum(map(int, str(self.date)))
        while mulank > 9:
            mulank = sum(map(int, str(mulank)))
        return mulank
    
    def get_namank(self, name):
        self.name_ = name.upper()  
        self.names = {
            'A': 1, 'I': 1, 'J': 1, 'Q': 1, 'Y': 1,
            'B': 2, 'K': 2, 'R': 2,
            'C': 3, 'G': 3, 'L': 3, 'S': 3,
            'D': 4, 'M': 4, 'T': 4,
            'E': 5, 'H': 5, 'N': 5, 'X': 5,
            'U': 6, 'V': 6, 'W': 6,
            'O': 7, 'Z': 7,
            'F': 8, 'P': 8
        }
        namank = 0
        for char in self.name_:
            for key in self.names:
                if char in key:
                    print(f"Character: {char}, Key: {key}, Value: {self.names[key]}")
                    namank += self.names[key]
                    break 

        while namank > 9:
            namank = sum(map(int, str(namank)))
        return namank
    
    
    def lucky_numbers(self):
        namank_value  = self.get_namank(self.name_)
        mulank_value = self.get_mulank()
        bhagyanak_value = self.get_bhagyanak()
        self.numbers = {
            1 : [[1,2,3,5,6,9] , [8] , [4,7]],
            2 : [[1,2,3,5],[8,4,6],[6,7]],
            3 : [[1,2,3,5,7],[6],[4,8,9,7]],
            4 : [[1,7,5,6],[4,8,9,2],[3]],
            5 : [[1,2,3,5,6],[],[8,7,4,9]],
            6 : [[1,7,5,6] , [3] , [8,9,2,4]],
            7 : [[1,3,5,4,6],[],[2,4,8,9]],
            8 : [[5,3,6,7],[1,4,8,2],[9]],
            9: [[1,5,3], [4,2], [9,7,6,8]]
        }

        for ank, nums in self.numbers.items():
            if ank == namank_value or bhagyanak_value or mulank_value:
                self.lucky_numbers_ += nums[0]
                for num in nums[1]:
                    if num in self.lucky_numbers_:
                        self.lucky_numbers_.remove(num)
                for num in nums[2]:
                    if num in self.lucky_numbers_:
                        self.lucky_numbers_.remove(num)

        return list(set(self.lucky_numbers_))

    def print_summary(self):
        self.summary_info = {
            'name': self.name_,
            'date': self.birthdate,
            'mulank': self.get_mulank(),
            'namank': self.get_namank(self.name_),
            'bhagyanak': self.get_bhagyanak(),
            'lucky_numbers': self.lucky_numbers()
        }
        if self.lucky_numbers_:
            self.summary_info['vibration_cor'] = self.lucky_numbers_[0]
        else:
            self.summary_info['vibration_cor'] = None
            
        return self.summary_info



    
   



            





        






        