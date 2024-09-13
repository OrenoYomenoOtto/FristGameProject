class hp():
    def __init__(self, max_hp:int, current_hp:int):
        self.max_hp = max_hp
        self.current_hp = current_hp

    def heal_hp(self, heal_amount:int):
        if self.current_hp + heal_amount >= self.max_hp:
            self.current_hp = self.max_hp
        else:
            self.current_hp += heal_amount

    def receive_damage(self, damage_amount:int):
        self.current_hp -= damage_amount
        if self.current_hp < 0:
            self.current_hp = 0

    def check_can_heal(self):
        isMax = False
        if self.current_hp == self.max_hp:
            isMax = True
        return isMax

    def check_zero_hp(self):
        isZero = False
        if self.current_hp == 0:
            isZero = True
        return isZero