from server import mcp
from tools.parquet_tools import summarize_parquet_file
from tools.csv_tools import summarize_csv_file

def main():
    print("Hello from mix-server!")


if __name__ == "__main__":
    mcp.run()
