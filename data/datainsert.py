import os
import csv
from azure.data.tables import TableServiceClient, TableEntity
from dotenv import load_dotenv

load_dotenv()  

# CONFIG
AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
TABLE_NAME = "ResearchAIQnA"
CSV_FILE_PATH = "data/researchai.csv"


def upload_csv_to_table():
    try:
        # Create Table service client
        table_service = TableServiceClient.from_connection_string(
            conn_str=AZURE_CONNECTION_STRING
        )

        # Create table if it does not exist
        table_client = table_service.create_table_if_not_exists(
            table_name=TABLE_NAME
        )

        # Read CSV and insert rows
        with open(CSV_FILE_PATH, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                entity = TableEntity(
                    PartitionKey="ResearchAI",
                    RowKey=row["id"],
                    question=row["question"],
                    answer=row["answer"]
                )

                table_client.upsert_entity(entity=entity)

        print("CSV data uploaded successfully to Azure Table Storage")

    except Exception as e:
        print("Upload failed:", e)


if __name__ == "__main__":
    upload_csv_to_table()
