import tqdm

def getAll(pyalexObj, verbous=True):
    count = pyalexObj.count()
    if verbous:
        if count/200/60<1:
            print(f"Fetching {count} objects. it may takes {round(count/200,2)} to {round(count/200*3,2)} seconds")
        else:
            print(f"Fetching {count} objects. it may takes {round(count/200/60,2)} to {round(count/200/60*3,2)} minutes")
    if count>10000:
        pager = pyalexObj.paginate(per_page=200, n_max=None)
    else:
        pager = pyalexObj.paginate(method="page",per_page=200)
    arr = []
    for page in tqdm.tqdm(pager,disable= not verbous):
        arr += page
    return arr

def flatten_pyalex_dict(dictionary, delimiter = "/", ignore=["abstract_inverted_index"]):
    for key in list(dictionary.keys()):
        if isinstance(dictionary[key], dict):
            if key in ignore:
                continue
            for subkey in dictionary[key]:
                dictionary[key + delimiter + subkey] = dictionary[key][subkey]
            del dictionary[key]
    return dictionary