class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        index = [0,0]
        for student in students:
            index[student] += 1
        k = 0
        while k<len(sandwiches):
            if index[sandwiches[k]]>0:
                index[sandwiches[k]] -= 1
            else:
                break
            k += 1
        return len(sandwiches)-k
