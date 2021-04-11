import arviz as az
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


filename = 'alaskaPopulation.csv'
df = pd.read_csv('{0}'.format(filename),index_col=None,skiprows=1)

# print(df.head())
print(df['Population'])

year = df['Year'].to_numpy(dtype='float32').reshape(-1)
population = df['Population'].str.replace(',','').astype(float).to_numpy(dtype='float32').reshape(-1)
voteMargin = df['Vote Margin (D - R)'].astype(float).to_numpy(dtype='float32').reshape(-1)
pop_white = df['White'].str.replace(',','').astype(float).to_numpy(dtype='float32').reshape(-1)

print(year)
print(voteMargin)

print(population.dtype)

fig, ax = plt.subplots(3,1)

np.isnan(population)


ax[0].plot(year[~np.isnan(population)],population[~np.isnan(population)],'o',label='population')
ax[0].legend()
ax[0].set_ylabel('Population')


ax[1].plot(year[~np.isnan(voteMargin)],voteMargin[~np.isnan(voteMargin)],'o',label='voteMargin')
ax[1].legend()
ax[1].set_ylabel('Vote Margin')

ax[2].plot(year[~np.isnan(pop_white)],pop_white[~np.isnan(pop_white)],'o',label='pop_white')
ax[2].legend()
ax[2].set_ylabel('Vote Margin')


ax[-1].set_xlabel('Time (years)')

plt.show()