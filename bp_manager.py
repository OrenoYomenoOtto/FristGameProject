import bp_module as bp_md

total_point = 100

hp_p =  0
mp_p = 0
atk_p = 0
def_p = 0
sw_p = 0
Answer = "n"


BP = bp_md.bp(total_point)
ex_txt = ("BPはプレイヤーのステータスを強化できるポイントです。\nBPで強化できるステータスはHP、MP、攻撃力(ATK)、防御力(DEF)、行動の重み(SW)の5つが存在します。\n"
          "HP、MP、ATK、DEFは総量内であれば好きに変更可能です。ただし、SWは7から0の範囲で強化可能です。\n")


print("BPを振り分けましょう。\n振り分けた値がプレイヤーのステータスになります。\nHP、MP、ATK、DEF、SWの5つにBPを振り分けてください。")
print("今回のBPは"+str(total_point)+"です。\n")
print("HPに振り分けてください。(残りBP："+str(total_point)+")")
hp_p = input("数値を入力：")
print("MPに振り分けてください。(残りBP："+str(total_point)+")")
mp_p = input("数値を入力：")
print("ATKに振り分けてください。(残りBP："+str(total_point)+")")
atk_p = input("数値を入力：")
print("DEFに振り分けてください。(残りBP："+str(total_point)+")")
def_p = input("数値を入力：")
print("SWに振り分けてください。範囲は0～7です。(残りBP："+str(total_point)+")")
sw_p = input("数値を入力：")

print("=================================")
print("HP："+str(hp_p)+"　MP："+str(mp_p)+"　ATK："+str(atk_p)+"　DEF："+str(def_p)+"　SW："+str(sw_p))
if(BP>0):
    Answer = input("BPが残っていますがよろしいですか？(Y/n)")
    if(Answer == n):

Answer=input("BPの配分はこれでよろしいですか？(Y/n)")
