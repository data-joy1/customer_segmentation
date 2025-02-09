import pandas as pd

def load_data():
    df = pd.read_csv(r"D:\projects for cv\customer_segmentation\data\Mall_Customers.csv")
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())
