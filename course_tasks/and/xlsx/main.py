import os
import openpyxl as xl


def get_filepaths(filename):
    if filename.is_dir():
        for item in os.scandir(filename):
            get_filepaths(item)
    else:
        return filename.path


def get_gender(file):
    _sex = []
    for sheet in file.sheetnames[1:]:
        data = file[sheet]['A5'].value
        if data is not None:
            _sex.append(data)
    return _sex


def get_arr(arr, el):
    count = 0
    for item in arr:
        if item == el:
            count += 1
    return count


def count_genders(big_list):
    male = 0
    female = 0
    for mini_list in big_list:
        for el in mini_list:
            if el == 'Male':
                male += 1
            elif el == 'Female':
                female += 1
    return {'Male': male, 'Female': female}


if __name__ == "__main__":
    dir_path = '/home/lab_andrew/Desktop/personal_data/programming_etc/repositories/easy_it/course_tasks/and/xlsx/output'
    some_list = [get_filepaths(i) for i in os.scandir(dir_path) if get_filepaths(i) if get_filepaths(i) is not None]
    some_list = [i for i in some_list if i is not None]
    some_list = [i for i in some_list if i.endswith('xlsx')]
    sex = []
    for filename in some_list:
        wb = xl.load_workbook(filename)
        sex.append(get_gender(wb))

    print(count_genders(sex))


