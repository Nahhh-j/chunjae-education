'''
[Question 3] = (30점)
<외톨이 고르기>
구슬치기 게임을 하려면 두 사람이 필요하다.
하나의 외톨이(깍두기)를 제외한 모든 사람은 자기만의 짝이 하나 더 유일하게 존재한다.
번호는 자연수라고 가정하며, 외톨이는 1명만 유일하게 존재한다고 가정한다.
아래의 nums1 예제에서 1, 2, 4, 5번은 각각 자신의 파트너가 존재하나, 3번만은 파트너가 없는 외톨이다.
외톨이를 구하여 반환하는 함수를 완성하고, 외톨이를 출력해보시오.
'''

nums1 = [2, 1, 3, 1, 4, 5, 2, 5, 4]
nums2 = [7, 3, 26, 13, 1, 3, 77, 7, 13, 1, 26]

def find_solo(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num, freq in count.items():
        if freq == 1:
            return num

print(find_solo(nums1))  # 3 출력
print(find_solo(nums2))  # 77 출력