import csv
import glob
import os

# get the current file location
current_project_directory = os.getcwd()

def merge_csv():

  """
  This Function is used to get all the csv files in input_file_location and then generate a unified csv file
  """

  # location of the input csv files
  input_file_location = current_project_directory + '\\input_files\\'

  # location for unified csv files
  output_file_location = current_project_directory + '\\output_files\\'

  # get all the .csv file in all_csv_files list
  all_csv_files = [i for i in glob.glob(input_file_location + '*.csv')]

  # get all the unique headers name by iterating through all the csv files and appending it to unique_headers_name list
  unique_headers_name = []

  # below for loop iterate through all the csv files and append the unique headers in unique_headers_name list
  for filename in all_csv_files:
    with open(filename, "r", newline="") as f_in:
      reader = csv.reader(f_in)
      headers = next(reader)
      for h in headers:
        if h not in unique_headers_name:
          unique_headers_name.append(h)


  # write to output csv file
  with open(output_file_location + 'output.csv', "w", newline="") as f_out:
    writer = csv.DictWriter(f_out, fieldnames=unique_headers_name)
    writer.writeheader()
    for filename in all_csv_files:
      with open(filename, "r", newline="") as f_in:
        reader = csv.DictReader(f_in)

        for line in reader:
          writer.writerow(line)

if __name__ == '__main__':
  merge_csv()