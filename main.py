import telegram
import telegram.ext


def main():
    updater = telegram.ext.Updater(token='YOUR_BOT_TOKEN', use_context=True)
    dispatcher = updater.dispatcher

    # Add your bot's command handlers here

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()