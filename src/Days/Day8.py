from Days.Base.BaseDay import BaseDay

class Challenge(BaseDay):
    def __init__(self, day=0):
        super().__init__(day)
    
    def calcP1(self):
        visible_trees = set()
        # __idee__ füge coordinaten der bäume in ein set ein. doppeltes zählen wird so umangen.
        # finde bäume sichtbar von LINKS
        for y_coord in range(len(self.input)):
            tree_line = self.input[y_coord]
            for x_coord in range(len(tree_line)):
                t_height = tree_line[x_coord]
                is_visible = True
                for left_tree_index in range(x_coord):
                    left_tree_height = tree_line[left_tree_index]
                    if left_tree_height >= t_height:
                        is_visible = False
                        break
                if is_visible:
                    visible_trees.add((x_coord, y_coord))
        left_seen = len(visible_trees)
        # print(f"{left_seen} trees seen from LEFT.")

        # finde bäume sichtbar von RECHTS
        for y_coord in range(len(self.input)):
            tree_line = self.input[y_coord]
            for x_coord in range(len(tree_line)):
                t_height = tree_line[x_coord]
                is_visible = True
                # ist Baum von rechts sehbar?
                for right_tree_index in range(x_coord+1, len(tree_line)):
                    right_tree_height = tree_line[right_tree_index]
                    if right_tree_height >= t_height:
                        is_visible = False
                        break
                if is_visible:
                    visible_trees.add((x_coord, y_coord))
        right_seen = len(visible_trees) - left_seen
        # print(f"{right_seen} new trees from seen from RIGHT.")

        # finde bäume sichtbar von OBEN
        for x_coord in range(len(self.input[0])):
            for y_coord in range(len(self.input)):
                tree_height = self.input[y_coord][x_coord]
                is_visible = True
                for t_t_index in range(y_coord):
                    top_tree_height = self.input[t_t_index][x_coord]
                    if top_tree_height >= tree_height:
                        is_visible = False
                        break
                if is_visible:
                    visible_trees.add((x_coord, y_coord))
        top_seen = len(visible_trees) - right_seen - left_seen
        # print(f"{top_seen} new trees from seen from TOP.")

        # finde bäume sichtbar von UNTEN 
        for x_coord in range(len(self.input[0])):
            for y_coord in range(len(self.input)):
                tree_height = self.input[y_coord][x_coord]
                is_visible = True
                for t_t_index in range(y_coord+1, len(self.input)):
                    top_tree_height = self.input[t_t_index][x_coord]
                    if top_tree_height >= tree_height:
                        is_visible = False
                        break
                if is_visible:
                    visible_trees.add((x_coord, y_coord))
        # bot_seen = len(visible_trees) - right_seen - left_seen - top_seen
        # print(f"{bot_seen} new trees from seen from BOTTOM.")
        
        return len(visible_trees)

    def calcP2(self):
        # __idee__ füge coordinaten der bäume in ein set ein. doppeltes zählen wird so umangen.
        best_score = -1
        for y_coord in range(1, len(self.input)-1):
            tree_line = self.input[y_coord]
            for x_coord in range(1, len(tree_line)-1):
                curr_tree = tree_line[x_coord]
                count_left = 0
                for l_t_index in range(x_coord-1, -1, -1):
                    left_tree = tree_line[l_t_index]
                    count_left += 1
                    if left_tree >= curr_tree:
                        break
                
                count_right = 0
                for r_t_index in range(x_coord+1, len(tree_line)):
                    right_tree = tree_line[r_t_index]
                    count_right += 1
                    if right_tree >= curr_tree:
                        break

                count_top = 0
                for t_t_index in range(y_coord-1,-1,-1):
                    top_tree = self.input[t_t_index][x_coord]
                    count_top += 1
                    if top_tree >= curr_tree:
                        break

                count_bot = 0
                for b_t_index in range(y_coord+1, len(self.input)):
                    bot_tree = self.input[b_t_index][x_coord]
                    count_bot += 1
                    if bot_tree >= curr_tree:
                        break
                
                curr_score = count_left*count_right*count_top*count_bot

                if curr_score > best_score:
                    best_score = curr_score

        return best_score