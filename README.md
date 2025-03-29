# SalesDashboard
# Recruitment Data with Source Icons

This project generates a Pandas DataFrame simulating recruitment data and adds icons representing the recruitment sources (LinkedIn, Indeed, Company Website, Referral).

## Overview

The script `recruitment_data.py` contains two main functions:

* `generate_recruitment_data()`: Creates a DataFrame with simulated recruitment data, including Applicant ID, Job, Stage, Source, and Days to Hire.
* `add_source_icons()`: Adds a "Source Icon" column to the DataFrame, mapping each recruitment source to a corresponding Font Awesome icon name.

## Files

* `recruitment_data.py`: Python script containing the data generation and icon addition functions.
* `README.md`: This file, providing project documentation.

## Requirements

* Python 3.x
* Pandas (`pandas`)
* NumPy (`numpy`)
* (Optional) Dash (`dash`) and Dash Iconify (`dash_iconify`) for displaying icons in a web application.

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2.  (Optional) Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  Install the required packages:

    ```bash
    pip install pandas numpy
    #if you plan to use the dash example.
    pip install dash dash-iconify
    ```

## Usage

1.  Run the `recruitment_data.py` script:

    ```bash
    python recruitment_data.py
    ```

    This will generate the DataFrame, add the icons, and print the first few rows to the console.

2.  (Optional) For displaying the icons in a Dash web application:

    * Ensure Dash and Dash Iconify are installed.
    * Uncomment the Dash-related code in `recruitment_data.py`.
    * Run the script.
    * Open the displayed URL in your web browser.

## Function Details

### `generate_recruitment_data(num_jobs=5, num_applicants=100)`

* Generates a DataFrame with simulated recruitment data.
* Parameters:
    * `num_jobs`: Number of jobs (default: 5).
    * `num_applicants`: Number of applicants (default: 100).
* Returns: Pandas DataFrame.

### `add_source_icons(df)`

* Adds a "Source Icon" column to the DataFrame, mapping recruitment sources to Font Awesome icon names.
* Parameters:
    * `df`: Pandas DataFrame.
* Returns: Modified Pandas DataFrame.

## Icon Display Notes

* The "Source Icon" column contains Font Awesome icon names.
* To display the icons in a web environment, you'll need to include the Font Awesome library or use a library such as dash_iconify.
* If you just print the DataFrame to the console, it will display the icon names as strings.
* The dash example included in the code, shows how to properly display the icons in a web application.

## Example Output (Console)
