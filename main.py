import pyautogui
import time

numberOfRole = 0
numberOfSignet = 0
numberOfMistyques = 0

def run():
    global numberOfMistyques
    global numberOfSignet
    time.sleep(1)
    signetFound = pyautogui.locateCenterOnScreen("templates/signetPrice.png", confidence=0.95)
    if signetFound!=None:
        pyautogui.click(signetFound)
        time.sleep(1)
        validateSignet = pyautogui.locateCenterOnScreen("templates/checkSummon.png", confidence=0.99)
        if validateSignet!=None:
            buySignet = pyautogui.locateCenterOnScreen("templates/buySignet.png")
            if buySignet != None:
                pyautogui.click(buySignet)
                numberOfSignet = numberOfSignet + 1
        else:
            cancel = pyautogui.locateCenterOnScreen("templates/cancelBuy.png")
            if cancel != None:
                pyautogui.click(cancel)
                time.sleep(0.2)
    mystiquesFound = pyautogui.locateCenterOnScreen("templates/mistyquesPrice.png", confidence=0.98)
    if mystiquesFound!=None:
        pyautogui.click(mystiquesFound)
        time.sleep(1)
        validateMistyques = pyautogui.locateCenterOnScreen("templates/checkSummon.png", confidence=0.99)
        if validateMistyques!=None:
            buyMistyques = pyautogui.locateCenterOnScreen("templates/buyMistyques.png")
            if buyMistyques != None:
                pyautogui.click(buyMistyques)
                numberOfMistyques = numberOfMistyques + 1
        else:
            cancel = pyautogui.locateCenterOnScreen("templates/cancelBuy.png")
            if cancel != None:
                pyautogui.click(cancel)
                time.sleep(0.2)

refreshButton = pyautogui.locateCenterOnScreen("templates/refresh.png")
pyautogui.click(refreshButton)
time.sleep(1)
confirmRefreshButton = pyautogui.locateCenterOnScreen("templates/confirmRefresh.png")
pyautogui.click(confirmRefreshButton)
try:
    while numberOfRole < 4000:
        time.sleep(1)
        run()
        time.sleep(0.5)
        pyautogui.mouseDown(1000, 1000)
        pyautogui.dragTo(1000, 200, 0.5)
        pyautogui.mouseUp(1000, 200)
        time.sleep(1)
        run()
        time.sleep(0.2)
        pyautogui.click(refreshButton)
        time.sleep(0.5)
        pyautogui.click(confirmRefreshButton)
        time.sleep(1)
        numberOfRole = numberOfRole + 1
except KeyboardInterrupt:
    print("Interrompu par action humaine")

print("number of role : " + numberOfRole.__str__())
print("number of signet buy : " + numberOfSignet.__str__())
print("number of mistyque buy : " + numberOfMistyques.__str__())
