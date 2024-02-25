from pyalex import Works, Authors
import tqdm
import pandas as pd

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
    pager = pyalexObj.paginate(method="page",per_page=200)
    arr = []
    for page in tqdm.tqdm(pager):
        arr += page
    return arr

# obj = Works().filter(institution={"id":"https://openalex.org/I74801974"}, publication_year=">2020",cited_by_count=">10",primary_topic={"field":{"id":11}}).sample(500,seed=42).select(["cited_by_count"])
# getAll(obj)