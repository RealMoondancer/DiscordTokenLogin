from selenium import webdriver
import time


def add_token(driver, url, token='abc'):
    # JavaScript code to recreate the localStorage object, has to be executed after each reload on discord's sites.
    recreate_localStorage_script = '''
    const iframe = document.createElement('iframe');
    document.head.append(iframe);
    const pd = Object.getOwnPropertyDescriptor(iframe.contentWindow, 'localStorage');
    iframe.remove();    
    Object.defineProperty(window, 'localStorage', pd);
    '''

    print('[add_token] url:', url)
    driver.get(url)  # Opens the URL

    time.sleep(1)  # Waits 1 second after the site loaded fully

    try:
        driver.execute_script(
            recreate_localStorage_script)  # Recreates the localStorage Object after it gets deleted by discord
        driver.execute_script(
            f"window.localStorage.setItem('token', '\"{token}\"');")  # Adds the token to login with to the localStorage
        driver.refresh()  # Refreshes the Site

        # If you get redirected to https://discord.com/app it worked.
        # Otherwise the token probably doesn't work.

        # Checking if the token is in the localStorage
        driver.execute_script(
            recreate_localStorage_script)  # Recreating the localStorage Object again, has to be done after every reload
        print('[add_token] get token:', driver.execute_script(
            f"return window.localStorage.getItem('token');"))  # Gets the token value from the localStorage

    except Exception as ex:
        print('[Exception]', ex)  # If an exception occurs, it gets printed out here.


if __name__ == '__main__':
    token = input("Enter user Token:\n  -> ")

    driver = webdriver.Chrome()

    add_token(driver, "https://discord.com/login", token)  # Supply the driver, the website and the value

    input("Press ENTER to exit safely.")  # Wait for enter key to be pressed (in the console)
    driver.close()  # Ends the chromedriver.exe processes. If the window just gets closed those processes / this process stays running.
    exit()  # Exits the program.
