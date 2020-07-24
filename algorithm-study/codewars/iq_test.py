def iq_test(nums):
    sol = [int(i) % 2 for i in nums.split(" ")]
    if sum(sol) == 1:
        return sol.index(1) + 1
    else:
        return sol.index(0) + 1

print(iq_test("2 4 7 8 10"))