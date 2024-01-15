import requests

class LINENotifyBot(object):
    API_URL = 'https://notify-api.line.me/api/notify'

    def __init__(self, access_token):
        self.__headers = {'Authorization': 'Bearer ' + access_token}

    def send(self, message, image=None, sticker_package_id=None, sticker_id=None):
        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id,
        }
        files = {}
        if image is not None:
            try:
                with open(image, 'rb') as img:
                    files = {'imageFile': img}
                    r = self._make_request(payload, files)
                    r.raise_for_status()
            except IOError as e:
                print(f"画像ファイルのオープンに失敗しました: {e}")
            except requests.exceptions.RequestException as e:
                print(f"リクエスト中にエラーが発生しました: {e}")
        else:
            try:
                r = self._make_request(payload, files)
                r.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"リクエスト中にエラーが発生しました: {e}")

    def _make_request(self, payload, files):
        return requests.post(
            LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload,
            files=files
        )
