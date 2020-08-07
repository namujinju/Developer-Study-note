# Level 2 카펫

def solution(brown, yellow):
    a = int((brown/2-2+((brown/2-2)**2-4*yellow)**0.5)/2+2)
    b = int((brown/2-2-((brown/2-2)**2-4*yellow)**0.5)/2+2)
    return [a, b]


brown, yellow = 10, 2
print(solution(brown, yellow))
