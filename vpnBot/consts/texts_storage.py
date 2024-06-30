from abc import ABC

from vpnBot.consts.common import PRICE, INVITATION_BONUS


class TextsStorage(ABC):
    START_TEXT = (
        "Привет! Этот бот предоставляет доступ к быстрому и стабильному vpn.\n"
        f"На вашем балансе {PRICE}₽, чтобы Вы могли попробовать первый месяц бесплатно.\n\n"
        'Для начала, нужно скачать приложение Wireguard (по ссылке снизу), вернуться в бота и нажать на кнопку "Перейти в меню" на клавиатуре ниже.'
    )

    WG_APP_ANDROID_LINK = (
        "https://play.google.com/store/apps/details?id=com.wireguard.android"
    )
    WG_APP_IOS_LINK = "https://apps.apple.com/us/app/wireguard/id1441195209"
    WG_APP_PC_LINK = "https://www.wireguard.com/install/"

    MAIN_MENU_TEXT_FROM_START = 'Отлично!\nТеперь, чтобы подключить vpn, нажми на кнопку "Устройста" в меню ниже, а затем на кнопку "Добавить устройство".'

    MAIN_MENU_TEXT = (
        "Меню\n"
        'Для добавления нового устройства или удаления существующего, перейдите в раздел "Устройства".\n'
        'Для пополнения баланса или просмотра истории транзакций, перейдите в раздел "Финансы".'
    )

    CHOOSE_DEVICE = "Выберите устройство:"
    NO_DEVICES_ADDED = "У Вас пока нет добавленных устройств."

    ADD_DEVICE_CONFIRMATION_INFO = (
        "После добавления устройства с вашего счета автоматически спишется сумма, "
        "соответствующая стоимости подписки в месяц за одно устройство - {}₽.\n"
        "На Вашем счете - {}₽."
    )

    DELETE_DEVICE_CONFIRMATION_INFO = "Вы уверены, что хотите удалить устройство? Доступ к vpn будет ограничен сразу после удаления."

    SOMETHING_WENT_WRONG_TRYING_AGAIN_MSG = (
        "К сожалению, что-то пошло не так :( \n Пробуем еще раз, подождите немного.."
    )

    SOMETHING_WENT_WRONG_ERROR_MSG = (
        "К сожалению, что-то пошло не так :( \n"
        "Попробуйте повторить операцию еще раз."
    )

    SOMETHING_WENT_VERY_WRONG_ERROR_MSG = (
        "К сожалению, что-то пошло не так :( \n"
        "Похоже, мы списали средства с карты и не смогли зачислить их."
        "Свяжитесь с @arseny_volodko."
    )

    SPECIFIC_DEVICE_INFO_TEXT = (
        "Устройство №{}:\n" "Статус: {}.\n" "Следующее списание: {}.\n"
    )

    ACTIVE = "Активно 🟢"
    INACTIVE = "Не активно 🔴"

    DEVICE_SUCCESSFULLY_ADDED = "Устройство успешно добавлено."
    DEVICE_SUCCESSFULLY_DELETED = "Устройство успешно удалено."

    CURRENT_BALANCE = "Текущий баланс: {}₽."

    ACTUAL_ON_MOMENT = "Актуально на момент: {}"

    ON_YOUR_ACCOUNT = "На вашем счете: {}₽."

    CHOOSE_SUM_TO_FILL_UP_BALANCE = "Выберите, на какую сумму пополнить баланс."

    INPUT_PROMO_CODE = "Введите промокод."

    PROMO_CODE_SUCCESSFULLY_APPLIED = (
        "Промокод успешно применен. Ваш баланс пополнен на {}₽."
    )

    # EXCEPTIONS

    NOT_ENOUGH_MONEY_ERROR_MSG = (
        "На вашем счете недостаточно средств для подключения нового устройства.\n"
        f"Стоимость подписки: {PRICE}₽ в месяц."
    )

    NO_AVAILABLE_IPS_ERROR_MSG = (
        "К сожалению, на данный момент на сервере закончились свободные IP адреса. "
        "Приносим извинения за доставленные неудобства."
    )

    NO_SUCH_CLIENT_ERROR_MSG = "Похоже, такого устройства уже не существует."

    DEVICE_LIMIT_ERROR_MSG = "Вы можете добавить не более 3х устройств."

    ALREADY_USED_PROMO_CODE_ERROR_MSG = "Вы уже воспользовались данным промокодом."

    NO_SUCH_PROMO_CODE_ERROR_MSG = "Похоже, такого промокода не существует."

    PROMO_CODE_INACTIVE_ERROR_MSG = "Данный промокод более недействителен."

    INVITATION_LINK_INFO_MSG = (
        f"Вы можете пригласить друзей и получить {INVITATION_BONUS}₽ за каждого нового пользователя, "
        "перешедшего по вашей пригласительной ссылке: {}"
    )

    SUCCESSFUL_INVITATION_INFO_MSG = (
        f"Вам начислено {INVITATION_BONUS}₽ за приглашение нового пользователя."
    )

    SUBSCRIPTION_SUCCESSFULLY_RENEWED = (
        "Подписка на устройство №{} успешно продлена.\n"
        f"С вашего счета списано {PRICE}₽."
    )

    SUBSCRIPTION_NOT_RENEWED = (
        "Доступ к VPN для устройства №{} приостановлен из-за нехватки средств на счете для продления подписки.\n"
        'Для возобновления подписки пополните баланс, перейдите в меню в раздел "Устройства", '
        'выберите соответствующее устройство и нажмите "Активировать".'
    )

    INACTIVE_DEVICE_DELETED = (
        "Устройство №{} удалено, поскольку было неактивно в течение 2х месяцев."
    )

    DEVICE_SUBSCRIPTION_SUCCESSFULLY_RESUMED = "Подпика успешно возобновлена."

    DEVICE_SUBSCRIPTION_ALREADY_ACTIVE = "Подписка на устройство уже активна."

    BALANCE_SUCCESSFULLY_FILLED_UP = "Баланс успешно пополнен."

    FILL_UP_BALANCE_INFO_MSG = "Пополнение баланса на {}₽."
    PAY = "Оплатить"

    ADDING_DEVICE_INFO_MSG = "Удаляем устройство.."

    INSTRUCTION = (
        "<b>Инструкция по подключению:</b>\n"
        "1. Откройте QR на другом устройстве.\n"
        '2. Откройте скаченное приложение Wireguard на вашем телефоне и нажмите на кнопку "Добавить туннель" или на плюсик.\n'
        '3. В предложенных вариантах выберите "Создать из QR-кода".\n'
        "4. Отсканируйте QR и введите любое название тунеля.\n\n"
        "Ура! Теперь можно смотреть рилсы!\n\n"
        "см. также:\n"
        "1. <a href='https://www.notion.so/vpn-Wireguard-CyberNexVpn-a890908d8b854002b8842cfcb1f78de2'>Быстрое и удобное подключение vpn на Iphone</a>\n"
        "2. <a href='https://www.notion.so/vpn-Wireguard-CyberNexVpn-a890908d8b854002b8842cfcb1f78de2?pvs=4#ac6c73a025344076aadc43df5f06034c'>Альтернативные способы подключения</a>\n"
        "Если что-то не выходит или не работает - напишите @arseny_volodko."
    )

    YOOKASSA_ERROR_INFO_MSG = "К сожалению, платежная система не отвечает, попробуйте повторить операцию через некоторое время."
