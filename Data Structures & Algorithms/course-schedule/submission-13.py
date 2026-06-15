class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}

        for course, preReq in prerequisites:
            if course in courses:
                courses[course].append(preReq)
            else:
                courses[course] = [preReq]
            
            if preReq not in courses:
                courses[preReq] = []
            
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if courses[course] == []:
                return True
            
            visiting.add(course)
            for preReq in courses[course]:
                if not dfs(preReq):
                    return False
            visiting.remove(course)
            courses[course] = []
            return True
        
        for course in range(numCourses):
            if course in courses:
                if not dfs(course):
                    return False
        
        return True


        
        
        

