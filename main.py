from controller import controller
from recording import bank
from strategies.gmail.gmailStrategy import gmailStrategy
from strategies.Telegram.TelegramStrategy import TelegramStrategy
import threading



bank.updateAllBalances()

# CHANGE THIS TO GO FROM TESTNET TO LIVENET
real_money = False

telegramBot = TelegramStrategy()
telegramThread = threading.Thread(target=telegramBot.run()).start()

trader = controller(.001, .1, real_money)
trader.importAPIKeys()
trader.addStrategy(gmailStrategy('strategies/gmail/credentials.json'))
trader.run()

