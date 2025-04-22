import qrcode
# Generate Grounded CC QR
qrcode.make("https://ianwong123.github.io/cc-qr/grounded-cc.jpg").save("grounded-qr.png")
# Generate Coated CC QR
qrcode.make("https://ianwong123.github.io/cc-qr/coated-cc.jpg").save("coated-qr.png")
