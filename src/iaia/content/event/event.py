

def moveContentToTop(item, event):

    folder = item.getParentNode()
    folder.moveObjectsToTop(item.id)
    print item.id
