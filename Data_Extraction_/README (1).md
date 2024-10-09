# Data Extraction and Analysis Project


## Overview
This project involves extracting data from URLs, performing text analysis on the extracted data, and saving the results into an Excel file.



## Approach to the Solution
1. **Data Extraction**:
   - `data_extraction.py` fetches HTML content from given URLs, extracts the title and article text, and saves the data into text files in a directory named extracted_texts.

2. **Text Analysis**:
   - `data_analysis.py` reads the extracted text files and calculates various text metrics including positive/negative scores, polarity, subjectivity, sentence length, complex words, fog index, word count, syllables, personal pronouns, and average word length. 
   - The results are saved into a new Excel file named(Output data structure).

3. **Automation**:
   - `main.py` automates the execution of both scripts (`data_extraction.py` and `data_analysis.py`).



## Dependencies
- **requests**: For fetching HTML content from URLs.
- **beautifulsoup4**: For parsing HTML and extracting data.
- **nltk**: For natural language processing tasks.
- **textblob**: For sentiment analysis.
- **openpyxl**: For reading and writing Excel files.



### Installation

1. Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org).
2. Install the required dependencies using pip. Open a terminal or command prompt and run:
    ```
    pip install requests beautifulsoup4 nltk textblob openpyxl
    ```



### How to Run the Scripts

1. **Run the Main Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where `main.py`, `data_extraction.py`, and `data_analysis.py` are located.
   - Execute the main script:
     ```
     python main.py
     ```

2. **Expected Output**:
   - The script will create a unique directory (e.g., `extracted_texts`, `extracted_texts01`, etc.) and save text files for each URL.
   - It will also generate an Excel file (e.g., `Output data structure.xlsx`) containing the analyzed text metrics.



### Project Structure

project_directory/
│
├── main.py
├── data_extraction.py
├── data_analysis.py
├── Input.xlsx
└── words/
    ├── positive-words.txt
    └── negative-words.txt





### Example Commands

1. **Run Data Extraction Only**:
    ```
    python data_extraction.py
    ```

2. **Run Data Analysis Only**:
    ```
    python data_analysis.py
    ```

3. **Run the Entire Process**:
    ```
    python main.py
    ```


### Notes
- The script creates a unique directory for storing extracted text files and a uniquely named Excel file to avoid overwriting existing files.

---

This README file provides a comprehensive guide on setting up and running this project, ensuring that all necessary information and instructions are clear and easy to follow.
