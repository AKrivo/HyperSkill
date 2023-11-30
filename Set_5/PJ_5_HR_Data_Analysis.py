import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
            'B_office_data.xml' not in os.listdir('../Data') and
            'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    # write your code here

# Part 1/5
A_df = pd.read_xml('../Data/A_office_data.xml')
B_df = pd.read_xml('../Data/B_office_data.xml')
hr_df = pd.read_xml('../Data/hr_data.xml')


def newIndex(DataFrame, column, pref):
    """ DataFrame is df to modify
       column is target column
       pref is prefix """

    dataframelist = DataFrame[column].tolist()
    res = []
    for i in dataframelist:
        res.append(pref + str(i))

    return pd.Series(res)


A_df = A_df.set_index(newIndex(A_df, "employee_office_id", "A"))
B_df = B_df.set_index(newIndex(B_df, "employee_office_id", "B"))
hr_df.set_index("employee_id", drop=False, inplace=True)

# Part 2/5
AB_df = pd.concat([A_df, B_df])
new_df = AB_df.merge(hr_df, left_index=True,
                     right_index=True, indicator=True).drop(["employee_office_id",
                                                             "employee_id", "_merge"], axis=1)


new_df.sort_index(inplace=True)
# Part 3/5

x = new_df.sort_values(by='average_monthly_hours', ascending=False).head(10)['Department'].to_list()
y = new_df.query("Department == 'IT' & salary == 'low'")['number_project'].sum()
z = new_df.loc[['A4', 'B7064', 'A3033'], ['last_evaluation', 'satisfaction_level']].values.tolist()


# print(x)
# print(y)
# print(z)

# Part 4/5

def count_bigger_5(employee_project_counts):
    return sum(employee_project_counts > 5)


# x = new_df[new_df.number_project > 5].number_project.count()
# x = new_df.agg({'number_project': ['mean', count_bigger_5]}).round(2)

x = (
    new_df.groupby('left')
    .agg(
        {
            'number_project': ['median', count_bigger_5],
            'time_spend_company': ['mean', 'median'],
            'Work_accident': ['mean'],
            'last_evaluation': ['mean', 'std']
        }
    )
    .round(2)
    .to_dict()
)

# Part 5/5

table = new_df.pivot_table(index="Department", columns=["left", "salary"], values="average_monthly_hours", aggfunc='median').round(2)
x = table.where((table[(0, 'high')] < table[(0, 'medium')]) | (table[(1, 'low')] < table[(1, 'high')])).dropna().to_dict()

table2 = new_df.pivot_table(index="time_spend_company", columns="promotion_last_5years", values=['satisfaction_level', 'last_evaluation'], aggfunc=['max', 'mean', 'min']).round(2)
z = table2.where(table2['mean', 'last_evaluation', 0] > table2['mean', 'last_evaluation', 1]).dropna().to_dict()

print(x)
print(z)
