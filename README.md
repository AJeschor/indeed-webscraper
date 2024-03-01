

# Indeed Scraper Command Line Tool

- Scrape jobs posted on Indeed.
- Get detailed information from this job portal about saved and sponsored jobs.
- Specify the search based on location with the output attributes position, location, and description.

This Python script is a command-line implementation of the Indeed Scraper by Misceres available on the Apify platform. For more details about the Indeed Scraper, refer to [the Apify website](https://apify.com/misceres/indeed-scraper).
Its goal is to provide a simple CLI tool to scrape jobs posted on Indeed to get detailed information from about job postings based on location, position, and description.

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

```
{
  "Webscraper_Settings": {
    "RUN_INPUT": {
      "position": "biology, chemistry",
      "country": "CA",
      "location": "Ottawa",
      "maxItems": 5,
      "parseCompanyDetails": true,
      "saveOnlyUniqueItems": true,
      "followApplyRedirects": true,
      "maxConcurrency": 5
    }
```

#### Positions/keywords for search
- **Variable name:** position
- **Data type:** string
- **Requirement:** Optional

Any combination of positions or keywords for search. If Start URLs are used, search position is disabled.

#### Country for search
- **Variable name:** country
- **Data type:** Enum
- **Requirement:** Optional

Country codes based on the ISO 3166-1 alpha-2 standard. Default value of this property is "US".

#### Location for search
- **Variable name:** location
- **Data type:** string
- **Requirement:** Optional

Any combination of city, zip code, or locality for search.

#### Max items
- **Variable name:** maxItems
- **Data type:** integer
- **Requirement:** Optional

Limit of detail/product pages to be scraped.

#### Scrape company details
- **Variable name:** parseCompanyDetails
- **Data type:** boolean
- **Requirement:** Optional

If true, will also navigate to the company page of each job posting to scrape company info not available directly on the job posting page. Default value of this property is "false".

#### Save Only Unique Items
- **Variable name:** saveOnlyUniqueItems
- **Data type:** boolean
- **Requirement:** Optional

If true, only unique items will be scraped. Default value of this property is "true".

#### Follow redirects for apply link
- **Variable name:** followApplyRedirects
- **Data type:** boolean

- **Requirement:** Optional
If true, will follow redirects of Indeed's externalApplyLink and output the final one. Default value of this property is "true".

#### Max concurrency
- **Variable name:** maxConcurrency
- **Data type:** integer
- **Requirement:** Optional

Specifies the maximum number of concurrent tasks or requests the Apify Actor will execute simultaneously.Be nice to the website; don't go over 10.

## Output

The scraped job listings will be saved as JSON files in the `output_files` directory. Each file will have a unique filename based on the current date and time of the run.

## Note

- Ensure that you have a stable internet connection while running the script to fetch job listings from Indeed.
- Be mindful of the Apify platform's usage limits to avoid exceeding any quotas or restrictions.

## Contribute

#### Why Contribute?

- **Report Issues:** If you encounter any issues while using indeed-webscraper, such as bugs or unexpected behavior, reporting them is crucial. By doing so, you help maintain the quality of the package and provide valuable feedback to the developers. Additionally, you can use the issue tracker to suggest new features or enhancements.

- **Improve Features:** Contributing code through pull requests allows you to fix existing issues or extend the functionality of indeed-webscraper. Whether it's addressing a bug, adding new features, or enhancing existing ones, your contributions can significantly benefit the project and its users.

### How to Contribute

1. **Setup the Project on Your Local Machine:**

    - **Cloning the Repository:** Begin by creating a folder on your local machine and navigating to it. Then, clone the InfoExtractor repository using one of the following commands:
        ```
        git clone git@github.com:AJeschor/indeed-webscraper.git
        ```
        or
        ```
        git clone git@github.com:AJeschor/indeed-webscraper.git
        ```
        After cloning, navigate into the indeed-webscraper folder.

    - **Setting up the Environment:** Optionally, set up a project environment by creating a virtual environment if one needs to install any dependencies.

2. **General Guidelines for Contribution:**

    - **Reporting an Issue:** When reporting an issue, provide clear and detailed information, including a description of the problem, expected behavior, and relevant code snippets if applicable. This helps developers understand and address the issue effectively.

    - **Pull Request:** If you're submitting a pull request, clearly state its purpose in the description. Whether it's fixing a bug, adding features, or enhancing code quality, clearly communicate the intent of your contribution.

    - **Documentation and Comments:** When pushing code changes, ensure proper documentation through docstrings. Additionally, adding comments to your code helps explain its functionality, making it easier for others to understand and review your contribution.

By adhering to these guidelines and actively contributing to indeed-webscraper, you play a vital role in improving the package for both current and future users. Your contributions are greatly appreciated and help drive the success of the project.
