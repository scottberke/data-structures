require 'spec_helper'


describe 'Hash Table' do
  describe '.new' do
    it 'creates a hash table' do
      hash_table = HashTable.new
      expect(hash_table).to be_a HashTable
    end

    it 'sets size' do
      size = rand(100)
      hash_table = HashTable.new(size: size)

      expect(hash_table.size).to eq size
    end

    it 'creates buckets' do
      size = rand(100)
      hash_table = HashTable.new(size: size)

      expect(hash_table.buckets.length).to eq size
    end
  end

  describe 'getters and setters' do
    let(:hash_table) { HashTable.new }
    describe 'setter' do
      it 'sets a value associated to a key' do
        value = rand(100)
        key = 'key'

        expect(hash_table[key] = value).to eq value
      end

      describe 'getter' do
        it 'gets a value given a key' do
          value = rand(100)
          key = 'key'
          hash_table[key] = value

          expect(hash_table[key]).to eq value    
        end
      end
    end
  end
end
