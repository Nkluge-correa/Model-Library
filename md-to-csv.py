import argparse
import os
import pandas as pd

def recreate_db(markdown_dir, output_csv):
    """
    Recreate the CSV file from the Markdown files.
    """
    markdown_dir = "submissions"

    # Create an empty DataFrame with the same column names
    columns = ["model_name_string", "model_name_url", "model_size_string", "dataset", "data_type",
           "research_field", "risks_and_limitations", "risk_types", "publication_date",
           "organization_and_url", "institution_type", "country", "license", "paper_name_url",
           "model_description", "organization_info"]

    new_db = pd.DataFrame(columns=columns)

    # Loop through each Markdown file in the directory
    for filename in os.listdir(markdown_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(markdown_dir, filename)

            lines = []
            # Read the contents of the Markdown file
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            data = {}
            for line in lines:
                if line.startswith('# '):
                    data["model_name_string"] = line[2:].strip()
                elif line.startswith('- Name:'):
                    data["model_name_url"] = line[8:].strip()
                elif line.startswith('- Model Size:'):
                    data["model_size_string"] = line[14:].strip()
                elif line.startswith('- Dataset:'):
                    data["dataset"] = line[11:].strip()
                elif line.startswith('- Input/Output Format:'):
                    data["data_type"] = line[22:].strip()
                elif line.startswith('- Research Field:'):
                    data["research_field"] = line[18:].strip()
                elif line.startswith('- Contains an Impact Assessment:'):
                    data["risks_and_limitations"] = line[33:].strip()
                elif line.startswith('- Associated Risks:'):
                    data["risk_types"] = line[20:].strip()
                elif line.startswith('- Date of Publication:'):
                    data["publication_date"] = line[22:].strip()
                elif line.startswith('- Organization:'):
                    data["organization_and_url"] = line[15:].strip()
                elif line.startswith('- Institution Type:'):
                    data["institution_type"] = line[19:].strip()
                elif line.startswith('- Country/Origin:'):
                    data["country"] = line[17:].strip()
                elif line.startswith('- License:'):
                    data["license"] = line[10:].strip()
                elif line.startswith('- Publication:'):
                    data["paper_name_url"] = line[14:].strip()
                elif line.startswith('## Description'):
                    model_description = ''
                    for next_line in lines[lines.index(line) + 1:]:
                        if next_line.startswith('##'):
                            break
                        model_description += next_line
                    data["model_description"] = model_description.strip()

                elif line.startswith('## Organization'):
                    organization_info = ''
                    for next_line in lines[lines.index(line) + 1:]:
                        if next_line.startswith('##'):
                            break
                        organization_info += next_line
                    data["organization_info"] = organization_info.strip()
                
            data

            # Convert the dictionary into a DataFrame
            df = pd.DataFrame(data, index=[0])

            # Concatenate the DataFrame to the result DataFrame
            new_db = pd.concat([new_db, df], ignore_index=True)

    # Save the result DataFrame as a CSV file
    new_db.to_csv(output_csv, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Recreate CSV file from Markdown files.')
    parser.add_argument('markdown_dir', help='Directory containing Markdown files')
    parser.add_argument('output_csv', help='Path to the output CSV file')

    args = parser.parse_args()

    recreate_db(args.markdown_dir, args.output_csv)

    print('Done!')

# How to run:
# python md-to-csv.py submissions data/data.csv