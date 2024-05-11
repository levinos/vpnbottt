from abc import ABC

from vpnBot.static.common import PRICE


class TextsStorage(ABC):
    START_TEXT = (
        "Привет! Этот бот предоставляет специальные ключи для подключения к VPN через приложение Wireguard."
        "Уникальные алгоритмы шифрования и маршрутизации не снижают скорость интернета, а также обеспечивают мгновенное подключение к VPN.\n\n"
        f"На вашем балансе {PRICE}₽, чтобы Вы могли попробовать первый месяц бесплатно.\n\n"
        "Для начала, нужно скачать приложение Wireguard, а затем перейти в меню."
    )

    WG_APP_ANDROID_LINK = (
        "https://play.google.com/store/apps/details?id=com.wireguard.android"
    )
    WG_APP_IOS_LINK = "https://apps.apple.com/us/app/wireguard/id1441195209"
    WG_APP_PC_LINK = "https://www.wireguard.com/install/"

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

    SOMETHING_WENT_WRONG_ERROR_MSG = (
        "К сожалению, что-то пошло не так :( \n"
        "Попробуйте повторить операцию еще раз."
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
        "На вашем счете недостаточно средств для подключения нового устройства. "
        "Стоимость подписки списывается автоматически после добавления устройства.\n"
        f"Стоимость подписки: {PRICE}₽ в месяц."
    )

    NO_AVAILABLE_IPS_ERROR_MSG = (
        "К сожалению, на данный момент на сервере закончились свободные IP адреса. "
        "Приносим извинения за доставленные неудобства."
    )

    DEVICE_LIMIT_ERROR_MSG = "Вы можете добавить не более 3х устройств."

    ALREADY_USED_PROMO_CODE_ERROR_MSG = "Вы уже воспользовались данным промокодом."

    NO_SUCH_PROMO_CODE_ERROR_MSG = "Похоже, такого промокода не существует."

    PROMO_CODE_INACTIVE_ERROR_MSG = "Данный промокод более недействителен."
