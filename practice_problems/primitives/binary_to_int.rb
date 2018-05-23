BASE = 2
def binary_to_int(binary)
  reversed_binary = binary.reverse!
  accumulator = 0

  reversed_binary.each_char.with_index(0) do |char, index|
    accumulator += (BASE**index * char.to_i)
  end

  accumulator
end
