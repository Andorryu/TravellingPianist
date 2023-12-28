import os

songs_dict = {3: 'Gimme_Gimme_Gimme_A_Man_After_Midnight.mscz.mxl'}


mypath = "/home/will/Downloads"

files = os.listdir(mypath)

for file_name in files:
    if len(songs_dict) == 0:
        songs_dict[0] = file_name
    elif file_name in songs_dict.values():
        pass
    else:
        songs_dict[list(songs_dict.keys())[-1]+1] = file_name


print(songs_dict)
print("\n\n")


def filter_dictionary(original_dict, search_string):
    result_dict = {}

    for key, value in original_dict.items():
        if search_string.lower() in value.lower():
            result_dict[key] = value
    
    return result_dict

result = filter_dictionary(songs_dict, "hotline")

print(result)