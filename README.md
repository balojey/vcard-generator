# Python vCard Generator Web App

This Python web application allows you to easily generate vCard files from data stored in an Excel sheet. With just a few simple steps, you can convert your contact information into vCard format, making it compatible with various contact management and email applications.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin using the vCard generator web app, ensure you have the following dependencies installed:

- Python 3.x
- Flask (a Python web framework)
- xlsx_csv (for converting Excel files to csv)
- flask-wtf (for creating forms)
- vcf_creator (for creating vCards from csv files)
- Poetry (for dependency management)

Set up the project using:

```bash
poetry add flask-wtf vcf_creator xlsx_csv
```

## Getting Started

1. Clone or download this repository to your local machine.

```bash
git clone https://github.com/ademolab91/vcard-generator.git
```

2. Navigate to the project directory:

```bash
cd vcard-generator
```

3. Create and activate a virtual environment (recommended):

```bash
poetry shell
```

4. Activate the virtual environment:

On Windows:

```bash
poetry shell
```

On macOS and Linux:

```bash
source venv/bin/activate
```

6. Start the Flask web application:

```bash
python main.py
```

The app should now be running locally at `http://localhost:5000`.

## Usage

1. Prepare your contact data in an Excel spreadsheet. The spreadsheet should have a header row with columns for the following fields: Name, Phone, Email, Address, and any other relevant fields.

2. Upload the excel sheet on the web interface.

3. Input a suffix and prefix if needed.

4. Access the web app by opening a web browser and navigating to `http://localhost:5000`.

5. Click the "Generate vCard" button.

6. The app will read the data from the excel file and generate vCard files for each contact listed in the Excel sheet.

7. Download the vCard files to your computer.

8. You can now import the vCard files into your preferred contact management or email application.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Please make sure to follow the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using the Python vCard Generator Web App. If you have any questions, issues, or suggestions, please feel free to open an issue or contact me at [ademolabalogun91@gmail.com](mailto:ademolabalogun91@gmail.com). I hope this tool simplifies the process of creating vCards from Excel data for your convenience.
