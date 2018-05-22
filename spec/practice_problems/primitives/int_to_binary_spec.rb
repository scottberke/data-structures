

describe 'int_to_binary' do
  it 'converts 1 to binary' do
    int = 1
    binary = '1'
    expect(int_to_binary(int)).to eq binary
  end

  it 'converts 2 to binary' do
    int = 2
    binary = '10'
    expect(int_to_binary(int)).to eq binary
  end

  it 'converts 3 to binary' do
    int = 3
    binary = '11'
    expect(int_to_binary(int)).to eq binary
  end

  it 'converts 4 to binary' do
    int = 4
    binary = '100'
    expect(int_to_binary(int)).to eq binary
  end

  it 'converts all the numbers' do
    max = rand(1000)
    1.upto(max) do |int|
      expect(int_to_binary(int)).to eq int.to_s(2)
    end
  end

end
