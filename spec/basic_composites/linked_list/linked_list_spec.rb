require 'spec_helper'

describe 'Linked List' do
  describe '.new' do
    let(:linked_list) { LinkedList::LinkedList.new }
    let(:node) { LinkedList::Node.new(data: 'data') }

    it 'creates a new linked list' do
        expect(linked_list).to be_a LinkedList::LinkedList
    end

    it 'sets a head' do
       ll_w_head = LinkedList::LinkedList.new(head: node)

       expect(ll_w_head.head).to eq node
    end

    it 'sets a tail' do
      ll_w_tail = LinkedList::LinkedList.new(head: node)

      expect(ll_w_tail.tail).to eq node
    end

  end

  describe '#append' do
    let(:linked_list) { LinkedList::LinkedList.new }
    let(:node) { LinkedList::Node.new(data: 'data') }

    it 'adds a new node to the linked list' do
      linked_list = LinkedList::LinkedList.new(head: node)
      new_node = LinkedList::Node.new(data: 'new node')

      linked_list.append(new_node)

      expect(linked_list.tail).to eq new_node
      expect(linked_list.head.next).to eq new_node
    end

    it 'adds a new node and sets head if empty' do
      expect(linked_list.head).to be_nil

      linked_list.append(node)

      expect(linked_list.head).to eq node
      expect(linked_list.tail).to eq node
    end

  end

  describe '#push' do
    let(:node) { LinkedList::Node.new(data: 'data') }
    let(:linked_list) { LinkedList::LinkedList.new(head: node) }

    it 'inserts new node into head' do
      new_node = LinkedList::Node.new(data: 'new_node')
      linked_list.push(new_node)

      expect(linked_list.head).to eq new_node
      expect(linked_list.tail).to eq node
    end
  end

  describe '#insert_after' do
    let(:node) { LinkedList::Node.new(data: 'data') }
    let(:linked_list) { LinkedList::LinkedList.new(head: node) }

    it 'inserts node after specified node' do
      second_node = LinkedList::Node.new(data: 'second_node')
      third_node = LinkedList::Node.new(data: 'third_node')

      linked_list.append(second_node)

      linked_list.insert_after(node: third_node, after: node.data)

      expect(linked_list.head).to eq node
      expect(linked_list.head.next).to eq third_node
      expect(linked_list.tail).to eq second_node
    end

    it 'updates tail if inserted node is last' do
      second_node = LinkedList::Node.new(data: 'second_node')
      third_node = LinkedList::Node.new(data: 'third_node')

      linked_list.append(second_node)

      expect(linked_list.tail).to eq second_node

      linked_list.insert_after(node: third_node, after: second_node.data)

      expect(linked_list.tail).to eq third_node
    end
  end

  describe '#get' do
    let(:node) { LinkedList::Node.new(data: 'data') }
    let(:linked_list) { LinkedList::LinkedList.new(head: node) }

    it 'gets the specified node by data' do
      second_node = LinkedList::Node.new(data: 'second_node')
      third_node = LinkedList::Node.new(data: 'third_node')

      linked_list.append(second_node)
      linked_list.append(third_node)

      expect(linked_list.get(third_node.data)).to eq third_node
      expect(linked_list.get(second_node.data)).to eq second_node
      expect(linked_list.get(node.data)).to eq node
    end

    context 'data doesnt exist in linked list' do
      it 'returns nil' do
        second_node = LinkedList::Node.new(data: 'second_node')
        third_node = LinkedList::Node.new(data: 'third_node')

        linked_list.append(second_node)
        linked_list.append(third_node)

        misc_data = 'fourth_node'

        expect(linked_list.get(misc_data)).to be_nil
      end

    end
  end

  describe '#delete_node' do
    let(:node) { LinkedList::Node.new(data: 'data') }
    let(:linked_list) { LinkedList::LinkedList.new(head: node) }

    it 'deletes the node' do
      second_node = LinkedList::Node.new(data: 'second_node')
      third_node = LinkedList::Node.new(data: 'third_node')

      linked_list.append(second_node)
      linked_list.append(third_node)

      expect(linked_list.delete_node(second_node.data)).to eq second_node
    end

    it 'updates head when deleted node is head' do
      second_node = LinkedList::Node.new(data: 'second_node')
      third_node = LinkedList::Node.new(data: 'third_node')

      linked_list.append(second_node)
      linked_list.append(third_node)
      linked_list.delete_node(node.data)

      expect(linked_list.head).to eq second_node
    end

    it 'updates tail when deleted node is tail' do
      second_node = LinkedList::Node.new(data: 'second_node')
      third_node = LinkedList::Node.new(data: 'third_node')

      linked_list.append(second_node)
      linked_list.append(third_node)
      linked_list.delete_node(third_node.data)

      expect(linked_list.tail).to eq second_node
    end

    context 'node isnt in list' do
      it 'returns nil' do
        second_node = LinkedList::Node.new(data: 'second_node')
        third_node = LinkedList::Node.new(data: 'third_node')

        linked_list.append(second_node)
        linked_list.append(third_node)

        misc_data = 'fourth_node'
        expect(linked_list.delete_node(misc_data)).to be_nil
      end
    end
  end
end
