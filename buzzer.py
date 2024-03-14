from machine import Pin
def toggle_buzz(buzzer):
    buzzer.value(not buzzer.value())
    print("anything", buzzer.value())
