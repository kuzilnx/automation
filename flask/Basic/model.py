# create a function that check if data.db exists and if it does, it will append to it some data, and if it does not, it will return error

def write_to_file(file_name, data):
    try:
        with open(file_name,'w') as f:
            f.write(data)
        return 0

    except:
        return 1


if __name__ == "__main__":
    write_to_file()

