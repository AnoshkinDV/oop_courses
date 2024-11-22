class MediaPlayer:
    def open(self,file):
        self.filename = file # создаем локальное свойство с нужным нам значением
    def play(self):
        print(f'Воспроизведение {self.filename}')

media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open('filemedia1')
media2.open('filemedia2')
media1.play()
media1.play()
