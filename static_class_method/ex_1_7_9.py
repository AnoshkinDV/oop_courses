class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f'воспроизведение видео {self.name}')


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_index):
        video = cls.videos[video_index]
        video.play()

v1 = Video()
v2 = Video()
v1.create('Python')
v2.create('Поколение Python')
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)
