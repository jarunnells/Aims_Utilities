'''
import os
from shutil import copy2


class Bulk_Rename:
    """Bulk File Rename Class
    """

    def __init__(self):
        pass

    def print_instructions(self):
        """Print Initial Instructions
        :returns confirmed: boolean control variable -> True=continue, False=exit
        """
        print('REQUIRED FILE NAME FORMAT: ')
        print('  (photo_date)_(student_last-student_first)_(A_number).jpg')
        print('\n  [EXAMPLE]\n      1025_Aardvark-Arthur_A00123456.jpg')
        print()
        usr_prompt = input('All files named properly? [Y/N] >>: ')
        confirmed = True if usr_prompt.lower() == 'y' else False
        print()

        return confirmed

    def get_dir_list(self):
        """Prompt for directory and get file list
        :returns dir_list: directory file listing
        """
        # dir_path = './test_files'
        temp = './test_files'
        dir_path = input(f'Directory PATH {temp} >>: ')
        os.chdir(dir_path)

        return os.listdir()

    def create_temp_dir(self, temp_dir):
        """Create temp directory to store renamed files
        :param temp_dir: directory string passed for validation
        """
        if not os.path.isdir(temp_dir):
            os.makedirs(temp_dir)
        else:
            pass

    def copy_files(self, dir_list):
        """Copy orignial files into temp directory for renaming process
        :param dir_list: directory file list used in file copy process
        """
        index = None
        for i, f in enumerate(dir_list, start=1):
            if os.path.isfile(f):  # && !os.path.isdir(f):
                copy2(f, f'./temp/{f}')
            index = i
        print(f'Files moved: {index}')

    def rename_files(self, dir_list):
        """Rename files method
        :param dir_list: Temp directory file list used in bulk renaming process
        """
        macOS_JUNK = ".DS_Store"
        index = None
        for i, f in enumerate(dir_list, start=1):
            if os.path.isfile(macOS_JUNK):
                print(os.path(macOS_JUNK))
                # os.remove(macOS_JUNK)
            f_name, f_ext = os.path.splitext(f)
            print(f_name)
            try:
                pic_date, student, a_num = f_name.split('_')
            except ValueError as err:
                print(f"[ValueError] {err}")
            except Exception as exc:
                print(f"[Exception] {exc}")
                print(
                    f'pic_date: {pic_date}  student: {student}  a_num: {a_num}')
            pic_date = pic_date.strip().zfill(4)
            student = student.strip()
            a_num = a_num.strip()
            a_num_masked = a_num[5:].strip()

            try:
                f_name_NEW = f'{pic_date}_{student}_A-{a_num_masked}{f_ext}'
                os.rename(f, f_name_NEW)
                index = i
            except OSError as err:
                print(f'[ERROR] {err}')

        print(f'Files renamed: {index}')


def main():
    """Main Program
    """
    br = Bulk_Rename()

    confirmed = br.print_instructions()

    if confirmed:
        dir_list_orig = br.get_dir_list()
        temp_dir = './temp'
        temp_dir_FULL = None

        try:
            br.create_temp_dir(temp_dir)
            br.copy_files(dir_list_orig)
        except OSError as err:
            print(f'[ERROR] {err}')
        else:
            os.chdir(temp_dir)
        finally:
            temp_dir_FULL = os.getcwd()

        dir_list_temp = os.listdir() if os.getcwd() == temp_dir_FULL else None

        if dir_list_temp is not None:
            br.rename_files(dir_list_temp)

    else:
        print('Please apply proper naming convention before running this utility!')


if __name__ == '__main__':
    main()
'''
''''''
import os
from shutil import copy2
from datetime import datetime

class Bulk_Rename:
    """Bulk File Rename Class
    """

    def __init__(self):
        pass

    def print_instructions(self):
        """Print Initial Instructions
        :returns confirmed: boolean control variable -> True=continue, False=exit
        """
        print('REQUIRED FILE NAME FORMAT: ')
        print('  (photo_date)_(student_last-student_first)_(A_number).jpg')
        print('\n  [EXAMPLE]\n      1025_Aardvark-Arthur_A00123456.jpg')
        print()
        usr_prompt = input('All files named properly? [Y/N] >>: ')
        confirmed = True if usr_prompt.lower() == 'y' else False
        print()

        return confirmed

    def get_dir_list(self):
        """Prompt for directory and get file list
        :returns dir_list: directory file listing
        """
        # dir_path = './test_files'
        temp = './test_files'
        dir_path = input(f'Directory PATH {temp} >>: ')
        os.chdir(dir_path)

        return os.listdir()

    def create_temp_dir(self, temp_dir):
        """Create temp directory to store renamed files
        :param temp_dir: directory string passed for validation
        """
        if not os.path.isdir(temp_dir):
            os.makedirs(temp_dir)
        else:
            pass

    def copy_files(self, dir_list, temp_dir):
        """Copy orignial files into temp directory for renaming process
        :param dir_list: directory file list used in file copy process
        """
        count = 0
        for i, f in enumerate(dir_list, start=1):
            if os.path.isfile(f):  # && !os.path.isdir(f):
                # copy2(f, f'./temp/{f}')
                copy2(f, f'{temp_dir}{f}')
                count += 1
        print(f'Files moved: {count}')

    def rename_files(self, dir_list):
        """Rename files method
        :param dir_list: Temp directory file list used in bulk renaming process
        """
        count = 0
        for i, f in enumerate(dir_list, start=1):
            f_name, f_ext = os.path.splitext(f)
            pic_date, student, a_num = f_name.split('_')
            pic_date = pic_date.strip().zfill(4)
            student = student.strip()
            a_num = a_num.strip()
            a_num_masked = a_num[5:].strip()

            try:
                f_name_NEW = f'{pic_date}_{student}_A-{a_num_masked}{f_ext}'
                os.rename(f, f_name_NEW)
                count += 1
            except OSError as err:
                print(f'[ERROR] {err}')

        print(f'Files renamed: {count}')


def main():
    """Main Program
    """
    br = Bulk_Rename()

    confirmed = br.print_instructions()

    if confirmed:
        dir_list_orig = br.get_dir_list()
        # temp_dir = None
        temp_dir_FULL = None
        timestamp = f"[{'%m'}{'%d'}_{'%H'}{'%M'}{'%f'}]"

        try:
            br.create_temp_dir(temp_dir := f"./temp{datetime.now().strftime(timestamp)}/")
            br.copy_files(dir_list_orig, temp_dir)
        except OSError as err:
            print(f'[ERROR] {err}')
        else:
            os.chdir(temp_dir)
        finally:
            temp_dir_FULL = os.getcwd()

        dir_list_temp = os.listdir() if os.getcwd() == temp_dir_FULL else None

        if dir_list_temp is not None:
            br.rename_files(dir_list_temp)

    else:
        print('Please apply proper naming convention before running this \
               utility!')


if __name__ == '__main__':
    main()

''''''
