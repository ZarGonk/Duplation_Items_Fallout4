from pynput import keyboard
from pynput.keyboard import Key, Controller
import threading
import time

teclado = Controller()
executando = False
parar_execucao = False

def pressionar_teclas():
    global executando, parar_execucao
    while executando and not parar_execucao:
        print("Executando sequência de teclas...")

        # Pressiona R por 1 segundo
        teclado.press('r')
        time.sleep(1)
        teclado.release('r')

        # Aguarda 0.01 segundos
        #time.sleep(0.1)

        # Pressiona TAB por 5 segundos
        teclado.press(Key.tab)
        time.sleep(5)
        teclado.release(Key.tab)

        # Pequeno intervalo entre repetições (opcional)
        time.sleep(0.1)

def ao_pressionar_tecla(tecla):
    global executando, parar_execucao
    try:
        if tecla == keyboard.Key.f2 and not executando:
            print("F2 pressionado: Iniciando execução contínua.")
            executando = True
            parar_execucao = False
            thread = threading.Thread(target=pressionar_teclas)
            thread.start()

        elif tecla == keyboard.Key.f4:
            print("F4 pressionado: Parando execução.")
            parar_execucao = True
            executando = False

    except Exception as e:
        print(f"Erro: {e}")

def main():
    print("Aguardando F2 para iniciar e F4 para parar.")
    with keyboard.Listener(on_press=ao_pressionar_tecla) as listener:
        listener.join()

if __name__ == "__main__":
    main()
