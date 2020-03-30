from twilio.rest import Client
import os
from Corona_Updater import india_data, world_data
from dotenv import load_dotenv
import time

# Load Environment variable 
load_dotenv()

# Main Function.
def main():
    # Account_sid
    acc_sid = os.getenv("acc_sid")
    # Auth Key or token 
    auth_token = os.getenv("auth_token")

    # Setting up client
    client = Client(acc_sid, auth_token)
    # Urls for function call
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
    r = [os.getenv("To_no"), os.getenv("To_no_2")]
    # Creating Message for sending.
    for i in r:
        message = client.messages.create(body = text,
                                        from_ = os.getenv("twilio_no"),
                                        to = i
                                        )
        print(message.sid)

# Driver Code.
if __name__ == "__main__":
    main()