import bp_module as bp_md

def check_N(point):
    isNatural_num = True
    if(point<0):
        isNatural_num = False
        print("自然数を入力して下さい")
    return isNatural_num

def check_enough_point(point):
    isEnough_point = True
    if(BP.get_rest_point()<point):
        isEnough_point = False
        print("ポイントが足りません")
    return isEnough_point

def check_range_07(point):
    isRange = True
    if(point<0 or point>7):
        isRange = False
        print("範囲内の数値を入力してください")
    return isRange


total_point = 100
bp_list = ("SW","HP","MP","ATK","DEF")
partition_point = [0,0,0,0,0]

BP = bp_md.bp(total_point)
ex_txt = ("BPはプレイヤーのステータスを強化できるポイントです。\n振り分けた値がプレイヤーのステータスになります。\nBPで強化できるステータスはHP、MP、攻撃力(ATK)、防御力(DEF)、行動の重み(SW)の5つが存在します。\nHP、MP、ATK、DEFは総量内であれば好きに変更可能です。ただし、SWは7から0の範囲で強化可能です。\n")

while(True):
    print("BPを振り分けましょう。振り分けた値がプレイヤーのステータスになります。\nSW、HP、MP、ATK、DEFの5つにBPを振り分けてください。\n今回のBPは"+str(BP.get_total_point())+"です。\n各項目は半角数字で入力してください")

    while(True):
        print("SWにBPを振り分けてください。(残り:"+str(BP.get_rest_point())+")")
        print("SWの範囲は0～7です")
        tmp = input("数値を入力")
        try:
            point = int(tmp)
        except ValueError:
            print("数値以外が入力されました。半角数字を入力してください")
            continue
        if(check_N(point)==True and check_range_07(point)==True and check_enough_point(point)==True):
            BP.set_rest_point(BP.get_rest_point() - point)
            partition_point[0] = point
            break
    
    while(True):
        print("HPにBPを振り分けてください。(残り:"+str(BP.get_rest_point())+")")
        tmp = input("数値を入力")
        try:
            point = int(tmp)
        except ValueError:
            print("数値以外が入力されました。半角数字を入力してください")
            continue
        if(check_N(point)==True and check_enough_point(point)==True):
            BP.set_rest_point(BP.get_rest_point() - point)
            partition_point[1] = point
            break

    while(True):
        print("MPにBPを振り分けてください。(残り:"+str(BP.get_rest_point())+")")
        tmp = input("数値を入力")
        try:
            point = int(tmp)
        except ValueError:
            print("数値以外が入力されました。半角数字を入力してください")
            continue
        if(check_N(point)==True and check_enough_point(point)==True):
            BP.set_rest_point(BP.get_rest_point() - point)
            partition_point[2] = point
            break

    while(True):
        print("ATKにBPを振り分けてください。(残り:"+str(BP.get_rest_point())+")")
        tmp = input("数値を入力")
        try:
            point = int(tmp)
        except ValueError:
            print("数値以外が入力されました。半角数字を入力してください")
            continue
        if(check_N(point)==True and check_enough_point(point)==True):
            BP.set_rest_point(BP.get_rest_point() - point)
            partition_point[3] = point
            break

    while(True):
        print("DEFにBPを振り分けてください。(残り:"+str(BP.get_rest_point())+")")
        tmp = input("数値を入力")
        try:
            point = int(tmp)
        except ValueError:
            print("数値以外が入力されました。半角数字を入力してください")
            continue
        if(check_N(point)==True and check_enough_point(point)==True):
            BP.set_rest_point(BP.get_rest_point() - point)
            partition_point[4] = point
            break

    print("=================================")
    for i in range(len(partition_point)):
        print(bp_list[i]+":"+str(partition_point[i]))
    print("=================================")
    print("ステータスはこれでいいですか？(Y or AnyKey)")
    check_status = input()
    if(check_status == "Y"):
        break
    else:
        BP.reset_point()
        pass
