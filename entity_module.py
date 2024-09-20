import hp_module
import mp_module

#エンティティクラス
class entity():
    #初期化
    def __init__(self,
                 hit_point:hp_module.hp,
                 magic_point:mp_module.mp,
                 attack:int,
                 defense:int,
                 act_weight:int,
                 ) -> None:
        self.__hp = hit_point
        self.__attack = attack
        self.__defense = defense
        self.__actweight = act_weight
        self.__mp = magic_point

    #ダメージを受けるメソッド
    def update_hp_damage(self,damage:int):
        self.__hp.receive_damage(damage)

    #ダメージの大きさを計算し、返すメソッド
    def calculate_damage(self, attack:int):
        return attack // self.__defense
    
    #HP回復メソッド
    def heal_hp(self,heal:int):
        self.__hp.heal_hp(heal)

    #MP回復メソッド
    def recovery_mp(self, recovery:int):
        self.__mp.recovery_mp(recovery)
    
    #生死判定メソッド
    def check_is_dead(self):
        return self.__hp.check_zero_hp()
    
    #hp参照メソッド
    def get_hp(self):
        return self.__hp
    
#playerクラス
class player(entity):
    #初期化
    def __init__(self,
        hit_point,
        magic_point,
        attack,
        defense,
        act_weight,
        name,
        remaining,
        ):
        super().__init__(
            hit_point,
            magic_point,
            attack,
            defense,
            act_weight,
            )  #親クラスのコンストラクタを呼び出し
        self.__name = name
        self.__remaining = remaining
    
    #空腹値を変更するメソッド
    def decrease_hunger():
        pass

    #name参照メソッド
    def get_name(self):
        return self.__name

    #remaining参照メソッド
    def get_remaining(self):
        return self.__remaining
    
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
        update_value = self.__actweight - 10*bp
        #行動力が3以下にならないときのみ更新する
        if update_value >= 3:
            self.__actweight = update_value
            return True
        else:
            return False