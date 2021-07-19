import time
import pyautogui


end = True
# coin_flip = True


def click():
    pyautogui.mouseDown()
    time.sleep(0.03)
    pyautogui.mouseUp()


def run():
    test = 0

    while True:
        while test < 10:
            flip = pyautogui.locateCenterOnScreen('./coin_flip/start.png', confidence=0.9)
            if bool(flip):
                pyautogui.moveTo(flip[0], flip[1] + 65)
                test = 10
            else:
                
                time.sleep(2)
                test += 1
        test = 0
        click()
        time.sleep(3)

        while test < 10:
            start = pyautogui.locateCenterOnScreen('./images/start.png', confidence=0.6)
            if bool(start):
                pyautogui.moveTo(start)
                test = 10
            else:
                time.sleep(2)
                test += 1
        test = 0

        click()
        time.sleep(4)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(3)

        import coin_flip
        coin_flip = coin_flip.coin_flip.start()

        if coin_flip:
            print('go_sleep')
            time.sleep(2)
            while test < 5:
                power = pyautogui.locateCenterOnScreen('./images/power.png', confidence=0.6)
                power2 = pyautogui.locateCenterOnScreen('./images/power2.png', confidence=0.6)
                if bool(power):
                    print('get_power')
                    pyautogui.moveTo(power)
                    click()
                    time.sleep(20)
                    print('go_next')
                    test = 5
                elif bool(power2):
                    print('get_power2')
                    pyautogui.moveTo(power2)
                    click()
                    time.sleep(20)
                    print('go_next')
                    test = 5
                else:
                    time.sleep(5)
                    test += 1
            test = 0
            while test < 5:
                choise = pyautogui.locateCenterOnScreen('./images/choise.png', confidence=0.6)
                if bool(choise):
                    pyautogui.moveTo(choise)
                    click()
                    test = 5
                    time.sleep(60)
                else:
                    time.sleep(1)
                    test += 1
            test = 0


run()
