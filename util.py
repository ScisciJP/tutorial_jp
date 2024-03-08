import tqdm

def getAll(pyalexObj, verbous=True):
    count = pyalexObj.count()
    print(f"Fetching {count} objects. it may takes {round(count/200/60*3,2)} minutes")
    if count>10000:
        pager = pyalexObj.paginate(per_page=200, n_max=None)
    else:
        pager = pyalexObj.paginate(method="page",per_page=200)
    arr = []
    for page in tqdm.tqdm(pager,disable= not verbous):
        arr += page
    return arr