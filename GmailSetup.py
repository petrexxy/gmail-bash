import time, os, sys, re

def gotoLogin(__driver, __email, __password):
    try:
        __driver.get("https://google.com/gmail/"); time.sleep(1.5);
        #print(__driver.page_source)
        email_login_js = 'document.getElementById("Email").value = "%s";' \
                            %str(__email); email_login_js += 'document.getElementById("next").click();';
        __driver.execute_script(email_login_js); time.sleep(1.5)
        #print(__driver.page_source)
        #print("Set Email")
        password_login_js = 'document.getElementById("Passwd").value = "%s";' \
                            %str(__password); password_login_js += 'document.getElementById("signIn").click();'
        __driver.execute_script(password_login_js); time.sleep(1.5)
        #__driver.save_screenshot("login.png")
        return True
    except Exception as error:
        print(error);
        return False
def cursoroff():
    if 'posix' in os.name:
	sys.stdout.write("\x1b[?25l")
def cursoron():
    if 'posix' in os.name:
	sys.stdout.write("\x1b[?25h")
cursoroff()

def binSetup():
    if os.path.exists("/Applications/Chromium.app/Contents/MacOS/Chromium"):
        bin_path = "/Applications/Chromium.app/Contents/MacOS/Chromium"
    elif os.path.exists("/usr/bin/chromium"):
        bin_path = "/usr/bin/chromium"
    else:
        while True:
            bin_path = raw_input("Please Enter Chrome/Chromium Executable Path: ")
            if os.path.exists(bin_path):
                break
            else:
                print("\nNot A Valid Path\n")
                continue
    return bin_path

def driverSetup(arch):
#	print(os.getcwd()+"/Drivers/chromedriver%s"%arch)
    if os.path.exists(os.getcwd()+"/Drivers/chromedriver%s"%arch):
	    #print("Driver Found")
        return str(os.getcwd()+"/Drivers/chromedriver%s"%arch)
    else: return False

def manualdriverSetup():
    while True:
        driver_path = raw_input("Driver Path: ")
        if os.path.exists(driver_path):
            return driver_path
            break
        else:
            print("\nNot Valid Path\n")
            continue
