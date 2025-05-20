def categorize_transactions(df):
    def categorize(desc):
        desc = desc.lower()
        if "uber" in desc or "lyft" in desc:
            return "Transport"
        elif "starbucks" in desc or "coffee" in desc:
            return "Food"
        elif "rent" in desc:
            return "Housing"
        return "Other"

    df["category"] = df["description"].apply(categorize)
    return df
