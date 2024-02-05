import os
import argparse
import pandas as pd

def generate_markdown(csv_file):
    """
    Generate the Markdown files from the CSV file.
    """
    db = pd.read_csv(csv_file)

    for model in db.model_name_string.tolist():
        info = db.iloc[int(db[db.model_name_string == model].index.values)]

        model_details = f"""# {info.model_name_string}

## Model Details

- Name: {info.model_name_url}
- Model Size: {info.model_size_string}
- Dataset: {info.dataset}
- Input/Output Format: {info.data_type}
- Research Field: {info.research_field}
- Contains an Impact Assessment: {info.risks_and_limitations}
- Associated Risks: {info.risk_types}
- Date of Publication: {info.publication_date}
- Organization: {info.organization_and_url}
- Country/Origin: {info.country}
- License: {info.license}
- Publication: {info.paper_name_url}

## Description

{info.model_description}

## Organization

{info.organization_info}
"""

        output_dir = 'submissions'
        os.makedirs(output_dir, exist_ok=True)

        with open(os.path.join(output_dir, f'{model}.md'), 'w') as f:
            f.write(model_details)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Markdown files from a CSV file.')
    parser.add_argument('csv_file', help='Path to the input CSV file')

    args = parser.parse_args()

    generate_markdown(args.csv_file)

    print('Done!')

# How to run:
# python csv-to-md.py data/data.csv
