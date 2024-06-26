import pyfirmata

comport='COM8'

board=pyfirmata.Arduino(comport)


led_1=board.get_pin('d:8:o')
led_2=board.get_pin('d:9:o')
led_3=board.get_pin('d:10:o')
led_4=board.get_pin('d:11:o')
led_5=board.get_pin('d:12:o')

def led(fingerUp):
    a,b,c,d,e=fingerUp
    print(a,b,c,d,e)
    led_1.write(a)
    led_2.write(b)
    led_3.write(c)
    led_4.write(d)
    led_5.write(e)
    