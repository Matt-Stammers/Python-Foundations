# my version:

def get_grade(s1, s2, s3):
    values = (s1, s2, s3)
    val_sum = sum([v for v in values])
    score = val_sum/3
    if score >= 90:
    	return "A"
    if score >= 80:
    	return "B"
    elif score >= 70:
    	return "C"
    elif score >= 60:
    	return "D"
    else:
    	return "F"

# better version
      
 def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"
    
def get_grade(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')

# stores as a list

def get_grade(s1, s2, s3):
    mean = sum([s1,s2,s3])/3
    if mean>=90: return 'A'
    if mean>=80: return 'B'
    if mean>=70: return 'C'
    if mean>=60: return 'D'
    return 'F'
    
def get_grade(s1, s2, s3):
    grades = {"A": (90, 101), "B": (80, 90), "C": (70, 80), "D": (60, 70), "F": (0, 60)}
    mean = (s1 + s2 + s3) // 3

    for letter, minmax in grades.iteritems():
        min_, max_ = minmax
        if min_ <= mean < max_:
            return letter
