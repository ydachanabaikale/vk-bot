import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import time
import os

VK_TOKEN = "vk1.a.mymkbo7bw1lA4fwgmz2c7c0BNBTNxfc8Uoz_ah-w490RwkEc8i1YSHkOOo3C_XdtrHgWhIwxfAAv50wTklTzZn2E1oqxu9Bemxu70Vvl91iesXQ3hzeNLH4O37eJuyRANr4kr69n9Jn5K9GbuVeJMAubr7HZy-Cm1ptXnycoXwir-YxDzQ52_OTg3okcpoKwMPKCzrOEFIGmQ3SYEvHFiw"
GROUP_ID = 238085810

def start_bot():
    vk_session = vk_api.VkApi(token=VK_TOKEN, api_version='5.199')
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    print("Бот запущен! Жду сообщений...")

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg = event.text.lower().strip()
            print(f"Получено: {msg}")

            if "удача" in msg:
                vk.messages.send(
                    user_id=event.user_id,
                    message="Здравствуйте!\n\nДля того чтобы стать участником акций и получить шанс выиграть желанный приз, необходимо приобрести постер из списка товаров\n\nИНСТРУКЦИЯ:\n\n1) ПРИОБРЕТИ ПОСТЕР ✅\nПереходи по ссылке и совершай оплату по СБП https://auth.robokassa.ru/merchant/Invoice/TNsGiM9VCk6ulRArMw4Dug\n\n‼ВНИМАНИЕ‼\nОПЛАТА ПРОХОДИТ С ЛЮБЫХ БАНКОВ.\nПодписывайтесь на наш Телеграм-канал, чтобы быть в курсе всех новостей https://t.me/ydachanabaikale\n\n2) ПОСЛЕ ОПЛАТЫ отправь нам чек, название или фото товара, ФИО, номер телефона участника\n3) Менеджер отправит вам номер с постером\n4) МОЖНО КУПИТЬ НЕОГРАНИЧЕННОЕ КОЛИЧЕСТВО ПОСТЕРОВ. Больше постеров = больше шансов.\n\nГотово! В течение 24 часов наши менеджеры внесут Вас в список участников акции и отправят постер\n\nИТОГИ АКЦИИ ПОДВЕДЕМ В ПРЯМОМ ЭФИРЕ когда будут проданы все постеры\n\nПобедителя выберет генератор случайных чисел.\n\nЕсли нужна будет помощь, пиши! Мы на связи",
                    random_id=0
                )

while True:
    try:
        start_bot()
    except Exception as e:
        print(f"Ошибка: {e}")
        print("Перезапуск через 5 секунд...")
        time.sleep(5)