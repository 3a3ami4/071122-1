#  Copyright (c) ChernV (@otter18), 2021.

import os
import random

from setup import bot, logger
from webhook import app

# --------------- dialog params -------------------
dialog = {
    'hello': {
        'in': ['привет', 'hello', 'hi', 'privet', 'hey'],
        'out': ['Приветствую', 'Здравствуйте', 'Привет!']
    },
    'size': {
        'in': ['размер', 'размера', 'размеры'],
        'out': ['У нас есть 4 стандартных размера, в зависимости от того сколько человек вы хотите разместить на портрете:\n Solo 50*40см. Один человек.\n Duet 60*40 см один или два человека.\n Trio 50*70 до трех человек на портрете.\n Family 60*80 до пяти человек на портрете.\n При желании, мы можем сделать портрет большего размера, но его стоимость нужно будет уточнить в мастерской.']
    },
    'coast': {
        'in': ['стоимость', 'цена', 'сколько стоит', 'будет стоить', 'ценник'],
        'out': ['Стоимость зависит от размера портрета.
\n Solo 50*40см. Один человек. 2990р.
\n Duet 60*40 см один или два человека 3499р.
\n Trio 50*70 до трех человек на портрете 4490р.
\n Family 60*80 до пяти человек на портрете! Стоимость 5590р.']
    },
    '3': {
        'in': ['привет', 'hello', 'hi', 'privet', 'hey'],
        'out': ['Приветствую', 'Здравствуйте', 'Привет!']
    },
    '4': {
        'in': ['привет', 'hello', 'hi', 'privet', 'hey'],
        'out': ['Приветствую', 'Здравствуйте', 'Привет!']
    },
    '5': {
        'in': ['привет', 'hello', 'hi', 'privet', 'hey'],
        'out': ['Приветствую', 'Здравствуйте', 'Привет!']
    },
    'how r u': {
        'in': ['как дела', 'как ты', 'how are you', 'дела', 'how is it going'],
        'out': ['Хорошо', 'Отлично', 'Good. And how are u?']
    },
    'name': {
        'in': ['зовут', 'name', 'имя'],
        'out': [
            'Я  Art_SHINE-bot! Как думаете, мне подойдёт имя \"Артиша\"?',
            'Называйте меня Артиша!'    
        ]
    }
}


# --------------- bot -------------------
@bot.message_handler(commands=['help', 'start'])
def say_welcome(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used /start or /help')
    bot.send_message(
        message.chat.id,
        '<b>Здравствуйте! С Вами на связи Бот студии волшебных портретов Art_SHINE! </b> Я с радостью отвечу на все ваши вопросы, или постараюсь сделать это! Пожалуйста, задайте ваш вопрос!',
        parse_mode='html'
    )


@bot.message_handler(func=lambda message: True)
def echo(message):
    for t, resp in dialog.items():
        if sum([e in message.text.lower() for e in resp['in']]):
            logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used {t}:\n\n%s', message.text)
            bot.send_message(message.chat.id, random.choice(resp['out']))
            return

    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used echo:\n\n%s', message.text)
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    if os.environ.get("IS_PRODUCTION", "False") == "True":
        app.run()
    else:
        bot.infinity_polling()
