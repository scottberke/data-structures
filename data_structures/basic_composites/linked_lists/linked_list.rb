module LinkedList
  class Node
    attr_accessor :data, :next

    def initialize(data: nil)
      @data = data
      @next = nil
    end
  end

  class LinkedList
    attr_accessor :head, :tail

    def initialize(head: nil)
      @head = head
      @tail = head
    end

    def get(data)
      current_node = self.head

      while current_node.data != data && current_node.next
        current_node = current_node.next
      end

      current_node.data == data ? current_node : nil
    end

    def append(node)
      if !self.head
        self.head = node
        self.tail = node
      else
        current_node = self.head

        while current_node.next
          current_node = current_node.next
        end

        current_node.next = node
        self.tail = node
      end
    end

    def push(node)
      node.next = self.head
      self.head = node
    end

    def insert_after(node:, after:)
      after_node = self.get(after)

      node.next = after_node.next
      after_node.next = node

      if node.next.nil?
        self.tail = node
      end
    end

    def delete_node(data)
      if self.head.data == data
        node = self.head
        self.head = node.next

        return node
      end

      current_node = self.head
      while current_node.next
        if current_node.next.data == data
          node = current_node.next
          current_node.next = node.next

          if current_node.next.nil?
            self.tail = current_node
          end

          return node
        end

        current_node = current_node.next
      end

      return nil
    end
  end
end
