from abc import ABCMeta
from abc import abstractmethod

class Room(metaclass=ABCMeta):
    # コンストラクタ
    # id: 部屋のID
    # name: 部屋の名前
    # is_can_pass: 通行可能かどうか
    # params: 部屋固有のパラメータ。辞書型で渡す
    def __init__(self, id: int, name: str, is_can_pass: bool):
        self.id = id
        self.name = name
        self.is_can_pass = is_can_pass
        self.is_passed = False
    
    # 部屋に入る処理
    @abstractmethod
    def enter_room(self):
        pass
