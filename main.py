import pandas as pd
import os
API_KEY = os.getenv("API_KEY", "default-api-key")
def main():
    print("Hello from people-counter!")



def create_df(values: list):
    print(f"Creating DataFrame with values: {values}")
    print("API_KEY:", API_KEY)
    return pd.DataFrame(values, columns=["value"])


if __name__ == "__main__":
    main()
