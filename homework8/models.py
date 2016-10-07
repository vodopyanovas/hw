import qrcode


class PostModel(object):
    def __init__(self, form_data):
        self.text = form_data['text']

    def get_qr(self, ):
        qr_code = qrcode.make(self.text)
        return qr_code.save('./tmp/qr.png')

    def save_text(self):
        with open('tmp/my_text.txt', 'w') as text_file:
            text_file.write(self.text)