from pyalex import Works
import tqdm


def citation_snowball(id):
    return id
    # pager = Works().filter(cited_by=id).paginate(per_page=20)
    # reference = []
    # for page in pager:
    #     if len(page)>0:
    #         reference += list(map(lambda x: x["id"], page))
    # reference

def getAll(pyalexObj):
    # pyalexObj.count()
    pager = pyalexObj.paginate(per_page=200)
    arr = []
    for page in tqdm.tqdm(pager):
        arr += page
    return arr