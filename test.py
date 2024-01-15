from line_notify_bot import LINENotifyBot
from dotenv import load_dotenv
import os


load_dotenv()  # .envファイルから環境変数を読み込む
access_token = os.getenv('AccessToken')

bot = LINENotifyBot(access_token)

bot.send(
    message='Test配信です',
    # image='test.png',  # png or jpg
    image='user.png',  # png or jpg
    sticker_package_id=1,
    sticker_id=13,
)


