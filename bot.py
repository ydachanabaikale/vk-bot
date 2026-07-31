import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import time
import os

# ===== БЕРЁМ ДАННЫЕ ИЗ ПЕРЕМЕННЫХ ОКРУЖЕНИЯ =====
VK_TOKEN = "vk1.a.2_7nA3gvjyhXp1pC_wQbSMxQ2Zq1X1dt1Xo2pni4GCIsfYBPcRgiqTlfTDi8Uk7Wx8CmFR_SGQNhS1zju_HfnYm_XjY3c4G6icu976fDBLcHk5fYQOeNCULDnEIY_4rZGq_VF8XFp957HRJP_88f6_ZLKHRcrG4IHMvuwVPGaNR7qLho2ugE67sd6dqQ-qxtmnzCUdDCGOdmz9rLBrBYgA"
GROUP_ID = 238085810
# =================================================

def start_bot():
    vk_session = vk_api.VkApi(token=VK_TOKEN)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    print("✅ Бот запущен! Жду сообщений...")

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg = event.text.lower().strip()

            if "удача" in msg:
                vk.messages.send(
                    user_id=event.user_id,
                    message="Здравствуйте!\n\nДля того чтобы стать участником акции и получить шанс выиграть Iphone 17 и другие классные призы, необходимо приобрести постер за 400₽\n\nИНСТРУКЦИЯ:\n\n1) ПРИОБРЕТИ ПОСТЕР ✅\nПереходи по ссылке и совершай оплату по СБП https://auth.robokassa.ru/merchant/Invoice/w54nx9dvOka7hCJx3AGshQ\n\n‼ВНИМАНИЕ‼\nОПЛАТА ПРОХОДИТ С ЛЮБЫХ БАНКОВ.\n📌 Подписывайтесь на наш Телеграм-канал, чтобы быть в курсе всех новостей https://t.me/ydachanabaikale\n\n2) ПОСЛЕ ОПЛАТЫ отправь нам чек, ФИО, номер телефона участника 🤝 \n3) Менеджер отправит вам номер с постером\n4) МОЖНО КУПИТЬ НЕОГРАНИЧЕННОЕ КОЛИЧЕСТВО ПОСТЕРОВ. Больше постеров = больше шансов.\n\nГотово! В течение 24 часов наши менеджеры внесут Вас в список участников акции и отправят постер 🔥 \n\nИТОГИ АКЦИИ ПОДВЕДЕМ В ПРЯМОМ ЭФИРЕ 5 АВГУСТА ИЛИ КАК БУДУТ РАСПРОДАНЫ ВСЕ ПОСТЕРЫ 😎 \n\nПобедителя выберет генератор случайных чисел.\n\nЕсли нужна будет помощь, пиши! Мы на связи 😉 ",
                    random_id=0
                )

# ===== АВТОМАТИЧЕСКИЙ ПЕРЕЗАПУСК =====
while True:
    try:
        start_bot()
    except Exception as e:
        print(f"⚠️  Ошибка: {e}")
        print("🔄  Перезапуск через 5 секунд...")
        time.sleep(5)
