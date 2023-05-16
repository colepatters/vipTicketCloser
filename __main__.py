import pyautogui
from pynput import mouse

# Initialize pause
pause = 0.5
pyautogui.PAUSE = pause
pyautogui.FAILSAFE = True

# Initialize position variables
payPOS = None
otherPOS = None
vipPOS = None

# Initialize ticket counter
totalTickets = 0

# Initialize last click
lastClick = None

def closeTicket():
    pyautogui.click(payPOS)
    pyautogui.click(otherPOS)
    pyautogui.click(vipPOS)
    
# Setup mouse listener
def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        global lastClick
        lastClick = Click(x, y)
        return False
        
def startListener():
    with mouse.Listener(
            on_click=on_click) as listener:
        listener.join()
        
class Click:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
# Set up the positions of the buttons automatically
def autoSetup():
    pyautogui.alert("Please make sure the Android window is visible and the app is open.", title = 'TicketCloser Setup')
    
    global payPOS
    payPOS = pyautogui.locateCenterOnScreen('images/builtin/pay.png', confidence=0.9)
    
    if payPOS != None:
        pyautogui.click(payPOS)
    else:
        print("Pay button not found")
    
    global otherPOS
    otherPOS = pyautogui.locateCenterOnScreen('images/builtin/other.png', confidence=0.9)
    
    if otherPOS != None:
        pyautogui.click(otherPOS)
    else:
        print("Other button not found")
    
    global vipPOS
    vipPOS = pyautogui.locateCenterOnScreen('images/builtin/vip.png', confidence=0.9)
    
    if vipPOS != None:
        pyautogui.click(vipPOS)
    else:
        print("VIP button not found")  
        
    if payPOS != None and otherPOS != None and vipPOS != None:
        print("Setup complete")
    else:
        raise Exception("Setup failed. Please check and make sure the window is visible and try again.")

# Set up the positions of the buttons manually
def manualSetup():
    global payPOS
    global otherPOS
    global vipPOS
    
    pyautogui.alert("Click the Pay button.", title = 'Ticket Closer Manual Setup')
    startListener()
    print("Click detected at " + str(lastClick.x) + ", " + str(lastClick.y))
    payPOS = (lastClick.x, lastClick.y)
    
    pyautogui.alert("Click the Other button.", title = 'Ticket Closer Manual Setup')
    startListener()
    print("Click detected at " + str(lastClick.x) + ", " + str(lastClick.y))
    otherPOS = (lastClick.x, lastClick.y)
    
    pyautogui.alert("Click the VIP button.", title = 'Ticket Closer Manual Setup')
    startListener()
    print("Click detected at " + str(lastClick.x) + ", " + str(lastClick.y))
    vipPOS = (lastClick.x, lastClick.y)
    
    pyautogui.alert("Setup complete.", title = 'Ticket Closer Manual Setup')
    

def ticketCloser(safemode = False):
    numIterations = pyautogui.prompt(text='How many tickets would you like to close?', title='Ticket Closer', default='50')
    try:
        numIterations = int(numIterations)
    except:
        response = pyautogui.confirm("Invalid input. Please enter a number.", title = 'Ticket Closer', buttons = ['OK', 'Exit'])
        if response == "Exit":
            exit()
        else:
            ticketCloser()
    
    pyautogui.alert("Closing " + str(numIterations) + " tickets. This will take about " + str((numIterations * pause) + (0.75 * numIterations)) + " seconds. FAILSAFE IS ENABLED. TO QUIT AT ANY TIME, DRAG MOUSE TO TOP LEFT CORNER OF SCREEN." )
    
    # If safemode is enabled, locate images every time before clicking
    if safemode:
        pass
    
    # If safemode is disabled, locate images once and store the position
    if not safemode:    
        for i in range(numIterations):
            closeTicket()
            
            global totalTickets
            totalTickets += 1
        
    if pyautogui.confirm("Successfully closed " + str(numIterations) + " tickets.", title = 'Ticket Closer', buttons = ['Close More', 'Exit']) == "Close More":
        ticketCloser()
    else:
        exit()
    

pyautogui.alert("Welcome to Ticket Closer. Please make sure you have read the docs before using this program.", title = 'Ticket Closer', button = 'Continue')

setupType = pyautogui.confirm("Would you like to set up the positions of the buttons automatically or manually?", title = 'Ticket Closer', buttons = ['Auto', 'Manual'])
if setupType == "Auto":
    autoSetup()
elif setupType == "Manual":
    manualSetup()
elif setupType == None:
    exit()

ticketCloser()

# Unreachable
if totalTickets != 0:
    pyautogui.alert("Total tickets closed: " + str(totalTickets), title = 'Ticket Closer')

