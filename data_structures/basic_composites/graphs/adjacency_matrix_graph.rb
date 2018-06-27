module AdjacencyMatrix
  class Node
    attr_reader :location, :edges

    def initialize(location:, edges:)
        @location = location
        @edges = edges
    end
  end

  class AdjacencyMatrix
    attr_reader :size, :matrix, :nodes

    def initialize(size:)
      raise ArgumentError unless size > 1
      @size = size
      @matrix = 1.upto(size).map { |_| [nil] * size }
      @nodes = {}
    end

    def add_node(node)
      if node.edges.length != size
        raise ArgumentError
      end

      matrix_node = matrix[node.location]

      matrix_node.each_with_index do |val, index|
        matrix_node[index] = node.edges[index]
      end

      nodes[node.location] = node
    end

    def add_nodes_from_array(nodes)
      if nodes.length != size || nodes.first.length != size
        raise ArgumentError
      end

      nodes.each_with_index do |node, index|
        node = Node.new(location: index, edges: node)
        add_node(node)
      end

      self
    end

    def get_node(location)
      nodes.fetch(location, nil)
    end
  end
end
