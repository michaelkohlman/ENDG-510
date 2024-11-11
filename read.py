import pandas as pd # in case of error, install pnadas using: pip install pandas
import numpy as np # for random number generation

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

df_new_entries = pd.DataFrame(columns=['Temp', 'Humd', 'Label']) # set up data frame for new entries

temperature = 25 # start at a reasonable room temperature (25 celcius)
humidity = 15 # start at a reasonable room humidity (15%)
label = 0 # label of false data is to be 0.

iterations = 50 # number of false entries to be created

for i in range(iterations): # for each new entry
    temp_noise = np.random.uniform(-0.02*iterations,0.02*iterations)  # adding some random noise to each value to simulate regular fluctations
    humid_noise = np.random.uniform(-0.004*iterations,0.004*iterations)

    temperature = round((temperature - 0.1*iterations + temp_noise),2) # repeatedly decrease the recorded temperature, adding noise
    humidity = round((humidity + 0.02*iterations + humid_noise),2) # reportedly increase the reported humidity, adding noise

    new_data = {'Temp': temperature, 'Humd': humidity, 'Label': label} # compile new entry
    
    df = df.append(new_data, ignore_index=True) # add new entry to the dataframe

# Step 3: Save the DataFrame to a new CSV file
df.to_csv("data_virus.csv", index=False)

