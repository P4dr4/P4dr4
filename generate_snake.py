import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

# Generate mock contribution data
dates = pd.date_range(end=datetime.today(), periods=365).to_pydatetime().tolist()
contributions = np.random.randint(0, 5, size=(365))

data = pd.DataFrame({
    'date': dates,
    'contributions': contributions
})

# Create the directory if it doesn't exist
output_dir = 'dist'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a snake-like plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(data['date'], data['contributions'], lw=2)

ax.fill_between(data['date'], data['contributions'], alpha=0.3)
ax.set(xlim=[dates[0], dates[-1]], ylim=[0, 4])
ax.grid(True)

# Save the plot
plt.savefig(os.path.join(output_dir, 'snake.svg'), format='svg')
