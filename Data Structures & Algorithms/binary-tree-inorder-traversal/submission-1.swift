/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     var val: Int
 *     var left: TreeNode?
 *     var right: TreeNode?
 *     init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */

class Solution {
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        var result: [Int] = []

        func dfs(_ node: TreeNode?) {
            guard let node = node else { return }

            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        }

        dfs(root)
        return result
    }
}
