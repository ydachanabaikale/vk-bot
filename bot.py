import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import time
import os

# ===== БЕРЁМ ДАННЫЕ ИЗ ПЕРЕМЕННЫХ ОКРУЖЕНИЯ =====
VK_TOKEN = os.getenv("VK_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID", 0))
# =================================================

def start_bot():
    vk_session = vk_api.VkApi(token=VK_TOKEN)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    print("✅ Бот запущен! Жду сообщений...")

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg = event.text.lower().strip()

            if "айфон" in msg:
                vk.messages.send(
                    user_id=event.user_id,
                    message="Здравствуйте!\n\nДля того чтобы стать участником акции и получить шанс выиграть IPhone 17E, необходимо приобрести постер за 300₽\n\nИНСТРУКЦИЯ:\n\n1) ПРИОБРЕТИ ПОСТЕР ✅\nВоспользуйтесь QR кодом или совершите перевод по номеру телефона 89148902272 Альфа Банк\n\n‼ВНИМАНИЕ‼\nПолучатель Непомнящих Иван Андреевич\n📌 В назначении платежа ничего не указывать\n\n2) ПОСЛЕ ОПЛАТЫ отправь нам чек, ФИО, номер телефона участника 🤝 \n3) Менеджер отправит вам номер с постером\n4) МОЖНО КУПИТЬ НЕОГРАНИЧЕННОЕ КОЛИЧЕСТВО ПОСТЕРОВ. Больше постеров = больше шансов.\n\nГотово! В течение 24 часов наши менеджеры внесут Вас в список участников акции и отправят постер 🔥 \n\nИТОГИ АКЦИИ ПОДВЕДЕМ В ПРЯМОМ ЭФИРЕ 5 ИЮЛЯ ИЛИ КАК БУДУТ РАСПРОДАНЫ ВСЕ ПОСТЕРЫ 😎 \n\nПобедителя выберет генератор случайных чисел.\n\nЕсли нужна будет помощь, пиши! Мы на связи 😉 ",
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
