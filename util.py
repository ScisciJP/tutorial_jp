from pyalex import Works

def citation_snowball(id):
    return id
    # pager = Works().filter(cited_by=id).paginate(per_page=20)
    # reference = []
    # for page in pager:
    #     if len(page)>0:
    #         reference += list(map(lambda x: x["id"], page))
    # reference
