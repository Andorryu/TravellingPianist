import time
import pcf8574_io as pcf



p1 = pcf.PCF(0x20)

p1.pin_mode("0", "OUTPUT")
p1.pin_mode("1", "OUTPUT")
p1.pin_mode("2", "OUTPUT")
p1.pin_mode("3", "OUTPUT")
p1.write("0", "LOW")
p1.write("1", "LOW")
p1.write("2", "LOW")
p1.write("3", "LOW")

p1.write("0", "HIGH")

time.sleep(5)

p1.write("0", "LOW")
p1.write("1", "LOW")
p1.write("2", "LOW")
p1.write("3", "LOW")
