class HashTable
  attr_reader :size, :buckets

  def initialize(size: 100)
    @size = size
    @buckets = [nil] * size
  end

  def [](key)
    bucket_key = key.hash % size

    buckets[bucket_key]
  end

  def []=(key, value)
    bucket_key = key.hash % size
    buckets[bucket_key] = value
  end
end

# TODO Implement linked list in the buckets
# to account for key collision and store key name
