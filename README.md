

# Indeed Scraper Command Line Tool

- Scrape jobs posted on Indeed.
- Get detailed information from this job portal about saved and sponsored jobs.
- Specify the search based on location with the output attributes position, location, and description.

This Python script is a command-line implementation of the Indeed Scraper by Misceres available on the Apify platform. For more details about the Indeed Scraper, refer to [the Apify website](https://apify.com/misceres/indeed-scraper).

## Usage

1. **Clone the Repository:**
   Clone this repository to your local machine:

   ```
   git clone git@github.com:AJeschor/indeed-webscraper.git
   ```

2. **Create a Virtual Environment:**
   Navigate to the project directory and create a virtual environment:

   ```
   cd indeed-webscraper
   python -m venv .env
   ```

3. **Activate the Virtual Environment:**
   On Windows:

   ```
   .env\Scripts\activate
   ```

   On macOS and Linux:

   ```
   source .env/bin/activate
   ```

4. **Install Dependencies:**
   Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

5. **Prepare API Token:**
   Place your Apify API token in a file named `apify_api_token.json` in the same directory as the script. The file should contain your token in the following format:

   ```json
   {
       "API_TOKEN": "your_api_token_here"
   }
   ```

6. **Run the Script:**
   You can run the script from the command line:

   ```
   python main.py
   ```

   This will execute the webscraper, fetching job listings from Indeed and saving the results in JSON format in the `output_files` directory.

## Configuration

You can customize the webscraper's behavior by modifying the `RUN_INPUT` dictionary in the script. This dictionary contains parameters such as the positions to search for, the country, location, maximum number of items to fetch, etc.

### Webscraper Settings

[Source](https://apify.com/misceres/indeed-scraper/input-schema)

### Positions/keywords for search
- **Variable name:** position
- **Data type:** string
- **Requirement:** Optional

Any combination of positions or keywords for search. If Start URLs are used, search position is disabled.

### Country for search
- **Variable name:** country
- **Data type:** Enum
- **Requirement:** Optional

Country codes based on the ISO 3166-1 alpha-2 standard. Default value of this property is "US".

### Location for search
- **Variable name:** location
- **Data type:** string
- **Requirement:** Optional

Any combination of city, zip code, or locality for search.

### Max items
- **Variable name:** maxItems
- **Data type:** integer
- **Requirement:** Optional

Limit of detail/product pages to be scraped.

### Scrape company details
- **Variable name:** parseCompanyDetails
- **Data type:** boolean
- **Requirement:** Optional

If true, will also navigate to the company page of each job posting to scrape company info not available directly on the job posting page. Default value of this property is "false".

### Save Only Unique Items
- **Variable name:** saveOnlyUniqueItems
- **Data type:** boolean
- **Requirement:** Optional

If true, only unique items will be scraped. Default value of this property is "true".

### Follow redirects for apply link
- **Variable name:** followApplyRedirects
- **Data type:** boolean
- **Requirement:** Optional

If true, will follow redirects of Indeed's externalApplyLink and output the final one. Default value of this property is "true".

### Max concurrency
- **Variable name:** maxConcurrency
- **Data type:** integer
- **Requirement:** Optional

Specifies the maximum number of concurrent tasks or requests the Apify Actor will execute simultaneously.Be nice to the website; don't go over 10.

## Output

The scraped job listings will be saved as JSON files in the `output_files` directory. Each file will have a unique filename based on the current date and time of the run.

## Note

- Ensure that you have a stable internet connection while running the script to fetch job listings from Indeed.
- Be mindful of the Apify platform's usage limits to avoid exceeding any quotas or restrictions.

