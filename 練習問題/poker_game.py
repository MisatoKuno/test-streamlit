import random
import itertools

# class Terminal():
#     #osごとのクリア処理

class Card():
    def __init__(self):
        #全カード定義
        self.cards=[{"marks":mark,"nums":num} for mark,num in itertools.product(range(1,4+1),range(1,13+1))]
        #カードのシャッフル
        random.shuffle(self.cards)
        #最初のカードを5枚出す
        self.hand=[]
        self.take(5)
        #手札を昇順に並べ替える
        self.sort()
        #選択手札のクリア
        self.select_clear()
    
    def select_clear(self):
        self.selects=set()
    
    def take(self,n):
        #山札からカードをn枚とる
        self.hand+=self.cards[:n]
        #残りのカードを定義
        self.cards=self.cards[n:]
    
    def sort(self):
        #数字が小さい順に並べ替え
        for i in range(4):
            for j in range(i+1,5):
                if self.hand[i]["nums"]>self.hand[j]["nums"]:
                    tmp=self.hand[i]
                    self.hand[i]=self.hand[j]
                    self.hand[j]=tmp
    
    #カードの選択
    def select(self):
        
    
    #選択したカードの削除
    
    #カードの表示
        
    
# class Judge():
#     #カードの数が連続してるか調べる
#     #カードのマークがいくつ揃っているか調べる
#     #カードの数字がいくつ揃っているか調べる    
#         #ロイヤルストレートフラッシュ（同じマークで10～A）10000
#         #ストレートフラッシュ（同じマークで連続の数字）5000
#         #フォーカード2500
#         #フルハウス（スリーカード＋ペア）2000
#         #フラッシュ（全部同じマーク）1500
#         #ストレート（連続の数字）1200
#         #スリーカード1000
#         #ツーペア800
#         #ワンペア100
    
# class main_game():
#     def __init__(self):
#         #手札５枚出す
#         #ユーザ入力欄表示
#         #ターン表示
#     def main(self):
#         #ゲームの繰り返し
#             #捨てるカード選択（*で示す）
#             #カード入れ替え
#         #カード確定
#         #役判定・得点表示
#         #ゲーム終了
    