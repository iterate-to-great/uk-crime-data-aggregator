# UK Crime Data Aggregator

A Python tool for aggregating and processing street-level crime data from UK Police Force datasets.

## Overview

This project processes crime data obtained from [data.police.uk](https://data.police.uk), aggregating street-level crimes by postcode from multiple CSV files contained within a zip archive. The tool outputs a consolidated CSV file with crime statistics organized by location and time.

## Features

- 📦 Process multiple CSV files from a single zip archive
- 📍 Aggregate crime data by postcode
- 📊 Organize data by crime type and month
- 🗺️ Preserve geographic coordinates (Longitude, Latitude)
- 📁 Export results to a clean, structured CSV format

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Installation

Install the package in development mode with all dependencies:
```bash
pip install -e ".[dev]"
```

This will install:
- The project as an editable package
- pytest for testing
- pytest-cov for code coverage

### Running Tests

Run all tests:
```bash
pytest
```

Run tests with coverage report:
```bash
pytest --cov=src --cov-report=term-missing
```

Run a specific test file:
```bash
pytest tests/test_hello.py -v
```

## Usage

### Basic Usage

```python
python aggregate_crimes.py input_data.zip output_crimes.csv
```

### Command Line Arguments

- `input_file`: Path to the zip file containing crime data CSVs
- `output_file`: Path for the output aggregated CSV file

## Data Source

Crime data is sourced from [data.police.uk](https://data.police.uk), the official UK Police open data portal. This portal provides:

- Street-level crime and anti-social behaviour data
- Outcomes for crimes at street-level
- Stop and search data

### Downloading Data

1. Visit [data.police.uk](https://data.police.uk)
2. Select your desired date range and geographic area
3. Download the data as a zip file
4. Use this zip file as input for the aggregator

## Output Format

The aggregated output CSV contains the following columns in order:

| Column | Description | Example |
|--------|-------------|---------|
| `postcode` | UK postcode | SW1A 1AA |
| `crime_type` | Category of crime | Burglary |
| `month` | Month of occurrence | 2024-01 |
| `longitude` | Geographic longitude | -0.127758 |
| `latitude` | Geographic latitude | 51.507351 |

### Sample Output

```csv
postcode,crime_type,month,longitude,latitude
SW1A 1AA,Burglary,2024-01,-0.127758,51.507351
E1 6AN,Vehicle crime,2024-01,-0.075268,51.518847
M1 1AE,Theft from the person,2024-02,-2.238156,53.477245
```

## Development
- Test Driven Development (Please write a unit test and an end-to-end test)
- Trunk Based Development (Please create a pull request for each ticket)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/{ticket-number}-AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature #{ticket-number}'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request (Please add the ticket number in the description e.g. `Make a big change #123`)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- UK Police Forces for providing open crime data
- [data.police.uk](https://data.police.uk) for maintaining the data portal
- Contributors and maintainers of this project

---

**Note**: This tool is for educational and research purposes. Always verify data accuracy for critical applications.
