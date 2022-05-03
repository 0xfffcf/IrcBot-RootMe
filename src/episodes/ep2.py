from asyncio import run, sleep
import base64
import sys
sys.path.append('./')


from irc import Irc


# Global Variable
rootme_bot = "Candy"
command = "!ep2"
irc = Irc("irc.root-me.org", 6667, "#root-me_challenge", "soofiaaa")


def decode_base64(encoded_string : str):
    return base64.b64decode(encoded_string).decode("UTF-8")


async def main():
    irc.connect()
    await sleep(2)
    
    print("Bot is on!")
    irc.send_message(rootme_bot, command)

    while True:
        message = irc.receive_message()
        private_message = irc.read_private_message(message)

        if private_message != None:
            decoded_string = decode_base64(private_message)
            irc.send_message(rootme_bot, f"{command} -rep {decoded_string}")

            flag = irc.receive_message()
            flag_message = irc.read_private_message(flag)
            if flag_message != None:
                print(flag_message)

            exit()


if __name__ == "__main__":
    run(main())