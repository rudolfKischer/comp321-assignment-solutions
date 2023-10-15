

s, c, k = [int(num) for num in input().split()]

socks = [int(sock) for sock in input().split()]

socks.sort()

num_of_socks = s
bucket_size = c
max_diff = k

bucket_count = 1
bucket_min_sock = socks[0]
bucket_fill = 0

for sock in socks:

    if  bucket_fill >= bucket_size or (max_diff) < (sock - bucket_min_sock):
        bucket_min_sock = sock
        bucket_count += 1
        bucket_fill = 0
        continue

    bucket_fill +=1

print(bucket_count)

    
