import pandas as pd

df = pd.read_csv("brown_dwarfs.csv")
df = df[df['mass'].notna()]
df = df[df['radius'].notna()]

mass = df['mass'].tolist()
radius = df['radius'].tolist()

mass= df['mass'].astype(float)
radius = df['radius'].astype(float)

df.dtypes

solar_mass = mass*0.000954588
solar_radius = radius*0.102763

df = pd.DataFrame(list(zip(mass,radius)), columns=['Mass','Radius'])
df.to_csv('unit.csv')