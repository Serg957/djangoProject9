
def check_for_email(s):
    chars = (".com", ".ru", ".net")

    s.lower()
    if s.count('@') == 1 and s[0] != '@' and s.endswith(chars):
        return True
    else:
        return False
def sand_email(message, recipient, *, sender="univercity.help@gmail.com"):


    if not check_for_email(recipient) or not check_for_email(sender):
        print("Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>.")

    elif (recipient.lower() == sender.lower()):

        print('Нельзя отправить письмо самому себе!')

    elif  (sender.lower() == "univercity.help@gmail.com"):

         print('Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
         print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено'
        ' с адреса {sender} на адрес {recipient}')

sand_email('Это сообщение для проверки связи',"vasiok1337@gmail.com")

sand_email('Вы видите это сообщение как лучший студент курса',
           "urban.fan@mail.ru", sender="urban.info@gmail.com")
sand_email('Пожалуйста исправьте задание','urban.student@mail.ru',
           sender='urban.student@mail.uk')
sand_email('Напоминаю самому себе овебинаре','urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')





