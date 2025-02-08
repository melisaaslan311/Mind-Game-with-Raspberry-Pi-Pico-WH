from machine import Pin
import random
import time

led_red = Pin(18, Pin.OUT)
led_green = Pin(19, Pin.OUT)
led_blue = Pin(20, Pin.OUT)

button_red = Pin(21, Pin.IN, Pin.PULL_DOWN)
button_green = Pin(22, Pin.IN, Pin.PULL_DOWN)
button_blue = Pin(1, Pin.IN, Pin.PULL_DOWN)

RS = Pin(15, Pin.OUT)
E = Pin(14, Pin.OUT)
D4 = Pin(12, Pin.OUT)
D5 = Pin(13, Pin.OUT)
D6 = Pin(16, Pin.OUT)
D7 = Pin(17, Pin.OUT)

leds = [led_red, led_green, led_blue]
buttons = [button_red, button_green, button_blue]

led_order = []  
player = []  
level = 1  

def send_data(value, is_data=True):
    RS.value(is_data)  
    D4.value((value >> 4) & 0x01)
    D5.value((value >> 5) & 0x01)
    D6.value((value >> 6) & 0x01)
    D7.value((value >> 7) & 0x01)
    E.value(1)
    time.sleep(0.001)
    E.value(0)
    D4.value(value & 0x01)
    D5.value((value >> 1) & 0x01)
    D6.value((value >> 2) & 0x01)
    D7.value((value >> 3) & 0x01)
    E.value(1)
    time.sleep(0.001)
    E.value(0)
    time.sleep(0.002)

def lcd_init():
    time.sleep(0.02)
    send_data(0x02, is_data=False)  
    send_data(0x28, is_data=False)  
    send_data(0x0C, is_data=False)
    send_data(0x06, is_data=False)  
    send_data(0x01, is_data=False) 
    time.sleep(0.002)

def lcd_write(text):
    for char in text:
        if char == '\n':
            send_data(0xC0, is_data=False)  # İkinci satıra geçiş
        else:
            send_data(ord(char), is_data=True)

def update_lcd(message):
    send_data(0x01, is_data=False)  
    time.sleep(0.5)
    lcd_write("omer - melisa") 
    send_data(0xC0, is_data=False)  
    time.sleep(0.5)
    lcd_write(message)  

def flash_led(led):
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.2)

def play_lcd_order(order):
    for led_index in order:
        flash_led(leds[led_index])
    time.sleep(1)

def get_player_input(led_order_length):
    input_order = []
    start_time = time.time()
    while len(input_order) < led_order_length:
        for i, button in enumerate(buttons):
            if button.value() == 1:  
                flash_led(leds[i])  
                input_order.append(i)
                time.sleep(0.5)  
                while button.value() == 1:  
                    time.sleep(0.01)  
                
                if input_order[-1] != led_order[len(input_order) - 1]:
                    update_lcd("Wrong button!")  
                    return []  
                if len(input_order) == led_order_length:
                    break
        if time.time() - start_time > 20:
            update_lcd("Time is up!")  
            time.sleep(0.5)
            return []  
    return input_order


lcd_init()
update_lcd("")  

while True:
    if level <= 5:  
        led_order.append(random.randint(0, 2))  
    else:
        update_lcd("You Win")  
        break  

    update_lcd("")  
    play_lcd_order(led_order)
    update_lcd("It's your turn!")  
    player = get_player_input(len(led_order))
    if player == []:
        break 

    if player == led_order:
        update_lcd("Next level!")  
        level += 1
        time.sleep(2)
    else:
        update_lcd("Game Over!")  
        break

