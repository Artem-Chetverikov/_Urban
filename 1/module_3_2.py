def send_email(message: str, recipient: str, sender="university.help@gmail.com"):

    suffix_valid = [".com", ".ru", ".net"]
    bad_email = False
    suffix_rec = '.' + recipient.split('.')[-1]
    suffix_sen = '.' + sender.split('.')[-1]

    if not (suffix_rec in suffix_valid) or not (suffix_sen in suffix_valid):
        bad_email = True

    if not ('@' in recipient) or not ('@' in sender):
        bad_email = True

    if bad_email:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return

    if sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
        return

    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        return
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
