import pandas as pd


def calculate_bmi(df):
    """
    Calculate the Body Mass Index (BMI) for each individual.

    Parameters:
    df (pd.DataFrame): DataFrame containing 'height' and 'weight' columns.

    Returns:
    pd.DataFrame: DataFrame with an additional 'BMI' column.
    """
    df = df.copy()
    df["BMI"] = df["weight"] / df["height"] ** 2   # BMI = weight (kg) / height (m)^2
    return df


def categorize_bmi(df):
    """
    Categorize the BMI into Underweight, Normal weight, Overweight, and Obese.

    Parameters:
    df (pd.DataFrame): DataFrame containing the 'BMI' column.

    Returns:
    pd.DataFrame: DataFrame with an additional 'BMI_category' column.
    """
    def category(bmi):
        if bmi < 18.5:
            return "Underweight"
        if bmi < 25:
            return "Normal weight"
        if bmi < 30:
            return "Overweight"
        return "Obese"

    df = df.copy()
    df["BMI_category"] = df["BMI"].apply(category)
    return df


# Example data
data = {
    'height': [1.60, 1.75, 1.82, 1.90, 1.65],
    'weight': [55, 80, 72, 90, 70]
}
df = pd.DataFrame(data)

# Apply the functions to the dataset
df = calculate_bmi(df)
df = categorize_bmi(df)
print(df)
