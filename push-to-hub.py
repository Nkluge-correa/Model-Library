import argparse
import pandas as pd
from datasets import DatasetDict, Dataset

def push_to_hub(token, csv_file):
    db = pd.read_csv(csv_file)
    dataset = Dataset.from_pandas(db)

    ddict = DatasetDict({
        "main": dataset,
    })

    ddict.push_to_hub("nicholasKluge/model-library", token=token)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Push dataset to Hugging Face Model Hub.')
    parser.add_argument('token', default=None, help='Hugging Face API token')
    parser.add_argument('csv_file', help='Path to the CSV file')

    args = parser.parse_args()

    push_to_hub(args.token, args.csv_file)

    print('Done!')

# How to run:
# python push-to-hub.py "token_here" "data/data.csv"
