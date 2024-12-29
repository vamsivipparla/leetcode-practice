class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Convert wordList to a set for O(1) lookups
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # Preprocess words to create adjacency list for generic transformations
        adj_list = defaultdict(list)
        length = len(beginWord)

        for word in wordSet:
            for i in range(length):
                pattern = word[:i] + "*" + word[i+1:]
                adj_list[pattern].append(word)

        # BFS initialization
        queue = deque([(beginWord, 1)])  # (current_word, transformation_steps)
        visited = set()
        visited.add(beginWord)

        while queue:
            current_word, steps = queue.popleft()

            for i in range(length):
                # Generate intermediate patterns for the current word
                pattern = current_word[:i] + "*" + current_word[i+1:]

                # Explore all neighbors (words matching the pattern)
                for neighbor in adj_list[pattern]:
                    if neighbor == endWord:
                        return steps + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))

                # Clear the list to save memory
                adj_list[pattern] = []

        return 0