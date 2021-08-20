from db_wrapper import DbWrapper

if __name__ == '__main__':
    answer = inpute('Are you sure to clear ALL data in DbWrapper?   [yes/no]')
    answer2 = inpute('Repeat are you sure to clear ALL data in DbWrapper? [yes/no]')
    if answer == 'yes' and answer2 == 'yes':
        db = DbWrapper()
        db.clear_db()
