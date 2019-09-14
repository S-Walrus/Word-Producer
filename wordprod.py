from tqdm import tqdm
import pickle
from random import choice

class WordProducer:
   
    def __init__(self, k):
        self.d = {}
        if type(k) == int:
            self.k = [True for i in range(k)]
            self.l = k
        elif type(k) == list:
            self.k = k
            self.l = len(k)
        else:
            raise TypeError('You need to pass int or array of bool instead of {}'.format(str(type(k))))
    
    def fit(self, word_list):
        prefix = '_' * self.l
        for word in tqdm(word_list):
            word = prefix + word + '.'
            for i in range(len(word) - self.l):
                seq = ''.join(word[i + j] for j in range(self.l) if self.k[j])
                self.d[seq] = self.d.get(seq, []) + [word[i+self.l]]
    
    def generate(self, n=1):
        for r in range(n):
            word = '_' * self.l
            while word[-1] not in '.,':
                seq = ''.join([word[-self.l + j] for j in range(self.l) if self.k[j]])
                word = word + choice(self.d.get(seq, [',']))
            print(word[self.l:-1])
    
    def save(self, name):
        with open(name, 'wb') as f:
            pickle.dump(self.d, f)
    
    def load(self, name):
        with open(name, 'rb') as f:
            self.d = pickle.load(f)
