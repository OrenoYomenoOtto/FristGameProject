class mp():
    def __init__(self, max_mp, current_mp):
        self.max_mp = max_mp
        self.current_mp = current_mp
    
    def recovery_mp(self, recovery_amount):
        if self.current_mp + recovery_amount >= self.max_mp:
            self.current_mp = self.max_mp
        else:
            self.current_mp += recovery_amount

    def consume_mp(self, consume_amount):
        self.current_mp -= consume_amount

    def check_can_recovery(self):
        isMax = False
        if self.current_mp == self.max_mp:
            isMax = True
        return isMax

    def check_can_consume(self, consume_amount:int):
        isConsume = True
        if self.current_mp - consume_amount < 0:
            isConsume = False
        return isConsume
