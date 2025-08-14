class sorting_class:
      def __init__(self, values, colors):
            self.values = values
            self.colors = colors

      def select_sort(self):
            n = len(self.values)
            for i in range(n):
                  min_index = i
                  for j in range(i + 1, n):
                        if self.values[j] < self.values[min_index]:
                              min_index = j

      
      def insert_sort(self):
            n = len(self.values)

            for i in range(1, n):
                  key = self.values[i]
                  j = i - 1
                  while j >= 0 and key < self.values[j]:
                        self.values[j + 1] = self.values[j]
                        j -= 1
                  self.values[j + 1] = key