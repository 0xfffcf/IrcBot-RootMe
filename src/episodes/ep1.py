from asyncio import run, sleep
import math
import sys
sys.path.append('./')

from irc import Irc


# Global Variable
rootme_bot = "Candy"
command = "!ep1"
irc = Irc("irc.root-me.org", 6667, "#root-me_challenge", "soofiaaa")


def do_equation(equation : str):
    equation = equation.split('/', 1)

    sqrt_number1 = math.sqrt(int(equation[0]))
    multiplicaiton_result = sqrt_number1 * float(equation[1])
    
    return round(multiplicaiton_result, 2)


async def main():
    irc.connect()
    await sleep(2)
    
    print("Bot is on!")
    irc.send_message(rootme_bot, command)

    while True:
        message = irc.receive_message()
        private_message = irc.read_private_message(message)

        if private_message != None:
            result = do_equation(private_message)
            irc.send_message(rootme_bot, f"{command} -rep {result}")

            flag = irc.receive_message()
            flag_message = irc.read_private_message(flag)
            if flag_message != None:
                print(flag_message)
                irc.leave()

            exit()

if __name__ == "__main__":
    run(main())