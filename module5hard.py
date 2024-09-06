import time

class User:

    def __init__(self, nicname, password, age):
        self.nicname = nicname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nicname

    def __eq__(self, other):
        return other.nicname == self.nicname

    def get_info(self):
        return self.nicname, self.password


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    # Дописываю два класса для лучшего отражения имен
    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

class UrTube:
    def __init__(self):
        self.users = []   # Список объектов User
        self.videos = []  # Список объектов Video
        self.current_user = None  # Текущий пользователь, User

    def log_in(self, nicname, password):
        for user in self.users:
            if (nicname, hash(password)) == user.get_info():
                self.current_user = user
                return user

    def register(self, nicname, password, age):
        new_user = User(nicname, password, age)
          # Проверка имени.
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f' Пользователь  {nicname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video.title not in self.videos:
                self.videos.append(video)

    def get_videos(self, seach_video):
        my_seach_list = []
        for video in self.videos:
            if seach_video.lower() in str(video).lower():
                my_seach_list.append(video)
        return my_seach_list

    def watch_video(self, title):
        if self.current_user is None:
            print(' Войдите в аккаунт, чтобы смотреть видео ')
            return
            # Проверка авторизации пользователя
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age >=18:
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now, end=' ')
                        time.sleep(1)
                    video.time_now = 0
                    print('Конец видео')
                else:
                    print(' Вам нет 18 лет, пожалуйста покиньте страницу ')
                break

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

