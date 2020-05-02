# n=int(input())
# row=[]
# while 1:
#     try:
#         row.append(input())
#     else:
#         break

def findMedianSortedArrays(nums1, nums2):
    nums1[len(nums1):]=nums2
    nums1.sort()
    if len(nums1)%2==0:
        mid=len(nums1)//2
        return (nums1[mid]+nums1[mid-1])/2
    else:
        mid=len(nums1)//2
        return nums1[mid]/1
      
    # ans=[]
    # nums1.sort()
    # nums2.sort()
    # n1=0
    # n2=0
    # while n1<len(nums1) and n2<len(nums2):
    #     if nums1[n1]<nums2[n2]:
    #         ans.append(nums1[n1])
    #         n1+=1
    #     else:
    #         ans.append(nums2[n2])
    #         n2+=1
    
    # if len(ans)%2==0:
    #     mid=len(ans)//2
    #     return (ans[mid]+ans[mid-1])/2
    # else:
    #     mid=len(ans)//2
    #     return ans[mid+1]/1

nums1 = [1, 3]
nums2 = [2]

print(findMedianSortedArrays(nums1, nums2))