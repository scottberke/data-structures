
class Node
  attr_accessor :data, :edges

  def initialize(data: nil, edges: [])
    @data = data
    @edges = edges
  end

  def add_edge(edge)
    edges.push(edge)
  end
end

class Graph
  attr_accessor :nodes

  def initialize(nodes: [])
    @nodes = nodes
  end

  def add_node(node)
    nodes.push(node)
  end

  def add_edge(src:, dest:)
    src = fetch_node(src)
    dest = fetch_node(dest)

    raise "src and dest must exist" unless src && dest

    src.add_edge(dest) 
  end

  def fetch_node(node)
    node_index = nodes.find_index(node)
    begin
      nodes[node_index]
    rescue
      nil
    end
  end
end
