from data.loader import bot, db
import hendlers



if __name__ == "__main__":
    db.create_table_users()
    bot.infinity_polling()