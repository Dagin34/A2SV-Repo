depth = int(input())
road_lights = list(map(int, input().split()))

total_nodes = (1 << (depth + 1)) - 1
edge_weights = [0] * (total_nodes + 1)

for i in range(2, total_nodes + 1):
    edge_weights[i] = road_lights[i - 2]

additional = 0

def sync_paths(current_node):
    global additional

    left_child = 2 * current_node
    right_child = 2 * current_node + 1

    if left_child > total_nodes:
        return 0
    
    left_path_weight = sync_paths(left_child) + edge_weights[left_child]
    right_path_weight = sync_paths(right_child) + edge_weights[right_child]

    max_weight = max(left_path_weight, right_path_weight)

    additional += (max_weight - left_path_weight)
    additional += (max_weight - right_path_weight)

    return max_weight

sync_paths(1)
print(additional)