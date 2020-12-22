time = int(input('Введите время в секундах: '))

hours = time // 3600
residue = time % 3600
minutes = residue // 60
seconds = residue % 60

print("%02i:%02i:%02i" % (hours, minutes, seconds))
