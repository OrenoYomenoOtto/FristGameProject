class item():
    def __init__(self, item_name, item_id, item_type):
        self.item_name = item_name
        self.item_id = item_id
        self.item_type = item_type
    
    def use_item(self):
        """アイテムの使用を実行し、使用できればTrueを返す"""
        
        pass

    def use_for_map(self, MAP, Vector2):
        """マップに対するアイテムの効果を発動し、成功すればTrueを返す"""
        pass

    def use_for_player(self, Player):
        """マップに対するアイテムの効果を発動し、成功すればTrueを返す"""
        pass