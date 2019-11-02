class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        i_map = {}
        j_map = {}
        count = 0
        visited_map = {}
        for elem in stones:
            if i_map.get(elem[0]):
                i_map.get(elem[0]).append(elem)
            else:
                i_map[elem[0]] = [elem]
            if j_map.get(elem[1]):
                j_map.get(elem[1]).append(elem)
            else:
                j_map[elem[1]] = [elem]
            visited_map[tuple(elem)] = False
        print(i_map)
        print(j_map)
        print(visited_map)
        for elem in stones:
            count_inc = False
            for i_elem in i_map[elem[0]]:
                if i_elem != elem and not visited_map[tuple(i_elem)]:
                    visited_map[tuple[i_elem]] = True
                    count += 1
                    count_inc = True
                    break
            if not count_inc:
                for j_elem in j_map[elem[1]]:
                    if j_elem != elem and not visited_map[tuple(j_elem)]:
                        visited_map[tuple[j_elem]] = True
                        count += 1
                        break
            visited_map[tuple(elem)] = True
        return count







