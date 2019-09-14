from wordprod import WordProducer

with open('zdf-win.txt', 'r', encoding='windows-1251') as f:
    wp = WordProducer(3)
    wp.fit(f)
    wp.save('out.dict')
    wp.generate(100)
