def get_grade(s1, s2, s3):
    nums = (s1, s2, s3)
    average = sum(nums)/len(nums)
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
