# Data Preprocessing Techniques

This repository provides a comprehensive collection of Python scripts and examples demonstrating essential data preprocessing techniques used in machine learning and data analysis. The project covers data cleaning, transformation, reduction, and integration methods, implemented using popular libraries like Pandas and Scikit-learn.

## Features

The repository includes implementations for the following data preprocessing techniques:

- **Data Cleaning**: Handling missing values, noisy data, and outliers.
- **Data Transformation & Discretization**: Normalization techniques including Min-Max scaling and Z-score standardization.
- **Data Reduction**: Dimensionality reduction using Principal Component Analysis (PCA) and data sampling methods.
- **Data Integration**: Merging and combining datasets from multiple sources.

## Project Structure

```
Data-Preprocessing-Techniques/
├── Full Python Notebook Data Preprocessing Techniques.py  # Complete demonstration of all techniques
├── README.md
├── Data Cleaning/
│   ├── Data_cleaning.py
│   └── sample_dirty_dataset.csv
├── Data Integration/
│   ├── Data_integration.py
│   └── Dataset_for_data_integration.py
├── Data Reduction/
│   ├── Data_reduction.py
│   └── Dataset_for_data_reduction.py
└── Data Transformation & Discretization/
    ├── Data_Normalization.py
    └── sample_dataset.csv
```

## Requirements

To run the scripts in this repository, you need the following Python libraries:

- pandas
- numpy
- scikit-learn

You can install them using pip:

```bash
pip install pandas numpy scikit-learn
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Man0dya/Data-Preprocessing-Techniques.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Data-Preprocessing-Techniques
   ```

3. Run the full notebook for a complete walkthrough:
   ```bash
   python "Full Python Notebook Data Preprocessing Techniques.py"
   ```

4. Or run individual scripts in their respective folders:
   - Data Cleaning: `python Data Cleaning/Data_cleaning.py`
   - Data Integration: `python Data Integration/Data_integration.py`
   - Data Reduction: `python Data Reduction/Data_reduction.py`
   - Data Transformation: `python "Data Transformation & Discretization/Data_Normalization.py"`

Each script includes sample datasets and demonstrates the preprocessing techniques with example outputs.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.