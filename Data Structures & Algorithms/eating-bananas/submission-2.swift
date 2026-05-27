class Solution {
    func minEatingSpeed(_ piles: [Int], _ h: Int) -> Int {
        var maxBananas = 0
        for i in piles {
            if i > maxBananas {
                maxBananas = i
            }
        }

        var left = 1
        var mid: Int = 0
        
        while left < maxBananas {
            mid = (left + maxBananas) / 2

            if canFinish(piles, mid, h) == true {
                maxBananas = mid
            } else {
                left = mid + 1
            }
        }

        return left
    }

    func canFinish(_ piles: [Int], _ eatSpeed: Int, _ hours: Int) -> Bool {
        var hoursToFinish = 0
        for i in piles {
            hoursToFinish += (i / eatSpeed)
            if i % eatSpeed > 0 {
                hoursToFinish += 1
            }
        }

        if hoursToFinish > hours {
            return false
        } else {
            return true
        }
    }

}


//Koko Eating bananas
// so if I'm understanding correctly - my goal is to find the minimum bananas per hour (eating rate) that will allow me to eat all the piles within h hours
// clarifying questions - can I guarantee that h will be at least piles.count ? because I know that even if my n (bananas per hour) exceeds a given pile's bananas - I cannot move on - meaning that at minimum it'll take piles.count hours to finish any given piles
// will each banana pile have at least 0 bananans - I'm gonna assume a negative banana pile can't exist

//so I think my approach here would be to sort the piles in ascending order and then do a binary search (kinda of) to generate some number that'll fulfill the requirement

//my algorithem will kinda look like this:

// piles.sort
// eatingSpeed = piles[piles.count / 2] / h

// then i would need to run a checker to see if that fulfills the requirement, and after that i would keep evaluating to the left or the right until i find the min number

// i think here my runtime complexity would be O(logN) for the sorting, and then O(logN) + O(n) for each evaluation 
// spacetime would be O(1) as i'm just storing the n number and i can just mutate the original piles list when i sort, as it's not needed to return it or preserve it and order doesn't matter