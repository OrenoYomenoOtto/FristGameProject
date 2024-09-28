import entity_module

#初期パラメータ用の定数
PLAYER_INITIAL_HP = 10
PLAYER_INITIAL_MP = 10
PLAYER_INITIAL_ATTACK = 10
PLAYER_INITIAL_DEFENSE = 10
PLAYER_INITIAL_ACTWEIGHT = 10

#playerクラス
class Player(entity_module.Entity):
    #初期化
    def __init__(self,
        name,
        remaining,
        ):
        super().__init__(
            PLAYER_INITIAL_HP,
            PLAYER_INITIAL_MP,
            PLAYER_INITIAL_ATTACK,
            PLAYER_INITIAL_DEFENSE,
            PLAYER_INITIAL_ACTWEIGHT,
            )  #親クラスのコンストラクタを呼び出し
        self.__name = name
        self.__remaining = remaining
    
    #空腹値を変更するメソッド
    def decrease_hunger():
        pass

    #名前参照メソッド
    def get_name(self):
        return self.__name

    #残機参照メソッド(OK)
    def get_remaining(self):
        return self.__remaining
    
    #残機があるかを返すメソッド(OK)
    def has_remaining(self):
        if self.__remaining >= 1:
            return True
        else:
            return False
        
    #残機を減らすメソッド(OK)
    def decrease_remaining(self):
        if self.has_remaining():
            self.__remaining -=1
            return True
        else:
            return False

    #装備品(プレイヤーのみ)・状態異常(追加予定)を加味して真の攻撃力を返すメソッド
    #現時点で未実装のため、素の攻撃力を返す
    def get_true_attack(self):
        return self.__attack

    #装備品(プレイヤーのみ)・状態異常(追加予定)を加味して真の防御力を返すメソッド
    #現時点で未実装のため、素の防御力を返す
    def get_true_defense(self):
        return self.__defense

    #攻撃力更新メソッド
    def update_attack_bybp(self, bp:int):
        self.__attack += bp

    #防御力更新メソッド
    def update_defense_bybp(self, bp:int):
        self.__defense += bp 

    #hp更新メソッド
    def update_hp_bybp(self, bp:int):
        self.__hp.change_by_bp(bp)

    #mp更新メソッド
    def update_defense_bybp(self, bp:int):
        self.__mp.change_by_bp(bp)

    #行動力更新メソッド
    def update_act_weight(self, bp:int):
        update_value = self.__actweight - bp
        #行動力が3以下にならないときのみ更新する
        if update_value >= 3:
            self.__actweight = update_value
            return True
        else:
            return False