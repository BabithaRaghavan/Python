def group_by_owners(files):
    res_list = {}
    for key, value in sorted(files.items()):
        res_list[value].append(key)
        print(res_list)
    return(res_list)

if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))