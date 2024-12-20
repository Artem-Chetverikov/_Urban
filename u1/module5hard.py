from time import sleep


class User:

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:

    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        for user_i in self.users:
            if nickname == user_i.nickname and user_i.password == hash(password):
                self.current_user = user_i
                break

    def register(self, nickname: str, password: str, age: int):
        for user_i in self.users:
            if nickname == user_i.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        self.users.append(User(nickname, hash(password), age))
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            video_there = False
            for item in self.videos:
                if video.title == item.title:
                    video_there = True
            if not video_there:
                self.videos.append(video)

    def get_videos(self, search: str):
        list_video = []
        for video in self.videos:
            if search.lower() in video.title.lower():
                list_video.append(video.title)
        return list_video

    def watch_video(self, search: str):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == search:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for i in range(1, video.duration + 1):
                    video.time_now = i
                    print(video.time_now, end=' ')
                    # to-do sleep(1)
                print('Конец видео')
                video.time_now = 0
                return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
