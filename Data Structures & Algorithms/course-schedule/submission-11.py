class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i : [] for i in range(numCourses)}

        for course, preReq in prerequisites:
            courses[course].append(preReq)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                #cycle!
                return False
            if courses[course] == []:
                return True
            
            visiting.add(course)
            for preReq in courses[course]:
                if not dfs(preReq):
                    return False
            visiting.remove(course)
            ## saying that this course is valid for future needs
            courses[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        
        
        

