class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()

        for e in emails:
            i, local = 0, ""
            while e[i] not in ["+", "@"]:
                if e[i] != ".":
                    local += e[i]
                i += 1
            
            while e[i] != "@":
                i += 1
            
            local += e[i:]
            uniqueEmails.add(local)
        
        return len(uniqueEmails)

            
                
                
                