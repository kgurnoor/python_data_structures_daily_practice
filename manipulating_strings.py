def get_data(aTuple):
    nums=()
    words=()
    for t in aTuple:
        nums=nums+(t[0],)
        if t[1] not in words:
            words= words+(t[1],)
    min_n=min(nums)
    max_n=max(nums)
    unique_words=len(words)
    return(min_n,max_n,unique_words)


tswift=((2014,"katy"),(2009,"harry"),(2012,"jentzen"),(2010,"jake"),(2008,"joe"))
(min_year,max_year,num_people)=get_data(tswift)
print("From", min_year,"to", max_year,"Taylor Swift wrote songs about",num_people,"people!")
