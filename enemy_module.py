import entity_module

#playerクラス
class player(entity_module.entity):
    #初期化
    def __init__(self,
        ):
        super().__init__(
            )  #親クラスのコンストラクタを呼び出し
        
    #装備品(プレイヤーのみ)・状態異常(追加予定)を加味して真の攻撃力を返すメソッド
    #現時点で未実装のため、素の攻撃力を返す
    def get_true_defense(self):
        return self.__attack

    #装備品(プレイヤーのみ)・状態異常(追加予定)を加味して真の防御力を返すメソッド
    #現時点で未実装のため、素の防御力を返す
    def get_true_defense(self):
        return self.__defense