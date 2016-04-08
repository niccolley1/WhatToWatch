from SupportClasses.csv_files import open_csv_return_giant_list
from Movie import Movie

class ProcessData():

    def __init__(self):
        # Setting up dirs for future reference
        self._movie_data_dir = '/Users/Nic/TIY/W2/WhatToWatch/Data/MovieLensData/ml100k'
        self._saved_classes_dir = '/Users/Nic/TIY/W2/WhatToWatch/Data/SavedClassesData'
        self._movie_data = 'u.item'

        self._enconding = 'latin_1'

    """Takes the file name and feeds the information
        into the appropriate class"""
    def read_file(self, a_file, a_class):
        temp_name = self._movie_data_dir+'/'+a_file
        temp_list = []
        #print(temp_name)
        a = open_csv_return_giant_list(temp_name, self._enconding)
        #print(len(a))
        for row in a:
            #print(row[0])
            a = self.create_initial_instances(row, a_class)
            temp_list.append(a)
        return temp_list

    """Takes the data that is read from file and creates
        instances of the data."""
    def create_initial_instances(self, a_row, a_class):
        temp_name = 'movie_id_{}'.format(a_row[0])
        return a_class(a_row)


if __name__ == '__main__':
    f = ProcessData()
    #f.read_file('u.item', Movie)

    #f.main()
