length = int(input("Length(cm): "))
width = int(input("Width: "))
height = int(input("Height: "))
percent_acc = float(input("Percent of Acc: "))

volume = length * width * height
volume_in_litres = volume / 1000
acc_volumes = volume_in_litres * (percent_acc / 100)
needed_litres = volume_in_litres - acc_volumes

print(needed_litres)
