require 'spec_helper'

describe 'binary_to_int' do
  it 'converts binary 1 to int' do
    int = 1
    binary = '1'

    expect(binary_to_int(binary)).to eq int
  end

  it 'converts binary 2 to int' do
    int = 2
    binary = '10'

    expect(binary_to_int(binary)).to eq int
  end

  it 'converts binary 3 to int' do
    int = 3
    binary = '11'

    expect(binary_to_int(binary)).to eq int
  end

  it 'converts binary 4 to int' do
    int = 4
    binary = '100'

    expect(binary_to_int(binary)).to eq int
  end

  it 'converts all binary numbers to int' do
    max = rand(1000)

    1.upto(max) do |int|
      binary = int.to_s(2)
      expect(binary_to_int(binary)).to eq int
    end
  end
end
