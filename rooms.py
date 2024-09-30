from room import Room

class NothingRoom(Room):
    def __init__(self):
        super().__init__(0, "何もない部屋", True)
    
    def enter_room(self):
        print("何もない部屋に入りました。")
        self.is_passed = True


class MonsterRoom(Room):
    def __init__(self, monster_id: str):
        super().__init__(1, "モンスター部屋", False)
        self.monster_id = monster_id
    
    def enter_room(self):
        print("モンスター部屋に入りました: id = " + self.monster_id)
        self.is_passed = True

