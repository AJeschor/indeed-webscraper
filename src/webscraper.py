import json
import os
import time
from apify_client import ApifyClient

def load_api_token():
    """
    Load API token from apify_api_token.json file in the current directory.

    Returns:
    - str or None: The API token if found, otherwise None.
    """
    # Get the path to the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the API token file
    api_token_file_path = os.path.join(current_directory, "apify_api_token.json")
    try:
        with open(api_token_file_path, "r") as token_file:
            return json.load(token_file).get("API_TOKEN")
    except FileNotFoundError:
        print(f"Error: apify_api_token.json not found in the current directory.")
        return None

def run_webscraper():
    """
    Run the webscraper.
    """
    # Load API token
    api_token = load_api_token()

    if not api_token:
        print("Error loading API token. Exiting.")
        return

    # Initialize WebscraperActor with an output directory.
    RUN_INPUT = {}
    client = ApifyClient(api_token)

    # Run the Apify actor and fetch the results.
    formatted_results = []
    run = client.actor("misceres/indeed-scraper").call(run_input=RUN_INPUT)
    
    # Iterate through the dataset items obtained from the actor run.
    for raw_item in client.dataset(run["defaultDatasetId"]).iterate_items():
        # Format the raw data into a structured dictionary.
        formatted_item = {
            "id": raw_item.get("id", ""),
            "company": raw_item.get("company", ""),
            "positionName": raw_item.get("positionName", ""),
            "jobType": raw_item.get("jobType", []),
            "location": raw_item.get("location", ""),
            "salary": raw_item.get("salary", None),
            "postingDateParsed": raw_item.get("postingDateParsed", ""),
            "url": raw_item.get("url", ""),
            "externalApplyLink": raw_item.get("externalApplyLink", ""),
            "companyDescription": raw_item.get("companyInfo", {}).get("companyDescription", ""),
            "description": raw_item.get("description", "")
        }
        formatted_results.append(formatted_item)

    # Get the current date and time for generating a unique output filename.
    current_datetime = time.strftime("%Y-%m-%d_%H-%M-%S")
    output_directory = os.path.abspath("output_files")
    output_filename = os.path.join(output_directory, f"results_{current_datetime}.json")

    # Write the formatted results to a JSON file.
    with open(output_filename, "w") as file:
        json.dump(formatted_results, file, indent=4)

    print(f"Webscraper run successfully. Results saved to: {output_filename}")

if __name__ == "__main__":
    run_webscraper()
