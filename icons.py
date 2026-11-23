from PIL import Image, ImageDraw
def icon(size, pad_ratio, path):
    im = Image.new('RGB', (size, size), (16,19,24))
    d = ImageDraw.Draw(im)
    s = size*(1-2*pad_ratio); o = size*pad_ratio
    def R(x0,y0,x1,y1,c,r):
        d.rounded_rectangle([o+x0*s,o+y0*s,o+x1*s,o+y1*s], radius=r*s, fill=c)
    amber=(255,176,32)
    R(.12,.47,.88,.53,amber,.02)          # barra
    R(.20,.28,.30,.72,amber,.03)          # discos grandes
    R(.70,.28,.80,.72,amber,.03)
    R(.08,.36,.17,.64,amber,.03)          # discos pequeños
    R(.83,.36,.92,.64,amber,.03)
    im.save(path)
icon(192,.10,'docs/icons/icon-192.png')
icon(512,.10,'docs/icons/icon-512.png')
icon(512,.20,'docs/icons/icon-maskable-512.png')
