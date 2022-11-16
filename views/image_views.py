def adminfix(request, albumid=None, photoid=None, deletetype=None):
    album =  models.AlbumModel.objects.get(id=albumid)
    photos = models.PhotoModel.objects.filter(pablum__id=albumid).order_by('-id')
    totalphoto = len(photos)

  i = 0
for upfile in files:
    if upfile != '' and descs[i]!='':
        fs = FileSystemStorage()
        filename = fs.save(upfile.name,upfile)
        unit = models.PhotoModel.objects.create(palbum=album,psubject=descs[i],purl=upfile)
        unit.save()
    i+=1
return redirect('/adminfix/'+str(album.id)+'/')




