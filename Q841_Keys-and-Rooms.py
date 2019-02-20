class Solution:
    def canVisitAllRooms(self, rooms: 'List[List[int]]') -> 'bool':
#         check all room keys is avaliable
        n = len(rooms)
        self.rooms = rooms
        self.rooms_dict = {i:0 for i in range(n)}
        self.rooms_dict[0] = 1
        for room in self.rooms:
            for i in room:
                self.rooms_dict[i] = 1 
        for key, val in self.rooms_dict.items():
            if val == 0:
                return False
        self.rooms_dict[0] = 2
        self.visit(self.rooms[0])

        for key, val in self.rooms_dict.items():
            if val == 1:
                return False
        return True
    
    def visit(self, rooms):
        for room in rooms:
            if self.rooms_dict[room] == 1:
                self.rooms_dict[room] = 2
                self.visit(self.rooms[room])
        
        