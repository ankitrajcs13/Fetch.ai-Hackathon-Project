from uagents import Agent, Context, Model
import requests
from uagents.setup import fund_agent_if_low

class Message(Model):
    message: str

class DataModel(Model):
    source_name: str | None
    title: str | None
    description: str | None
    url: str | None
    published_at: str | None

RECIPIENT_ADDRESS = "agent1q2kxet3vh0scsf0sm7y2erzz33cve6tv5uk63x64upw5g68kr0chkv7hw50"

alice = Agent(
    name="alice",
    port=8000,
    seed="alice secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)

fund_agent_if_low(alice.wallet.address())

NEWS_API_KEY = "250fd000a28d46bebaca31aaa2d9697d"

def fetch_data_by_category(category):
    category_mapping = {
        1: "top-headlines?country=IN",
        2: "everything?domains=bbc.co.uk&apiKey=" + NEWS_API_KEY,
        3: "top-headlines?country=IN&category=sports",
        4: "everything?q=cryptocurrency&apiKey=" + NEWS_API_KEY,
        5: "top-headlines?country=IN&category=politics"
    }
    category_url = category_mapping.get(category)
    if category_url:
        NEWS_API_URL = f"https://newsapi.org/v2/{category_url}&apiKey={NEWS_API_KEY}"
        try:
            response = requests.get(NEWS_API_URL)
            if response.status_code == 200:
                data = response.json()
                articles = data.get("articles", [])[:10]  
                return articles
            else:
                print(f"Failed to fetch data from API. Status code: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []
    else:
        print("Invalid category selected.")
        return []

@alice.on_interval(period=5.0)
async def data_fetch(ctx: Context):
    
    user_category_choice = int(input("Select a category:\n1. Top 10 News\n2. World News (Technology)\n3. Sports\n4. Cryptocurrency\n5. Politics\nEnter your choice: "))
    articles = fetch_data_by_category(user_category_choice)
    if articles:
        for article in articles:
            data_obj = DataModel(
                source_name=article.get("source", {}).get("name"),
                title=article.get("title"),
                description=article.get("description"),
                url=article.get("url"),
                published_at=article.get("publishedAt")
            )
            await ctx.send(RECIPIENT_ADDRESS, data_obj)

@alice.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")

if __name__ == "__main__":
    alice.run()
