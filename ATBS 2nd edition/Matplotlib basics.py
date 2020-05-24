# I'm playing with this to learn about the use of matplotlib
# Copied from https://www.reddit.com/r/learnpython/comments/ep2xb8/rave_finally_able_to_prove_the_value_of_python/

# importing libraries
import openpyxl
import os
import matplotlib.pyplot as plt

# File path
path = FILE_PATH

# cells containing desired data in the workbooks
cells = ['G17', 'G19', 'G21',
         'K17', 'K19', 'K21',
         'O17', 'O19', 'O21',
         'S17', 'S19', 'S21',
         'W17', 'W19', 'W21', ]

# lists for plotting etc.
dates = []
weights = []

os.chdir(path)

# iterate through files.
for file in os.listdir(path):

    # avoid old file format because only interested in newer files
    if not (file[-3:]) == "xls":

        # read workbook and sheet
        workbook = openpyxl.load_workbook(file, data_only=True)
        test_sheet = workbook['Tests']

        # iterate over predefined cells from list
        for cell in cells:

            # get date of result. The date is in row 10 of same column as result
            cast_cell = test_sheet[str(cell[0] + "10")].value

            # and get the actual result
            cell_val = test_sheet[cell].value

            # if result is not None and year is recent add to result lists
            # cast_cell is a datetime object after reading the cell value to it
            # so we can use .year directly from that object
            if cell_val is not None and cast_cell.year > 2000:
                # appending to the lists
                dates.append(cast_cell)
                weights.append(cell_val)

# print basic stats
print(len(weights), "results found. Max:", max(weights), ", Min:", min(weights))
print("Average:", round(sum(weights) / len(weights), 2))

# data specific for the intercalibration
# Original data replaced with random data as I do not have permission to share it

our_val = [564.7, 572.7, 567.3, 561.3, 565.7, 564.1, 582.3, 574.3, 576.9, 565.2, 576.9]

years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2019, 2019, 2019]

avg_vals = [580.2, 578.3, 584.6, 587.1, 581.9, 578.7, 586.0, 580.5, 580.5, 580.5, 580.5]

# plot data
plt.figure(figsize=(25, 12))
plt.suptitle("Weight histogram")

# histogram
plt.subplot(131)
plt.title("Histogram, weights")
plt.hist(weights, bins=20)

# weights over time
plt.subplot(132)
plt.title("Weights over time")
plt.scatter(dates, weights)

# plotting us vs the intercalibration
plt.subplot(133)
plt.title("Us (Red) vs. Intercalibration (Blue)")
plt.scatter(years, our_val, c='red')
plt.scatter(years, avg_vals, c='blue')
plt.show()
