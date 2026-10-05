import pandas as pd

def extract_csv(file_path):
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    file_path = "./data/raw/online_retail.csv"
    df = extract_csv(file_path)

    print("عدد الصفوف :",len(df))
    print("عدد الاعمدة :",len(df.columns))
    print("اسماء الاعمدة :")
    print(df.columns.tolist())