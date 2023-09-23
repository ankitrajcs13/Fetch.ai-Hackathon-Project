# News Data Provider Agent Documentation 📰🤖

The News Data Provider Agent is part of the News Agent project and serves as the primary agent responsible for fetching news articles from external sources and forwarding them to other agents for processing and display.

## Table of Contents
- [Agent Overview](#agent-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)

## Agent Overview

The News Data Provider Agent is designed to retrieve news articles from an external API and send this data to other agents within the uAgent ecosystem. It plays a crucial role in the flow of news information and enables the display of news articles on the console and web interfaces.

## Features

### Real-time News Article Retrieval
- The agent continuously fetches news articles in real-time from an external news API.

### Data Broadcasting to Multiple Agents
- News articles fetched by the agent are sent to other agents, allowing for various processing and display options.

### Configurable API Endpoint and Data Fetching Interval
- Users can configure the external API endpoint for news retrieval.
- The data fetching interval can be adjusted to control how frequently news articles are retrieved.

## Getting Started

To use the News Data Provider Agent, follow these steps:

1. Install the necessary Python packages:
   ```bash
   pip install uagents
   ```

2. Set up the agent by providing a unique name, port, seed, and endpoint for communication. Ensure that the `fund_agent_if_low` function is called with the agent's wallet address for sufficient funds.

3. Customize the external news API endpoint, API key, and data fetching interval based on your preferences.

## Usage

The News Data Provider Agent is typically used in conjunction with other agents like the Console Display Agent and Web Display Agent. It continuously fetches news articles and sends them to these agents for display.

## Configuration

The key configurations for the News Data Provider Agent include:

- `NEWS_API_KEY`: The API key required to access the external news API.
- `NEWS_API_URL`: The URL of the external news API. Customize this based on your desired news source.
- `@alice.on_interval(period=5.0)`: Adjust the interval (in seconds) at which news articles are fetched.

## Example Usage

```python
# Import necessary modules and create the agent

# Define the fetch_data_from_api() function

@alice.on_interval(period=5.0)
async def data_fetch(ctx: Context):
    # Customize the user_category_choice and articles retrieval based on user preferences

    if articles:
        for article in articles:
            # Create a DataModel instance for each article

            # Send the data_obj to other agents for display

@alice.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    # Handle incoming messages if needed
```

## Contributing

We welcome contributions from the community! If you have ideas for improvements or new features, please open an issue or submit a pull request.


---

Feel free to explore and experiment with the News Data Provider Agent to enhance your understanding of agent-based systems and their applications. Happy coding and keep experimenting with uAgents! 🚀🤖