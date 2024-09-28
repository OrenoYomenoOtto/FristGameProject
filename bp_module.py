class bp():
    def __init__(self,total_point:int):
        self.__total_point = total_point
        self.__rest_point = total_point

    def get_total_point(self):
        return self.__total_point
    
    def get_rest_point(self):
        return self.__rest_point
    
    def set_rest_point(self,num):
        self.__rest_point = num

    def reset_point(self):
        self.__rest_point = self.__total_point

    def define_atk(self):
        pass

    def define_def(self):
        pass

    def define_hp(self):
        pass

    def define_mp(self):
        pass

    def define_sw(self):
        pass
