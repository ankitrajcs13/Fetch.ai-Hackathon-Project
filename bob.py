import json
import requests
from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

class DataModel(Model):
    source_name: str | None
    title: str | None
    description: str | None
    url: str | None
    published_at: str | None


web_agent_url = "http://127.0.0.1:8002/receive_data"  

bob = Agent(
    name="bob",
    port=8001,
    seed="bob secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)

fund_agent_if_low(bob.wallet.address())

@bob.on_message(model=DataModel)
async def handle_data(ctx: Context, sender: str, msg: DataModel):
    border_width = 100  
    border_color = "-"  

    
    border_line = border_color * border_width
    formatted_message = f"{border_line}\n"

    
    formatted_message += f"Source: {msg.source_name}\n"
    formatted_message += f"Published At: {msg.published_at}\n"
    formatted_message += f"Title: {msg.title}\n"
    formatted_message += f"Description: {msg.description}\n"
    formatted_message += f"URL: {msg.url}\n"

    formatted_message += f"{border_line}\n"


    print(formatted_message)

    data_to_send = {
        "source_name": msg.source_name,
        "title": msg.title,
        "description": msg.description,
        "url": msg.url,
        "published_at": msg.published_at,
    }

    try:
        response = requests.post(web_agent_url, json=data_to_send)
        if response.status_code == 200:
            print("Data sent to web_agent successfully.")
        else:
            print("Failed to send data to web_agent.")
    except requests.exceptions.RequestException as e:
        print("Error sending data to web_agent:", str(e))

if __name__ == "__main__":
    bob.run()




