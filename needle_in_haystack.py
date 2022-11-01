
haystack = ['dwane', 'richards', 'yessenia', 'perez', 'needle']


def contains(haystack, needle):

    # Does the haystack contain the needle?
    for item in haystack:
        if item != needle:
            print("your data don't live here")
        else:
            print(needle)


contains(haystack, 'needle')
