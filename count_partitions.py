def count_partitions(n, m):
    def count_with_second_partition_fixed(first_partition, second_partition):
        if first_partition == 1:
            return 1
        count = 0
        count += count_with_second_partition_fixed(first_partition-1, second_partition)
        count = count + 1
        return count
    return count_with_second_partition_fixed(n-m, m)

n = 6   #positive integer n
m = 4   #parts upto size m
sum_of_partitions = 0
for i in range(m):
    sum_of_partitions += count_partitions(n, i+1)

print(sum_of_partitions)