def int_to_binary(int)
  binary = ""

  while int > 0
    bit = (int%2).to_s
    binary.prepend(bit)
    int /= 2
  end

  binary
end
