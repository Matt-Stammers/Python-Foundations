def get_size(w,h,d):
    area = (w*h*2) + (w*d*2) + (h*d*2)
    volume = w*h*d
    return [area, volume]
    
# or even more concise

def get_size(w, h, d):
    area = 2*(w*h + h*d + w*d)
    volume = w*h*d
    return [area, volume]
