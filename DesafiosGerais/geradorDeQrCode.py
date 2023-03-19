import qrcode

imagem = qrcode.make("https://github.com/isahonorato")

imagem.save("qrcode.png")