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

print(new_df.index.to_list())
print(new_df.columns.to_list())

