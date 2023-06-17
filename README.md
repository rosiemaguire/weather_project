# Weather Project
This is repository provides the foundation for a weather app. It is written in Python, with functions that helps you analyse and visualise weather data from a CSV file. The app requires a specific format for the input CSV file.
## Prerequisites
To run this repo, make sure you have the following dependencies installed:
- Python (version 3.6 or later)
- `datetime` module (for handling dates)
- `pandas` module (for data manipulation)

You can install the required Python modules using the following command:
```shell
pip install pandas
```

## CSV File Format
The input CSV file must adhere to the following format:
- The file should have three columns with the following headers: "date", "min", "max".
- The "date" column should contain dates in the ISO 8601 format as `yyyy-mm-ddThh:mm:ss+hh:mm` (e.g., "2021-07-02T07:00:00+08:00").
- The "min" and "max" columns should contain temperature values in degrees Fahrenheit an are expected to be imported as integers.

Here's an example of a valid CSV file:
```
date,min,max
2021-07-02T07:00:00+08:00,65,82
2021-07-03T08:00:00+08:00,62,78
2021-07-04T06:00:00+08:00,68,85
```

## Output
The functions will process the data from the CSV file and provide the following outputs:

- Temperature statistics: The app will display the minimum and maximum temperatures found in the data in a daily or a weekly summary.
- Average temperatures: The app will calculate and show the average low and average high temperature for each csv.
- The outputs will be displayed in the terminal or command prompt.

## Troubleshooting
If you encounter any issues while using this repository, please check the following:

- Ensure that your CSV file is in the correct format and contains the required columns with the correct headers
- Verify that you have installed all the necessary Python modules mentioned in the prerequisites section.
- Double-check that the CSV file is in the same directory as the Python script.
- Make sure you are running the script using a compatible version of Python (3.6 or later).
- If the problem persists, feel free to contact the author for further assistance.
## Acknowledgements
This weather project was created using the [She Codes Australia Template](https://github.com/SheCodesAus/plus-weather-project-template) and developed using the `datetime`, and `pandas` modules. I would like to express my gratitude to the authors and contributors of these open-source libraries for their valuable work.
If you find this project useful, consider leaving a star on the GitHub repository or providing feedback to help me improve it further.

Happy weather analysis!
