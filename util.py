class Day:
    def __init__(self, day: int, part: int):
        from problems import description
        self.day  = day
        self.part = part
        self.desc = description(day, part)
    
    def load(self, typing=str, sep="\n", data=None) -> list:
        """Loads Data for Problem
        File _must_ be in /inputs/ and named dayXX.txt
        Returns data and makes it available as attribte "data"
        Keyword Arguments:
            data {[list]} -- Load computed data not from file (default: {None})
            typing {[type]} -- Type of data in list (default: {str})
            sep {[str]} -- Separator in input data (default: {"\n"})
        
        Returns:
            list -- Data for Problem
        """
        if data:
            self.data = data
        else:
            with open(f"input/day{self.day:02d}.txt") as f:
                data = f.read().split(sep)
            if "" in data:
                data.remove("")
            self.data = list(map(typing, data))
        self.raw_data = self.data.copy()
        self.raw_apply_data = self.data.copy()
        return self.data
    
    def reset(self,):
        """Reset Data to original
        """
        self.data = self.raw_data.copy()

    def reset_apply(self,):
        """Reset Data to to state after applying a function
        """
        self.reset()
        self.data = self.raw_apply_data.copy()
        
    def apply(self, func) -> list:
        """Apply a function to every element.
        Changes the original data.
        Arguments:
            func {function} -- Function to apply to every element in input
        
        Returns:
            list -- Function applied to every element in input
        """
        self.data = list(map(func, self.data))
        self.raw_apply_data = self.data.copy()
        return self.data


    def answer(self, num=None) -> str:
        if num == None: num = self.result
        else: self.result = num
        return f"The Solution on Day {self.day} for Part {self.part} is: {num}"

if __name__ == "__main__":
    day = Day(9,1)
    day.load(typing=int,sep=',')

    print(day.answer(day.result))
