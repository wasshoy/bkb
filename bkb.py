import random
import sys

from cabocha.analyzer import CaboChaAnalyzer

analyzer = CaboChaAnalyzer()
B = {'ば', 'び', 'ぶ', 'べ', 'ぼ', 'バ', 'ビ', 'ブ', 'ベ', 'ボ'}
K = {'か', 'き', 'く', 'け', 'こ', 'カ', 'キ', 'ク', 'ケ', 'コ'}

class BKB:
    def __init__(self, path):
        self.path = path
        with open(path) as f:
            text = f.read()
        self.text = text
    
    def extract_bkb(self): 
        bs = []   
        ks = []
        tree = analyzer.parse(self.text)
        for chunk in tree:
            word = chunk.surface[0] if chunk.surface[0] != ' ' else chunk.surface[1]
            if word in B: bs.append(chunk.surface)
            if word in K: ks.append(chunk.surface)
        return [bs, ks]
    
    def hiiya_sususu(self, b, k):
        if len(b) == 0 or len(k) == 0:
            print('\nヒイァ...\n')
            return None
        print(f'\n{random.choice(b)}', end=' '*4)
        print(f'{random.choice(k)}', end=' '*4)
        print(f'{random.choice(b)}', end='\n\n')
        print('B  K  B!', end=' '*4)
        print('ヒ  ィ  ー  ァ  ！', end=' '*4)
        print('ス ス ス。\n')
        
    
if __name__ == '__main__':
    bkb = BKB(sys.argv[1])
    b, k = bkb.extract_bkb()
    bkb.hiiya_sususu(b, k)