require 'spec_helper'

describe 'Node' do
  let(:node) { Node.new }

  describe '.new' do
    it 'initializes a new graph' do
      expect(node).to be_a Node
    end

    it 'sets data' do
      data = 'data'
      node = Node.new(data: data)

      expect(node.data).to eq data
    end

    it 'sets edges' do
      edges = [1,2,3]
      node = Node.new(edges: edges)

      expect(node.edges).to eq edges
    end
  end

  describe "#add_edge" do
    it 'adds an edge' do
      edge = rand(100)
      node.add_edge(edge)

      expect(node.edges).to include edge
    end
  end
end


describe 'Graph' do
  let(:node) { Node.new(data: rand(100)) }
  let(:graph) { Graph.new }

  describe '.new' do
    it 'initializes a new graph' do
      expect(graph).to be_a Graph
    end

    it 'initializes a new graph with nodes' do
      graph = Graph.new(nodes: [node])

      expect(graph.nodes).to eq [node]
    end
  end

  describe '#add_node' do
    it 'adds a node' do
      graph.add_node(node)
      expect(graph.nodes).to include node
    end
  end

  describe '#fetch_node' do
    it 'fetches a node' do
      graph.add_node(node)
      expect(graph.fetch_node(node)).to eq node
    end

    context 'node doesnt exist' do
      it 'returns nil' do
        expect(graph.fetch_node(node)).to be_nil
      end
    end
  end

  describe '#add_edge' do
    it 'adds and edge' do
      src = Node.new(data: rand(100))
      dest = Node.new(data: rand(100))

      graph.add_node(src)
      graph.add_node(dest)

      graph.add_edge(src: src, dest: dest)
      expect(src.edges).to include dest
    end

    context 'when dest or src doesnt exist' do
      it 'doesnt add edge' do
        src = Node.new(data: rand(100))
        dest = Node.new(data: rand(100))

        graph.add_node(src)

        expect { graph.add_edge(src: src, dest: dest) } .to raise_error
      end
    end
  end
end
