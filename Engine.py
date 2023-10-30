import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as sgt
from MLPipeine.ArchModel import Arch_Model

# Load data from an Excel file
raw_csv_data = pd.read_excel("Input/CallCenterData.xlsx")

# Create a copy of the data for processing
df_comp = raw_csv_data.copy()

# Set the date as the index for time series analysis
df_comp.set_index("month", inplace=True)

# Set the frequency of the data to monthly
df_comp = df_comp.asfreq('M')

# Visualize time series data for different categories
df_comp.Healthcare.plot(figsize=(20, 5), title="Healthcare")
# Save the plot as an image
plt.savefig("Output/" + "health.png")

# Repeat the visualization for other categories (Telecom, Banking, Technology, Insurance)

# Train-test split of the data
test_size = 22
df_train = df_comp[:-test_size]
df_test = df_comp[-test_size:]

# Calculate returns and volatility
df_train['returns'] = df_train.Banking.pct_change(1) * 100
df_train['sq_returns'] = df_train.returns.mul(df_train.returns)

# Plot returns and volatility
df_train.returns.plot(figsize=(20, 5))
plt.title("Returns", size=24)
# Save the plot as an image
plt.savefig("Output/" + "returns.png")

# Repeat the same for volatility

# Plot Partial Autocorrelation Function (PACF) of returns and volatility
sgt.plot_pacf(df_train.returns[1:], lags=40, alpha=0.05, zero=False, method=('ols'))
plt.title("PACF of Returns", size=20)
# Save the plot as an image
plt.savefig("Output/" + "PACFReturns.png")

# Repeat the same for ACF

# Perform an ARCH (Autoregressive Conditional Heteroskedasticity) model analysis on the data
Arch_Model(df_train, df_test)
