class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_rel = max_rel = cur_rel = 0

        for diff in differences:
            cur_rel += diff

            min_rel = min(min_rel, cur_rel)
            max_rel = max(max_rel, cur_rel)

            if max_rel - min_rel > upper - lower:
                return 0
        
        return (upper - lower) - (max_rel - min_rel) + 1




# 1. Understanding the Core Relationship
#     -> You're given differences[i] = hidden[i+1] - hidden[i].
#     -> This means hidden[i+1] = hidden[i] + differences[i].
#     -> Crucially, if you know any single element of the hidden sequence (let's say hidden[0]), you can determine the entire sequence.
#     -> hidden[1] = hidden[0] + differences[0]
#     -> hidden[2] = hidden[1] + differences[1] = (hidden[0] + differences[0]) + differences[1]
#     -> hidden[k] = hidden[0] + sum(differences[j] for j in 0..k-1)

# 2. The "Shape" vs. the "Position"
#     -> The differences array defines the shape or the relative changes within the hidden sequence. Adding differences[i] tells you how much the sequence goes up or down at step i.
#     -> The actual values in the hidden sequence depend entirely on the starting value, hidden[0]. Changing hidden[0] just shifts the entire sequence up or down without changing its shape (the differences between consecutive elements remain the same).

# 3. The Constraint: [lower, upper]
#     -> The only thing that makes a potential hidden sequence valid or invalid (once we fix the shape using differences) is whether all its elements fall within the inclusive range [lower, upper].



# 5. The Optimized Solution: Focusing on Relative Range
#     -> Insight: Instead of simulating every possible start value, let's analyze the shape defined by differences and see how much "vertical space" it needs.
#     -> Relative Sequence: Imagine a sequence starting at 0. Let's call it relative_hidden.
#     -> relative_hidden[0] = 0
#     -> relative_hidden[1] = differences[0]
#     -> relative_hidden[2] = differences[0] + differences[1]
#     -> relative_hidden[k] = sum(differences[j] for j in 0..k-1) (This is the prefix sum of differences).

#     -> Any actual valid hidden sequence is just hidden[k] = hidden[0] + relative_hidden[k].

#     -> Finding the Relative Range: Let's find the minimum (min_rel) and maximum (max_rel) values achieved in this relative_hidden sequence (including the starting 0).
#         -> The variable cur_rel in the solution tracks the current relative_hidden value as we iterate through differences.
#         -> min_rel = min(min_rel, cur_rel) keeps track of the minimum relative value seen so far (min_rel).
#         -> max_rel = max(max_rel, cur_rel) keeps track of the maximum relative value seen so far (max_rel).

#     -> After this loop, y - x represents the total range or "vertical height" required by the shape defined by differences. (max_rel - min_rel).

#     -> Connecting Relative Range to Bounds:
#         -> For the actual hidden sequence (starting at hidden[0]) to be valid, we need:
#         -> lower <= hidden[k] <= upper for all k.
#         -> lower <= hidden[0] + relative_hidden[k] <= upper for all k.

#     -> This must hold even for the minimum and maximum relative values:
#         -> lower <= hidden[0] + min_rel => hidden[0] >= lower - min_rel
#         -> hidden[0] + max_rel <= upper => hidden[0] <= upper - max_rel

#     -> So, the only valid starting values hidden[0] are those that satisfy:
#         -> lower - min_rel <= hidden[0] <= upper - max_rel


#     -> Counting the Possibilities: How many integers hidden[0] can satisfy this range?
#         -> The number of integers in an inclusive range [A, B] is B - A + 1, provided B >= A.
#         -> Number of valid hidden[0] = (upper - max_rel) - (lower - min_rel) + 1
#         -> Number of valid hidden[0] = upper - max_rel - lower + min_rel + 1
#         -> Number of valid hidden[0] = (upper - lower) - (max_rel - min_rel) + 1

#     -> This directly calculates the number of possible integer values for hidden[0] that guarantee the entire shifted sequence stays within the [lower, upper] bounds.


#     -> Handling Impossibility (The Early Exit / Condition):
#         -> What if the required range max_rel - min_rel (the height of the relative sequence) is larger than the allowed range upper - lower?
#         -> If max_rel - min_rel > upper - lower, then it's impossible to fit the sequence shape within the bounds, no matter how you shift it. There are no valid hidden[0] values.
#         -> In this case, the formula (upper - lower) - (max_rel - min_rel) + 1 would result in a value less than 1 (0 or negative).