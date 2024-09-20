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
        self.__hp.heal(heal)

    #MP回復メソッド
    def recovery_mp(self, recovery:int):
        self.__mp.recovery(recovery)
    
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
