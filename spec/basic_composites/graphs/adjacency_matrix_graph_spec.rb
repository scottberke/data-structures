require 'spec_helper'


describe 'Adjacency Matrix Graph' do
  describe '.new' do
    it 'creates an AdjacencyMatrix' do
      expect(AdjacencyMatrix::AdjacencyMatrix.new(size: 2)).to be_a AdjacencyMatrix::AdjacencyMatrix
    end

    it 'sets the size' do
      size = rand(2..10)
      matrix = AdjacencyMatrix::AdjacencyMatrix.new(size: size)
      expect(matrix.size).to eq size
    end

    context 'invalid size' do
      it 'raises an attribute error' do
        size = 0
        expect { AdjacencyMatrix::AdjacencyMatrix.new(size: size) }.to raise_error ArgumentError
      end
    end

    it 'sets matrix' do
      size = rand(2..10)
      matrix = AdjacencyMatrix::AdjacencyMatrix.new(size: size)

      expect(matrix.matrix.length).to eq size
      expect(matrix.matrix[0].length).to eq size
    end

    it 'sets nodes' do
      size = rand(2..10)
      matrix = AdjacencyMatrix::AdjacencyMatrix.new(size: size)

      expect(matrix.nodes).to be_a Hash
    end
  end

  describe '#add_node' do
    let(:size) { rand(3..10) }
    let(:edges) do
      edges = [nil] * size
      edges.map { |edge| edge = rand(0..3) }
    end

    let(:node) { AdjacencyMatrix::Node.new(location: 0, edges: edges) }
    let(:matrix) { AdjacencyMatrix::AdjacencyMatrix.new(size: size) }

    it 'adds a node' do
      matrix.add_node(node)

      matrix.matrix[0].each_with_index do |val, index|
        expect(val).to eq node.edges[index]
      end

      nodes_hash = { node.location => node }
      expect(matrix.nodes).to eq nodes_hash
    end

    context 'node with different size' do
      it 'raises an error' do
        matrix = AdjacencyMatrix::AdjacencyMatrix.new(size: size - 1)

        expect { matrix.add_node(node) }.to raise_error ArgumentError
      end
    end
  end

  describe '#add_nodes_from_array' do
    let(:size) { rand(2..10) }
    let(:matrix_array) do
      nodes = 1.upto(size).map { |_| [nil] * size }
      nodes.map { |node| node.map! { |edge| edge = rand(0..3) } }
    end

    let(:matrix) { AdjacencyMatrix::AdjacencyMatrix.new(size: size) }

    it 'addes nodes from an array' do
      matrix.add_nodes_from_array(matrix_array)

      expect(matrix.matrix).to eq matrix_array
    end
  end

  describe '#get_node' do
    let(:size) { rand(2..10) }
    let(:matrix_array) do
      nodes = 1.upto(size).map { |_| [nil] * size }
      nodes.map { |node| node.map! { |edge| edge = rand(0..3) } }
    end

    let(:matrix) do
      AdjacencyMatrix::AdjacencyMatrix.new(size: size).
        add_nodes_from_array(matrix_array)
    end

    it 'gets the node' do
      node_location = 0

      node = matrix.get_node(node_location)
      expect(node.edges).to eq matrix_array[node_location]
    end

    context 'location out of range' do
      it 'returns nil' do
        node_location = size + 1

        node = matrix.get_node(node_location)
        expect(node).to be_nil
      end
    end
  end
end
