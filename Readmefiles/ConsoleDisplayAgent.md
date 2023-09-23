# Console Display Agent Documentation 📰📺

The Console Display Agent is a critical component of the News Agent project, responsible for receiving news data from the News Data Provider Agent and displaying it in a structured format on the console. It allows users to stay updated with the latest news articles conveniently.

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

The Console Display Agent is designed to receive news data and display it in a visually appealing and structured format on the console. It presents news articles in a card-like structure, making it easy for users to read and digest the information.

## Features

### Structured News Display
- News articles are displayed in a card-like format with clear sections for source, publication time, title, description, and URL.

### Real-time Updates
- The agent continuously receives news data and updates the console display with the latest articles.

### Customizable Display
- Users can adjust the card format, border settings, and other display elements based on their preferences.

## Getting Started

To use the Console Display Agent, follow these steps:

1. Install the necessary Python packages:
   ```bash
   pip install uagents
   ```

2. Set up the agent by providing a unique name, port, seed, and endpoint for communication. Ensure that the `fund_agent_if_low` function is called with the agent's wallet address for sufficient funds.

3. Customize the display format, border settings, and any other visual elements as desired.

## Usage

The Console Display Agent works in conjunction with the News Data Provider Agent. It receives news articles from the data provider agent and displays them on the console in a structured format.

## Configuration

The key configurations for the Console Display Agent include:

- `@bob.on_message(model=DataModel)`: Defines the message model that the agent listens for. In this case, it listens for `DataModel` messages containing news data.

- Customization of the card-like structure and border settings for the news display.

## Example Usage

```python
# Import necessary modules and create the agent

@bob.on_message(model=DataModel)
async def handle_data(ctx: Context, sender: str, msg: DataModel):
    # Define border settings and create a card-like format

    # Display news information in the card format
    print(formatted_message)

    # Send the received data to the "web_agent" for web display

if __name__ == "__main__":
    bob.run()
```

## Contributing

We welcome contributions from the community! If you have ideas for improvements or new features, please open an issue or submit a pull request.


---

Feel free to explore and experiment with the Console Display Agent to enhance your understanding of agent-based systems and their applications. Happy coding and keep experimenting with uAgents! 🚀🤖