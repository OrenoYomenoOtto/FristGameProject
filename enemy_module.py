import entity_module
import random

#playerクラス
class player(entity_module.entity):
    #初期化
    def __init__(self,drop_item, drop_money, item_drop_probabily
        ):
        super().__init__(
            )  #親クラスのコンストラクタを呼び出し
        self.__drop_item = drop_item
        self.__drop_money = drop_money
        self.__item_drop_probabily = item_drop_probabily

    #装備品(プレイヤーのみ)・状態異常(追加予定)を加味して真の攻撃力を返すメソッド
    #現時点で未実装のため、素の攻撃力を返す
    def get_true_defense(self):
        return self.__attack

    #装備品(プレイヤーのみ)・状態異常(追加予定)を加味して真の防御力を返すメソッド
    #現時点で未実装のため、素の防御力を返す
    def get_true_defense(self):
        return self.__defense
    
    #アイテムを落とすかを返すメソッド
    def does_drop_money(self):
        if random.random() < self.__item_drop_probabily:
            return True
        else:
            return False
        
    #アイテムIDを返す
    def get_drop_itemid(self):
        return self.__drop_item
    
    #お金を返す
    def get_drop_money(self):
        return self.__drop_money