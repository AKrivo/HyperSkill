# write your code here
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)

general = pd.read_csv("text/general.csv")
prenatal = pd.read_csv("text/prenatal.csv")
sports = pd.read_csv("text/sports.csv")

# Part 2/5

names = []
for column in general.columns:
    names.append(column)

prenatal_c = prenatal.set_axis(names, axis=1)
sports_c = sports.set_axis(names, axis=1)

new_df = pd.concat([general, prenatal_c, sports_c], ignore_index=True).drop('Unnamed: 0', axis=1)

# Part 3/5

new_df.replace(['woman', 'female'], 'f', inplace=True)
new_df.replace(['man', 'male'], 'm', inplace=True)
new_df.dropna(axis=0, inplace=True, thresh=3)
new_df.loc[new_df.hospital == 'prenatal', 'gender'] = 'f'
new_df.fillna(0, inplace=True)

# print(new_df.shape)
# print(new_df.sample(n=20, random_state=30))

# Part 4/5

# Q1
ans_1 = new_df.hospital.value_counts().idxmax()
# Q2
ans_2 = new_df.loc[new_df.hospital == 'general', 'diagnosis'].value_counts("stomach").loc["stomach"].round(3)
# Q3
ans_3 = new_df.loc[new_df.hospital == 'sports', 'diagnosis'].value_counts("dislocation").loc["dislocation"].round(3)
# Q4
ans_4 = (new_df.loc[new_df.hospital == 'general', 'age'].median()
         - new_df.loc[new_df.hospital == 'sports', 'age'].median())
# Q5
ans_5_h = new_df.loc[new_df.blood_test == 't', 'hospital'].value_counts().idxmax()
ans_5_c = new_df.loc[new_df.blood_test == 't', 'hospital'].value_counts().max()

# print(f"The answer to the 1st question is {ans_1}")
# print(f"The answer to the 2st question is {ans_2}")
# print(f"The answer to the 3st question is {ans_3}")
# print(f"The answer to the 4st question is {int(ans_4)}")
# print(f"The answer to the 5st question is {ans_5_h}, {ans_5_c}  blood tests")

# Part 5/5

# Q1
# ["0-15", '15-35', '35-55', '55-70', '70-80']
age_bins = [0, 15, 35, 55, 70, 80]
title_1 = 'Age distribution'
xlabel_1 = 'Age'
ylabel_1 = 'Frequency'
age_hist = new_df.plot(
    y='age',
    kind='hist',
    bins=age_bins,
    title=title_1,
    xlabel=xlabel_1,
    ylabel=ylabel_1,
    edgecolor="white",
    xticks=age_bins)
plt.show()
print("The answer to the 1st question: 15-35")

# Q2

title_2 = 'Diagnosis'
diag_pie = (
    new_df
    .diagnosis
    .value_counts()
    .plot
        (
        y='diagnosis',
        kind='pie',
        title=title_2,
        autopct='%.1f%%'
    )
)
plt.show()
print('The answer to the 2nd question: pregnancy')

# Q3

data1 = new_df.loc[new_df.hospital == 'general', 'height']
data2 = new_df.loc[new_df.hospital == 'sports', 'height']
data3 = new_df.loc[new_df.hospital == 'prenatal', 'height']
data_list = [data1, data2, data3]
fig, axes = plt.subplots()
plt.violinplot(data_list)
axes.set_xticks((1, 2, 3))
axes.set_xticklabels(("general", "sports", 'prenatal'))
plt.show()

print("The answer to the 3nd question: It's because in sports hospital height is measured in feet")
