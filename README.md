# API Weatherstack

This program uses the Weatherstack API to provide weather information for a given location.

## Getting Started

### Prerequisites

You will need to have Python 3 installed on your system.

### Installing

1. Clone this repository to your local machine.
2. Install the required Python packages using pip: `pip install requests json python-dotenv`.

### Usage

1. Sign up for a free Weatherstack API account at https://weatherstack.com/.
2. Create a file called `.env` in the root directory of the project.
3. Add the following line to your `.env` file, replacing `YOUR_API_KEY` with your actual API key: `API_KEY=YOUR_API_KEY`.
4. Run the program by typing `python main.py` in the command line.
5. Enter the location for which you want to retrieve weather information. Press ENTER to exit.

## Code Description

The program first prompts the user to enter a location. It then makes a request to the Weatherstack API using the `requests` library and the user's input as a query parameter.

If the API returns an error, the program prints the error message and exits. Otherwise, it extracts the relevant weather information from the API response and prints it to the console in a human-readable format.

The `dotenv` package is used to load the API key from the `.env` file, which is not tracked by Git to protect the key.

## Authors

allie-green

## Acknowledgments

Weatherstack API documentation
