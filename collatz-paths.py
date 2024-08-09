import math
class CollatzStruct:
    def __init__(self, max_iter = 0):
        self.init_num = 4
        self.max_iter = max_iter
        self.iter = 0
        self.layers = [[self.init_num]] #could be one, but that would not be useful since first 3 lists would just be [1], [2], [4]
        self.len_layers = [1]
        self.working_layer = []
        self.raw_list = [self.init_num]
        self.len_raw_list = 0
        self._in_pigeonholes = None
        self.pigeonholes = self.make_pigeonholes()
        self.evaluate_upto_max_iter()


    #could use pathfinding algorithm e.g. djikstra's to find if an element already exists by linking numbers depthwise in a graph, but not now.
    #instead, i'm going to box numbers in ranges, so any number in 0-99 range will be place in list at 0th index, 100-199 at 1st etc...
    def make_pigeonholes(self, box_size = 100):
        self.box_size = box_size
        max_num = 2**(self.max_iter+math.log2(self.init_num))
        last_box_index = math.ceil(max_num/box_size)
        pigeonholes = [[] for index in range(last_box_index)]
        pigeonholes = list(last_box_index)
        print('Finished constructing pigeonholes.')
        return pigeonholes

    def reset_working_layer(self):
        self.working_layer = []

    def in_pigeonholes(self, number):
        if number in self.pigeonholes[math.floor(number/100)]:
            self._in_pigeonholes = True
            return True
        else:
            self._in_pigeonholes = False
            return False
        
    def count_raw_list(self):
        self.len_raw_list = len(self.raw_list)

    def count_last_layer(self):
        len_last_layer = len(self.layers[-1])
        self.len_layers.append(len_last_layer)
    
    def inv_collatz(self, number):    
        if not self.in_pigeonholes(2*number):
            self.working_layer.append(2*number)
            self.raw_list.append(2*number)
            self.pigeonholes[math.floor(2*number/self.box_size)].append(2*number) #allocates new number to pigeonhole by the hundreds.

        if ((number-1)%3 == 0) and (not self.in_pigeonholes((number-1)//3)) and (number-1 != 0):
            self.working_layer.append((number-1)//3)
            self.raw_list.append((number-1)//3)
            self.pigeonholes[math.floor((number-1)/(3*self.box_size))].append((number-1)//3)

    def evaluate_working_layer(self):
        for number in self.layers[-1]:
            self.inv_collatz(number)
        self.layers.append(self.working_layer)

    def do_updates(self):
        self.count_raw_list()
        self.count_last_layer()
        self.reset_working_layer()

    def evaluate_upto_max_iter(self):
        while self.iter < self.max_iter:
            self.evaluate_working_layer()
            self.do_updates()
            self.iter = self.iter+1

    def get_len_layers(self):
        return self.len_layers
    def get_len_raw_list(self):
        return self.len_raw_list
    def get_layers(self):
        return self.layers
    def get_raw_list(self):
        return self.raw_list
    
CzS_obj = CollatzStruct(30)
#print(CzS_obj.get_layers())
#print(CzS_obj.get_raw_list())
#print(CzS_obj.get_len_raw_list())
print(CzS_obj.pigeonholes)



#goal is to deprecate current list implementation of pigeonholes instantiated in the class CollatzStruct.
class PigeonHole:
    def __init__(self, size):

        self.keys = [1, 5, 3, 2, 0, 4]
        self.links = [(0,4)(1,0)(2,3)(3,2)(4,5)(5,1)] #these tell you how to find the keys. 1st val is key, 2nd val is index.
        self.coops = [[]]
