import math
from typing import List

# Helper class for Segment Tree Node
class Node:
    def __init__(self, k):
        # Product of the elements in the node's range modulo k
        self.prod = 1 
        # counts[r] = number of prefixes starting at the node's range start (L)
        #              and ending within the node's range [L, R], with product % k == r
        self.counts = [0] * k
        # Example: range [L, R], nums[L]%k = r0, (nums[L]*nums[L+1])%k = r1,...
        # counts[r0]++, counts[r1]++, etc.

# Merge function to combine results from two nodes
def merge(left_node: Node, right_node: Node, k: int) -> Node:
    """
    Merges the results from left (range [L, mid]) and right (range [mid+1, R]) child nodes.
    The resulting node represents the combined range [L, R].
    """
    # If one node is the identity (e.g., from a query outside range), return the other.
    # Our identity node has prod=1 and counts=[0]*k. Merge logic handles this.
    
    merged_node = Node(k)
    
    # 1. Calculate the combined product
    merged_node.prod = (left_node.prod * right_node.prod) % k
    
    # 2. Calculate the combined counts (for prefixes starting at L)
    
    # Start with counts from prefixes ending in the left part [L, mid]
    for r in range(k):
        merged_node.counts[r] = left_node.counts[r]
        
    # Add contributions from prefixes ending in the right part [mid+1, R]
    # These are prefixes of the form nums[L...p] where p > mid.
    # product(nums[L...p]) % k = (left_node.prod * product(nums[mid+1...p])) % k
    left_prod_mod_k = left_node.prod
    for r_prime in range(k):
        # right_node.counts[r_prime] is the count of prefixes starting at mid+1 
        # ending in [mid+1, R] with product r_prime % k.
        if right_node.counts[r_prime] > 0:
            # The corresponding full prefix starting at L has this remainder:
            final_rem = (left_prod_mod_k * r_prime) % k
            # Add the count for these prefixes
            merged_node.counts[final_rem] += right_node.counts[r_prime]
            
    return merged_node

class SegmentTree:
    def __init__(self, initial_nums: List[int], k: int):
        self.n = len(initial_nums)
        self.k = k
        # Store the current state of nums internally
        self.nums = list(initial_nums) 
        # Allocate space for the tree (4*n is safe)
        self.tree = [Node(k) for _ in range(4 * self.n)]
        # Define an identity node for queries outside a node's range
        self.identity_node = Node(k)
        self.identity_node.prod = 1 # Multiplicative identity
        # counts=[0]*k ensures it doesn't add any prefix counts when merged

        if self.n > 0:
             self.build(0, 0, self.n - 1)

    def build(self, v: int, tl: int, tr: int):
        """ Builds the segment tree recursively """
        if tl == tr:
            # Leaf node representing nums[tl]
            val_mod_k = self.nums[tl] % self.k
            self.tree[v].prod = val_mod_k
            self.tree[v].counts = [0] * self.k
            # The single prefix nums[tl] has remainder val_mod_k
            self.tree[v].counts[val_mod_k] = 1
        else:
            # Internal node: build children and merge
            tm = tl + (tr - tl) // 2 # Midpoint calculation
            left_child_idx = 2 * v + 1
            right_child_idx = 2 * v + 2
            self.build(left_child_idx, tl, tm)
            self.build(right_child_idx, tm + 1, tr)
            # Combine results using the merge function
            self.tree[v] = merge(self.tree[left_child_idx], self.tree[right_child_idx], self.k)

    def _update(self, v: int, tl: int, tr: int, pos: int, new_val: int):
        """ Recursive helper for updating value at pos """
        if tl == tr:
            # Leaf node found
            if tl == pos: # Ensure we are at the correct leaf
                 val_mod_k = new_val % self.k
                 self.tree[v].prod = val_mod_k
                 self.tree[v].counts = [0] * self.k
                 self.tree[v].counts[val_mod_k] = 1
        else:
            # Internal node: update the relevant child and re-merge
            tm = tl + (tr - tl) // 2
            left_child_idx = 2 * v + 1
            right_child_idx = 2 * v + 2
            if pos <= tm:
                self._update(left_child_idx, tl, tm, pos, new_val)
            else:
                self._update(right_child_idx, tm + 1, tr, pos, new_val)
            # Recalculate this node's value after child update
            self.tree[v] = merge(self.tree[left_child_idx], self.tree[right_child_idx], self.k)

    def update(self, pos: int, new_val: int):
        """ Public interface for updating value at index pos """
        # Check bounds (although constraints likely guarantee validity)
        if 0 <= pos < self.n:
             # Update the internal nums array to reflect the change
             self.nums[pos] = new_val 
             # Update the tree structure
             self._update(0, 0, self.n - 1, pos, new_val)

    def _query(self, v: int, tl: int, tr: int, l: int, r: int) -> Node:
        """ Recursive helper for range query [l, r] """
        # Case 1: Query range [l, r] is completely outside node's range [tl, tr]
        if r < tl or l > tr or l > r: # l > r handles empty query ranges
            return self.identity_node 

        # Case 2: Node's range [tl, tr] is fully contained within query range [l, r]
        if l <= tl and tr <= r:
            return self.tree[v]
            
        # Case 3: Node's range partially overlaps query range: query children and merge
        tm = tl + (tr - tl) // 2
        left_child_idx = 2 * v + 1
        right_child_idx = 2 * v + 2
        
        # Recursively query left and right children. The query range [l, r] stays the same.
        left_result = self._query(left_child_idx, tl, tm, l, r)
        right_result = self._query(right_child_idx, tm + 1, tr, l, r)
        
        # Merge the results. The merge function correctly combines adjacent results.
        return merge(left_result, right_result, self.k)

    def query(self, l: int, r: int) -> Node:
        """ 
        Public interface for querying the properties of range [l, r].
        Returns a Node whose 'counts' array reflects prefix products *starting at l*
        and ending within [l, r].
        """
        # Ensure query bounds are valid within the array size
        # No need to clamp here as _query handles out-of-bounds via identity node.
        # However, checking for l > r upfront is useful.
        if l > r or l >= self.n or r < 0:
             return self.identity_node
        
        # Adjust bounds to be within [0, n-1] if necessary, although _query handles this.
        # l = max(0, l)
        # r = min(self.n - 1, r)
        # if l > r: return self.identity_node
             
        return self._query(0, 0, self.n - 1, l, r)


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # Initialize Segment Tree with the initial state of nums
        st = SegmentTree(nums, k) 
        
        results = []
        
        for query in queries:
            indexi, valuei, starti, xi = query
            
            # 1. Persistent Update: Update the segment tree and its internal nums copy
            # Constraints guarantee 0 <= indexi < n
            st.update(indexi, valuei)
            
            # 2. Query for Prefixes starting at starti
            # We need the counts of prefixes nums[starti...p] for starti <= p < n.
            # This corresponds to querying the segment tree for the range [starti, n-1].
            
            query_result_node = Node(k) # Default result if range is empty
            if starti < n: # Only query if the starting index is valid
                # Query the segment tree for the range [starti, n-1]
                query_result_node = st.query(starti, n - 1)
                # The result node's 'counts' array contains counts of prefixes
                # starting at starti and ending in [starti, n-1].
            # Else (starti >= n), the range is empty, result remains the identity node.
            
            # The answer is the count for the target remainder xi 
            answer = query_result_node.counts[xi]
            results.append(answer)
            
        return results