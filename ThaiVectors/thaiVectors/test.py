from pprint import pprint

import gensim, logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = gensim.models.Word2Vec.load('vectors_0.0.1.model')

print(model)

pprint(model.most_similar(['ที่'], topn=10))

questions = ['มะละกอ ทุเรียน เห็ด องุ่น',
             'โต๊ะ แกง เก้าอี้ เตียง',
             'โทรศัพท์ โซฟา มือถือ คอมพิวเตอร์',
             'ปู่ ย่า น้อง ยาย']

for question in questions:
    print(question, '>', model.doesnt_match(question.split()))


sentence = 'ผม หิว ข้าว แล้ว'.split()
print(sentence)
for word in sentence:
    print('---------------------------------------')
    print('ใคร', word, model.similarity('ใคร', word))
    print('อะไร', word, model.similarity('อะไร', word))
    print('สถานที่', word, model.similarity('สถานที่', word))
    print('ไหน', word, model.similarity('ไหน', word))
    print('เวลา', word, model.similarity('เวลา', word))
    print('สิ่งของ', word, model.similarity('สิ่งของ', word))

sentence = 'ห้องน้ำ อยู่ ไหน'.split()
print(sentence)
for word in sentence:
    print('---------------------------------------')
    print('ใคร', word, model.similarity('ใคร', word))
    print('อะไร', word, model.similarity('อะไร', word))
    print('สถานที่', word, model.similarity('สถานที่', word))
    print('ไหน', word, model.similarity('ไหน', word))
    print('เวลา', word, model.similarity('เวลา', word))
    print('สิ่งของ', word, model.similarity('สิ่งของ', word))

sentence = 'วัน นี้ กิน ข้าว ที่ บ้าน'.split()
print(sentence)
for word in sentence:
    print('---------------------------------------')
    print('ใคร', word, model.similarity('ใคร', word))
    print('อะไร', word, model.similarity('อะไร', word))
    print('กริยา', word, model.similarity('กริยา', word))
    print('สถานที่', word, model.similarity('สถานที่', word))
    print('ไหน', word, model.similarity('ไหน', word))
    print('เวลา', word, model.similarity('เวลา', word))
    print('สิ่งของ', word, model.similarity('สิ่งของ', word))
x = model['คอม']
y = x.tolist()
print(y)