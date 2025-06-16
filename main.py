from data_collection import get_census_data
from model import train_model

def main():
    df = get_census_data()
    print("Data downloaded:", df.shape)
    model = train_model(df)

if __name__ == "__main__":
    main()