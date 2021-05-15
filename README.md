# DiscordTokenLogin
A simple script with wich you can login to discord using a token instead of email &amp; password.

## How it works
The script asks you to input a token to login with. After you enter it, the program will open a chrome browser using selenium and load https://discord.com/login. Tho discord deletes the localStorage, the script recreates it and adds the token to it. After that it will reload the site and if you get redirected to https://discord.com/app it worked!

Note: Only user accounts work. If you try to use a Bot token or an invalid user token, https://discord.com/login will show up again. If that happens, just restart the programm and try it with another token.
