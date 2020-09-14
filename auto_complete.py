#import re
import linecache
import json
from auto_complete_data import AutoCompleteDataClass
from json.decoder import JSONDecodeError

def change_to_auto_complete_data(c):
    with open("files.json", "r") as f:
        try:
            files = json.load(f)
        except JSONDecodeError:
            pass
        str_sen = linecache.getline(files[c[0]], c[1])
        # =================================================================ofset
        # offset=str_sen.index(prefix)#========================================
        res = AutoCompleteDataClass(str_sen, files[c[0]], c[1], 1, c[2])
        return res


def get_best_k_completions(prefix):
    autoComp = []
    file_name = prefix[0] + ".json"
    with open("json_files/" + file_name, "r") as f:
        cache_of_user = json.load(f)
    cache_of_user_dict = cache_of_user[0]
    comp = cache_of_user_dict.get(prefix)
    if comp:
        for c in comp:
            autoComp.append(change_to_auto_complete_data(c))
        if len(autoComp) == 5:
            return autoComp


