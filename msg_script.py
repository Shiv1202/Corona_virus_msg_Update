from twilio.rest import Client
import os
from Corona_Updater import india_data, world_data
from dotenv import load_dotenv
import time

load_dotenv()

# Main Function.
def main():
    acc_sid = os.getenv("acc_sid")
    auth_token = os.getenv("auth_token")


    client = Client(acc_sid, auth_token)
    main_url = "https://www.worldometers.info/coronavirus/"
    india_url = "https://www.worldometers.info/coronavirus/country/india/"
    w_data = world_data(main_url)
    i_data = india_data(india_url)
    # Message Body.
    text = f"""
            Corona virus Update.
            World Data - 
            Total = {w_data[0]}
            Deaths = {w_data[1]}
            Recoverd = {w_data[2]}
            India Data -
            Total = {i_data[0]}
            Deaths = {i_data[1]}
            Recoverd = {i_data[2]}
            STAY HOME, STAY SAFE
            """

    message = client.messages.create(body = text,
                                    from_ = os.getenv("twilio_no"),
                                    to = os.getenv("To_no")
                                    )
    print(message.sid)

# Driver Code.
if __name__ == "__main__":
    main()