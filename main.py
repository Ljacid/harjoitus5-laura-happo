# 27.9.2026
# Laura Happo
# FoCarissa tarvittavat kirjastot

from machine import Pin, PWM
from time import sleep

# Laura Happo
# 6.10.2026
# Tehtävä 6.2
# FoCarin koodaus Tehtävän 5.2 pohjalta, S-kirjain peilikuvana

# Alkutoimet FoCarin toimintaan
# Moottori A (oikea)
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Moottori B (vasen)
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Tehojen / nopeuden määrittely - luvut alle 24000 eivät pyöritä moottoreita
# 25% = 16383 
# 50% = 32767
# 75% = 49150
# 100% = 65535

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

# 8 sekunnin tauko
sleep(8)

# Määritä funktiot
def kaannyVasen(suuntaO, suuntaV, nopeus, aika):
    # Eteenpäin
    m1.value(suuntaO)
    m2.value(suuntaV)
    # Liike
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

def kaannyOikea(suuntaO, suuntaV, nopeus, aika):
    # Eteenpäin
    m1.value(suuntaO)
    m2.value(suuntaV)
    # Liike
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

def eteenpain(suuntaO, suuntaV, nopeus, aika):
    # Eteenpäin
    m1.value(suuntaO)
    m2.value(suuntaV)
    # Liike
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

def taaksepain(suuntaO, suuntaV, nopeus, aika):
    # Pakita
    m1.value(suuntaO)
    m2.value(suuntaV)
    # Liike
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

def kaannyPaikalla(suuntaO, suuntaV, nopeus, aika):
    # Käännös
    m1.value(suuntaO)
    m2.value(suuntaV)
    # Liike
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

def stop(nopeus, aika):
    sleep(aika)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    # Odota yksi sekunti moottoreiden pysähtymistä
    sleep(1)

# Haetaan tekstitiedosto ja luetaan se 
with open('data.txt', 'r') as tiedosto:
    for rivi in tiedosto:
        komento = rivi.strip()

        # Määritetään komentojen toiminnot
        if komento == "eteen":
            eteenpain(1, 1, 32767, 3)
            stop(0, 1)

        elif komento == "oikea":
            kaannyOikea(0, 1, 32767, 3.7)
            stop(0, 1)

        elif komento == "vasen":
            kaannyVasen(1, 0, 32767, 3.7)
            stop(0, 1)

        elif komento == "180 astetta":
            kaannyPaikalla(1, 0, 32767, 8)
            stop(0, 1)

        elif komento == "peruuta":
            taaksepain(0, 0, 32767, 3.3)
            stop(0, 1)
