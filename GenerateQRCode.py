import segno


class GenerateInfoQR:
    def __init__(self, name, size, information):
        self.name = name + ".png"
        self.size = size
        self.information = information

    def createSticker(self):
        qrcode = segno.make_qr(self.information)
        qrcode.save(self.name, scale=self.size)
        #print(self.information, self.size, self.name)


