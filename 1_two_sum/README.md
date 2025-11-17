Created a dictionary seen = {} to store numbers already processed.

Used enumerate() to iterate through the array with index and value.

For each value, calculated the missing number needed to reach the target: need = target - v.

If need exists in the dictionary, we found the correct pair and print their indices.

Otherwise, store the current value and index in seen.
like seen[value] = i
