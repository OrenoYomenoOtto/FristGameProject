from room import Room
from vector2 import Vector2

class Map:
    # コンストラクタ
    # rooms: マップの部屋の2次元リスト
    def __init__(self, rooms: list[list[Room]]):
        self.map = rooms

    
    # 位置を指定して部屋を取得
    # position: 部屋の位置
    # return: その位置の部屋
    def get_room(self, position: Vector2) -> Room:
        return self.map[position.y][position.x]

    
    # マップサイズを取得
    # return: マップのサイズ
    def get_map_size(self) -> Vector2:
        return Vector2(len(self.map[0]), len(self.map))