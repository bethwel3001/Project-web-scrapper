
import pandas as pd

def save_to_csv(data, filename):
    """Save the extracted data to a CSV file."""
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
